import os
import re
import requests
from datetime import datetime
from docx import Document
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
import json
# Agregar al inicio del script:
import logging
from typing import Optional, Dict, Any

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('cv_generator.log'),
        logging.StreamHandler()
    ]
)

class CVGeneratorError(Exception):
    """Excepción personalizada para errores del generador"""
    pass

class ConfigurationError(CVGeneratorError):
    """Error de configuración"""
    pass

class FileProcessingError(CVGeneratorError):
    """Error procesando archivos"""
    pass

class GeneradorCVInteligente:
    def __init__(self, config_path="config.json"):
        # Cargar configuración
        try:
            self.config = self.cargar_configuracion(config_path)
            self.cv_base_path = self.config['configuracion_general']['cv_base_path']
            self.carpeta_salida = self.config['configuracion_general']['carpeta_salida']
            self.umbral_fit = self.config['configuracion_general']['umbral_fit']
            self.perfil_tecnico = self.config['perfil_tecnico']
            logging.info(f"✅ Configuración cargada desde {config_path}")
        except Exception as e:
            raise ConfigurationError(f"Error cargando configuración: {e}")
        
        # Validar CV base
        if not self.validar_cv_base():
            raise FileProcessingError("CV base no válido")
            
        os.makedirs(self.carpeta_salida, exist_ok=True)
        
        # Adaptaciones del CV según el tipo de posición
        self.adaptaciones_cv = {
            'qa_automatizacion': {
                'titulo': 'QA Automation Engineer & Full Stack Developer',
                'resumen_adicional': 'Especializado en automatización de pruebas con Selenium, desarrollo de frameworks de testing y desarrollo full stack. Experiencia combinando desarrollo y QA en proyectos críticos.',
                'experiencias_extra': [
                    'Desarrollo de suites automatizadas usando Selenium WebDriver con Java y Python',
                    'Implementación de Page Object Model para mantener código reutilizable y escalable',
                    'Automatización de pruebas de APIs REST con validaciones de respuesta y datos',
                    'Desarrollo y testing simultáneo de funcionalidades en proyectos municipales'
                ]
            },
            'qa_manual': {
                'titulo': 'QA Manual Engineer & Full Stack Developer',
                'resumen_adicional': 'Especializado en testing funcional frontend y backend con enfoque en validación de datos críticos. Experiencia única combinando desarrollo y testing manual.',
                'experiencias_extra': [
                    'Ejecución de casos de prueba manuales en sistemas críticos desarrollados internamente',
                    'Validaciones cruzadas entre sistemas y bases de datos con conocimiento profundo del código',
                    'Documentación detallada de defectos y evidencias funcionales',
                    'Testing de funcionalidades desarrolladas en Python/FastAPI y Next.js'
                ]
            },
            'desarrollador_python': {
                'titulo': 'Python Full Stack Developer & QA Engineer',
                'resumen_adicional': 'Desarrollador especializado en Python con enfoque en calidad. Experiencia en FastAPI, desarrollo de APIs REST e integración con bases de datos PostgreSQL, complementado con expertise en testing.',
                'experiencias_extra': [
                    'Desarrollo de APIs REST escalables con Python y FastAPI en proyectos municipales',
                    'Implementación de microservicios con testing integrado desde el desarrollo',
                    'Optimización de consultas SQL y gestión de bases de datos PostgreSQL',
                    'Desarrollo de dashboards y paneles administrativos con Vue.js y Quasar'
                ]
            },
            'desarrollador_java': {
                'titulo': 'Java Developer & QA Engineer',  # Se ajustará según el nivel
                'resumen_adicional': 'Desarrollador con base sólida en Python/FastAPI y experiencia en QA. Mi experiencia en desarrollo backend y metodologías de testing me proporciona una excelente base para trabajar con Java.',
                'experiencias_extra': [
                    'Experiencia transferible desde Python/FastAPI hacia ecosistema Java/Spring',
                    'Base sólida en desarrollo de APIs REST y microservicios',
                    'Experiencia práctica en testing que complementa el desarrollo',
                    'Conocimiento en metodologías ágiles y mejores prácticas de desarrollo'
                ]
            }
        }

    def cargar_configuracion(self, config_path: str) -> Dict[str, Any]:
        """Carga la configuración desde archivo JSON"""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise ConfigurationError(f"Archivo de configuración no encontrado: {config_path}")
        except json.JSONDecodeError as e:
            raise ConfigurationError(f"Error en formato JSON: {e}")

    def validar_cv_base(self) -> bool:
        """Valida que el CV base exista y sea válido"""
        try:
            if not os.path.exists(self.cv_base_path):
                raise FileProcessingError(f"CV base no encontrado: {self.cv_base_path}")
            
            # Verificar que sea un archivo Word válido
            try:
                doc = Document(self.cv_base_path)
                if len(doc.paragraphs) < 5:
                    raise FileProcessingError("CV base parece estar vacío o corrupto")
            except Exception as e:
                raise FileProcessingError(f"Error leyendo CV base: {e}")
            
            logging.info(f"✅ CV base validado: {self.cv_base_path}")
            return True
            
        except FileProcessingError as e:
            logging.error(f"❌ Error validando CV base: {e}")
            return False

    def detectar_salario(self, texto_postulacion: str) -> Dict[str, Any]:
        """Detecta rangos salariales en la postulación"""
        resultado = {
            'salario_detectado': False,
            'moneda': None,
            'rango_min': None,
            'rango_max': None,
            'es_competitivo': None,
            'alertas': []
        }
        
        texto = texto_postulacion.lower()
        
        # Patrones para detectar salarios
        patrones_usd = [
            r'usd\s*(\d+(?:\.\d{3})*)',
            r'dolares?\s*(\d+(?:\.\d{3})*)',
            r'\$\s*(\d+(?:\.\d{3})*)\s*usd'
        ]
        
        patrones_ars = [
            r'\$\s*(\d+(?:\.\d{3})*)',
            r'pesos\s*(\d+(?:\.\d{3})*)',
            r'ars\s*(\d+(?:\.\d{3})*)'
        ]
        
        # Buscar USD primero
        for patron in patrones_usd:
            matches = re.findall(patron, texto)
            if matches:
                resultado['salario_detectado'] = True
                resultado['moneda'] = 'USD'
                salarios = [int(m.replace('.', '')) for m in matches]
                resultado['rango_min'] = min(salarios)
                resultado['rango_max'] = max(salarios) if len(salarios) > 1 else None
                break
        
        # Si no encontró USD, buscar ARS
        if not resultado['salario_detectado']:
            for patron in patrones_ars:
                matches = re.findall(patron, texto)
                if matches:
                    resultado['salario_detectado'] = True
                    resultado['moneda'] = 'ARS'
                    salarios = [int(m.replace('.', '')) for m in matches]
                    resultado['rango_min'] = min(salarios)
                    resultado['rango_max'] = max(salarios) if len(salarios) > 1 else None
                    break
        
        # Evaluar competitividad
        if resultado['salario_detectado'] and resultado['moneda'] == 'USD':
            min_esperado = self.config['deteccion_salarios']['salario_minimo_esperado_usd']
            max_esperado = self.config['deteccion_salarios']['salario_maximo_esperado_usd']
            
            if resultado['rango_min'] < min_esperado:
                resultado['alertas'].append(f"💰 Salario bajo: ${resultado['rango_min']} USD (mínimo esperado: ${min_esperado})")
                resultado['es_competitivo'] = False
            elif resultado['rango_min'] > max_esperado:
                resultado['alertas'].append(f"🎯 Salario alto: ${resultado['rango_min']} USD (máximo esperado: ${max_esperado})")
                resultado['es_competitivo'] = True
            else:
                resultado['es_competitivo'] = True
                resultado['alertas'].append(f"✅ Salario competitivo: ${resultado['rango_min']} USD")
        
        return resultado

    def cargar_cv_base(self):
        """Carga el CV base desde archivo Word"""
        try:
            doc = Document(self.cv_base_path)
            return "\n".join([p.text for p in doc.paragraphs if p.text.strip() != ""])
        except Exception as e:
            print(f"Error cargando CV base: {e}")
            return ""

    def detectar_tipo_posicion(self, texto_postulacion):
        """Detecta el tipo de posición y nivel basado en el texto de la postulación"""
        texto = texto_postulacion.lower()
        
        # Contadores para cada tipo (solo áreas donde tenemos experiencia)
        puntos = {
            'qa_automatizacion': 0,
            'qa_manual': 0,
            'desarrollador_python': 0,
            'desarrollador_java': 0,
            'desarrollador_frontend': 0,
            'desarrollador_fullstack': 0
        }
        
        # Palabras clave para QA Automatización
        if any(kw in texto for kw in ['automatización', 'selenium', 'automatizador', 'automation', 'locust', 'cypress']):
            puntos['qa_automatizacion'] += 3
        
        # Palabras clave para QA Manual
        if any(kw in texto for kw in ['qa funcional', 'testing funcional', 'qa manual', 'casos de prueba']):
            puntos['qa_manual'] += 3
            
        # Primero verificar si hay tecnologías que NO conocemos
        tecnologias_no_conocidas = self.config['tecnologias_no_conocidas']
        
        if any(tech in texto for tech in tecnologias_no_conocidas):
            print(f">>> 🚫 Tecnologías detectadas fuera de nuestro perfil: {[tech for tech in tecnologias_no_conocidas if tech in texto]}")
            return None, None
        
        # Palabras clave para Python (más específicas)
        if any(kw in texto for kw in ['python', 'django', 'flask', 'fastapi', 'pandas', 'numpy']):
            puntos['desarrollador_python'] += 3
            
        # Palabras clave para Java
        if any(kw in texto for kw in ['java', 'spring', 'spring boot', 'hibernate']):
            puntos['desarrollador_java'] += 3
            
        # Palabras clave para Frontend
        if any(kw in texto for kw in ['vue.js', 'vue', 'angular', 'frontend', 'front-end', 'javascript', 'typescript']):
            puntos['desarrollador_frontend'] += 3
            
        # Palabras clave para Full Stack
        if any(kw in texto for kw in ['full stack', 'fullstack', 'full-stack']):
            puntos['desarrollador_fullstack'] += 3
        
        # Palabras generales QA
        if any(kw in texto for kw in ['qa', 'testing', 'pruebas', 'quality assurance']):
            puntos['qa_automatizacion'] += 1
            puntos['qa_manual'] += 1
            
        # Palabras generales desarrollo (solo si no hay tecnologías específicas detectadas)
        palabras_desarrollo_general = ['desarrollador', 'developer', 'programador']
        if any(kw in texto for kw in palabras_desarrollo_general):
            # Solo asignar puntos generales si ya hay alguna tecnología específica detectada
            if max(puntos.values()) > 0:
                for tipo in puntos:
                    if puntos[tipo] > 0:
                        puntos[tipo] += 1
            else:
                # Si no hay tecnologías específicas, no asignar puntos automáticamente
                print(">>> ⚠️ Menciona 'desarrollador' pero sin tecnologías específicas de nuestro perfil")
                pass
        
        # Si no detecta nada de nuestras categorías, rechazar automáticamente
        if max(puntos.values()) == 0:
            print(f">>> 🚫 POSICIÓN FUERA DE NUESTRAS ÁREAS DE EXPERIENCIA")
            print(f">>> Texto analizado: {texto[:200]}...")
            print(f">>> Solo aplicamos a: QA, Python, Java, Frontend, Full Stack")
            return None, None
        
        tipo_base = max(puntos, key=puntos.get)
        max_puntos = puntos[tipo_base]
        
        # Mostrar información de detección
        print(f">>> Detección: {tipo_base} (puntos: {max_puntos})")
        
        # Detectar nivel de seniority
        nivel = self.detectar_nivel_seniority(texto)
        
        return tipo_base, nivel
    
    def detectar_nivel_seniority(self, texto):
        """Detecta el nivel de seniority requerido"""
        texto_lower = texto.lower()
        
        # Primero detectar SSR y variantes específicas de semi-senior
        if any(kw in texto_lower for kw in ['ssr', 'semi senior', 'semi-senior', 'advance', 'intermedio']):
            return 'semi_senior'
        elif any(kw in texto_lower for kw in ['junior', 'jr', 'trainee', 'entry level', 'sin experiencia']):
            return 'junior'
        elif any(kw in texto_lower for kw in ['senior', ' sr ', 'lead', 'líder', 'tech lead']):
            return 'senior'
        else:
            return 'semi_senior'  # Default

    def extraer_keywords_avanzado(self, texto_postulacion):
        """Extrae keywords relevantes de la postulación"""
        texto = texto_postulacion.lower()
        keywords_encontradas = []
        
        # Buscar en todas las categorías
        for categoria, keywords in self.perfil_tecnico.items():
            for kw in keywords:
                if kw in texto:
                    keywords_encontradas.append(kw)
        
        # Si no encuentra nada, buscar palabras más generales
        if not keywords_encontradas:
            palabras_generales = ['qa', 'testing', 'pruebas', 'developer', 'desarrollador', 
                                'programador', 'java', 'python', 'sql', 'api', 'web', 
                                'frontend', 'backend', 'full stack', 'scrum', 'agile']
            
            for palabra in palabras_generales:
                if palabra in texto:
                    keywords_encontradas.append(palabra)
        
        if not keywords_encontradas:
            print(">>> ⚠️  No se detectaron keywords específicas - usando tipo por defecto")
        
        return list(set(keywords_encontradas))  # Eliminar duplicados
    
    def validar_estrategia_aplicacion(self, tipo_posicion, nivel):
        """Valida si la posición está dentro de la estrategia de aplicación"""
        
        estrategia = self.config['estrategia_aplicacion']
        
        if nivel not in estrategia:
            return False
            
        tipos_permitidos = estrategia[nivel]
        return tipo_posicion in tipos_permitidos
    
    def tiene_experiencia_frontend(self):
        """Verifica si tenemos experiencia suficiente en frontend para aplicar"""
        # Basado en tu experiencia: Vue.js, Angular, Next.js, Quasar
        return True  # Tienes experiencia real en frontend
    
    def generar_experiencias_tecnicas_especificas(self, keywords, tipo_posicion):
        """Genera experiencias técnicas específicas basadas en keywords encontradas"""
        experiencias = []
        
        # Git Flow y Code Review (muy demandado)
        if any(kw in keywords for kw in ['git', 'github', 'gitlab']) or 'desarrollador' in tipo_posicion:
            experiencias.append("Gestión de código con Git, incluyendo branching strategies y code review en proyectos colaborativos")
        
        # Deploy y CI/CD
        if any(kw in keywords for kw in ['deploy', 'ci/cd', 'jenkins', 'docker']):
            experiencias.append("Participación en procesos de deployment y gestión de ramas en entornos de desarrollo")
        
        # Java específico (para posiciones junior)
        if 'java' in keywords and tipo_posicion == 'desarrollador_java':
            experiencias.append("Base sólida en desarrollo backend transferible a Java/Spring Boot")
            experiencias.append("Experiencia en APIs REST aplicable al ecosistema Java")
        
        # Bases de datos específicas
        if any(kw in keywords for kw in ['postgresql', 'mysql', 'sql']):
            experiencias.append("Optimización de consultas SQL y diseño de esquemas de base de datos")
        
        # Metodologías específicas mencionadas
        if any(kw in keywords for kw in ['scrum', 'kanban', 'agile']):
            experiencias.append("Participación activa en ceremonias ágiles y trabajo colaborativo en equipos multidisciplinarios")
        
        # APIs y microservicios
        if any(kw in keywords for kw in ['api', 'rest', 'microservicios']):
            experiencias.append("Diseño e implementación de APIs REST siguiendo mejores prácticas de arquitectura")
        
        return experiencias
    
    def generar_analisis_fit(self, keywords_postulacion, tipo_posicion, nivel, empresa):
        """Genera análisis automático de fit entre CV y postulación"""
        
        # Keywords que tenemos en nuestro CV (basado en tu experiencia real)
        nuestras_fortalezas = ['python', 'fastapi', 'postgresql', 'vue', 'quasar', 'next.js', 
                              'locust', 'postman', 'qa', 'manual', 'testing', 'scrum', 'kanban', 'git',
                              'javascript', 'sql', 'api', 'rest', 'agile', 'full stack', 'desarrollador', 
                              'angular', 'webservices', 'selenium', 'automatización', 'automation',
                              'frontend', 'backend', 'casos de prueba', 'validaciones', 'metodologías']
        
        coincidencias = []
        brechas = []
        
        # Analizar coincidencias
        for kw in keywords_postulacion:
            if kw in nuestras_fortalezas:
                coincidencias.append(kw)
        
        # Detectar brechas específicas
        if 'java' in keywords_postulacion and tipo_posicion == 'desarrollador_java':
            if nivel == 'senior':
                brechas.append("Java Senior requiere más experiencia - experiencia principal en Python")
            elif nivel == 'semi_senior':
                # Para SSR, solo mencionar como área de crecimiento, no como brecha bloqueante
                if len(coincidencias) < 3:
                    brechas.append("Java SSR - aprovechar experiencia backend transferible desde Python")
        
        if any(kw in keywords_postulacion for kw in ['code review', 'git flow', 'deploy']):
            if not any(kw in nuestras_fortalezas for kw in ['git', 'github']):
                brechas.append("Falta experiencia explícita en Git Flow/Code Review")
        
        if nivel == 'senior' and len(coincidencias) < 3:
            brechas.append("Puede requerir más experiencia para nivel Senior")
        
        # Calcular porcentaje de fit mejorado
        if not keywords_postulacion:
            # Si no hay keywords detectadas, usar heurística basada en tipo de posición
            fit_percentage = 60  # Base mínima
            if tipo_posicion in ['qa_manual', 'qa_automatizacion']:
                fit_percentage = 75  # Tenemos experiencia sólida en QA
            elif tipo_posicion == 'desarrollador_python':
                fit_percentage = 85  # Nuestra fortaleza principal
        else:
            total_keywords = len(keywords_postulacion)
            coincidencias_count = len(coincidencias)
            
            # Para QA, usar lógica especial porque es nuestra fortaleza
            if tipo_posicion in ['qa_manual', 'qa_automatizacion']:
                # Base alta para QA porque es nuestra experiencia
                base_percentage = 65
                
                # Bonificaciones específicas para QA
                if any(kw in coincidencias for kw in ['qa', 'testing', 'automatización', 'selenium']):
                    base_percentage += 15
                if any(kw in coincidencias for kw in ['sql', 'api', 'rest']):
                    base_percentage += 10
                if any(kw in coincidencias for kw in ['git', 'scrum', 'agile']):
                    base_percentage += 5
                    
                # Si tiene Java pero es QA, no penalizar tanto
                if 'java' in keywords_postulacion and tipo_posicion == 'qa_automatizacion':
                    base_percentage += 5  # Bonus menor porque podemos aprender Java para QA
                    
            else:
                # Para desarrollo, usar cálculo mejorado
                base_percentage = (coincidencias_count / total_keywords * 100) if total_keywords > 0 else 0
                
                if tipo_posicion == 'desarrollador_python' and any(kw in keywords_postulacion for kw in ['python', 'fastapi']):
                    base_percentage += 15  # Nuestra tecnología principal
                elif tipo_posicion == 'desarrollador_java':
                    # Para Java, dar base más alta porque tenemos experiencia backend transferible
                    base_percentage = max(base_percentage, 50)  # Base mínima para Java
                    
                    # Bonificaciones para Java
                    if any(kw in coincidencias for kw in ['sql', 'base de datos']):
                        base_percentage += 10  # Tenemos experiencia SQL
                    if any(kw in coincidencias for kw in ['api', 'rest']):
                        base_percentage += 10  # Experiencia en APIs
                    if any(kw in coincidencias for kw in ['scrum', 'ágiles', 'agile']):
                        base_percentage += 5   # Metodologías ágiles
                    if 'java' in keywords_postulacion:
                        base_percentage += 5   # Bonus por mencionar Java específicamente
            
            fit_percentage = min(100, base_percentage)  # Cap a 100%
        
        return {
            'fit_percentage': round(fit_percentage),
            'coincidencias': coincidencias,
            'brechas': brechas,
            'recomendaciones': self.generar_recomendaciones(tipo_posicion, nivel, brechas)
        }
    
    def generar_recomendaciones(self, tipo_posicion, nivel, brechas):
        """Genera recomendaciones específicas para mejorar el fit"""
        recomendaciones = []
        
        if tipo_posicion == 'desarrollador_java':
            recomendaciones.append("Destacar experiencia transferible desde Python hacia Java/Spring")
            recomendaciones.append("Mencionar cursos o proyectos personales en Java si los hay")
        
        if 'Git Flow' in str(brechas):
            recomendaciones.append("Agregar experiencia en Git Flow y code review al CV")
        
        if nivel == 'junior':
            recomendaciones.append("Enfatizar disposición a aprender y adaptabilidad")
        elif nivel == 'senior':
            recomendaciones.append("Destacar liderazgo técnico y mentoría a otros desarrolladores")
        
        return recomendaciones

    def adaptar_cv(self, cv_base, tipo_posicion, nivel, keywords_encontradas, empresa):
        """Adapta el CV según el tipo de posición y nivel detectado"""
        adaptacion = self.adaptaciones_cv.get(tipo_posicion, self.adaptaciones_cv['qa_manual'])
        
        # 1. Modificar título principal según el nivel
        titulo_adaptado = adaptacion['titulo']
        if tipo_posicion == 'desarrollador_java':
            if nivel == 'junior':
                titulo_adaptado = 'Java Junior Developer & QA Engineer'
            elif nivel == 'semi_senior':
                titulo_adaptado = 'Java SSR Developer & QA Engineer'
            elif nivel == 'senior':
                titulo_adaptado = 'Java Senior Developer & QA Engineer'
        
        cv_adaptado = cv_base.replace('QA Engineer', titulo_adaptado)
        
        # 2. Mejorar el perfil profesional integrando la especialización
        perfil_original = "QA Engineer y Full Stack Developer con experiencia en validación de datos, pruebas de sistemas y desarrollo de aplicaciones en entornos ágiles y arquitecturas de microservicios."
        
        perfil_mejorado = f"{adaptacion['titulo']} con experiencia en validación de datos, pruebas de sistemas y desarrollo de aplicaciones en entornos ágiles y arquitecturas de microservicios. {adaptacion['resumen_adicional']}"
        
        cv_adaptado = cv_adaptado.replace(perfil_original, perfil_mejorado)
        
        # 3. Agregar experiencias relevantes en la sección de logros
        logros_adicionales = "\n\nExperiencias Técnicas Destacadas:\n"
        for exp in adaptacion['experiencias_extra']:
            logros_adicionales += f"• {exp}\n"
        
        # Agregar experiencias técnicas específicas según keywords
        logros_tecnicos = self.generar_experiencias_tecnicas_especificas(keywords_encontradas, tipo_posicion)
        for exp_tec in logros_tecnicos:
            logros_adicionales += f"• {exp_tec}\n"
        
        # Ajustar según nivel de seniority
        if nivel == 'junior':
            logros_adicionales += "• Enfoque en aprendizaje continuo y adaptación a nuevas tecnologías\n"
        elif nivel == 'senior':
            logros_adicionales += "• Mentoría a desarrolladores junior y liderazgo técnico en proyectos\n"
        
        # Insertar después de "Logros Relevantes"
        cv_adaptado = cv_adaptado.replace(
            "Desarrollo de funcionalidades completas en plataformas de compras municipales con stack completo Python/JavaScript.",
            f"Desarrollo de funcionalidades completas en plataformas de compras municipales con stack completo Python/JavaScript.{logros_adicionales}"
        )
        
        # 4. Agregar keywords relevantes sutilmente
        keywords_faltantes = []
        for kw in keywords_encontradas:
            if kw not in cv_adaptado.lower() and kw in ['selenium', 'java', 'spring boot', 'automatización', 'katalon', 'uft']:
                keywords_faltantes.append(kw)
        
        if keywords_faltantes:
            tech_adicional = f"\n\nTecnologías y herramientas relevantes que fui adquiriendo: {', '.join(keywords_faltantes).title()}"
            cv_adaptado += tech_adicional
        
        return cv_adaptado, adaptacion['titulo']

    def generar_cv_pdf(self, texto_cv, nombre_archivo):
        """Genera el CV en formato PDF con mejor formato"""
        try:
            from reportlab.lib.styles import ParagraphStyle
            from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
            from reportlab.lib import colors
            
            doc = SimpleDocTemplate(nombre_archivo, pagesize=A4, 
                                  leftMargin=50, rightMargin=50, 
                                  topMargin=50, bottomMargin=50)
            styles = getSampleStyleSheet()
            
            # Estilos personalizados
            titulo_style = ParagraphStyle(
                'TituloPersonal',
                parent=styles['Heading1'],
                fontSize=16,
                spaceAfter=6,
                alignment=TA_CENTER,
                textColor=colors.darkblue
            )
            
            subtitulo_style = ParagraphStyle(
                'SubtituloPersonal', 
                parent=styles['Heading2'],
                fontSize=12,
                spaceAfter=8,
                textColor=colors.darkblue,
                borderWidth=1,
                borderColor=colors.lightgrey,
                borderPadding=3
            )
            
            contenido = []
            lineas = texto_cv.split('\n')
            
            for i, linea in enumerate(lineas):
                linea = linea.strip()
                if not linea:
                    contenido.append(Spacer(1, 6))
                    continue
                
                # Nombre (primera línea)
                if i == 0:
                    contenido.append(Paragraph(linea, titulo_style))
                    contenido.append(Spacer(1, 12))
                
                # Títulos de sección
                elif linea in ['Perfil Profesional', 'Logros Relevantes', 'Experiencia Profesional', 
                              'Tecnologías y Herramientas', 'Educación', 'Experiencias Técnicas Destacadas']:
                    contenido.append(Spacer(1, 12))
                    contenido.append(Paragraph(linea, subtitulo_style))
                    contenido.append(Spacer(1, 6))
                
                # Subtítulo de trabajo/empresa
                elif any(empresa in linea for empresa in ['Municipalidad', 'FABRICARG', 'CECAL', 'Proyecto Freelance']):
                    contenido.append(Spacer(1, 8))
                    contenido.append(Paragraph(f"<b>{linea}</b>", styles["Normal"]))
                    contenido.append(Spacer(1, 4))
                
                # Contenido normal
                else:
                    contenido.append(Paragraph(linea, styles["Normal"]))
                    contenido.append(Spacer(1, 4))
            
            doc.build(contenido)
            return True
        except Exception as e:
            print(f"Error generando PDF: {e}")
            return False

    def generar_speech_avanzado(self, empresa, tipo_posicion, nivel, keywords):
        """Genera un speech personalizado según el tipo de posición y nivel"""
        
        # Definir speech para Java según el nivel
        if tipo_posicion == 'desarrollador_java':
            if nivel == 'junior':
                speech_java = f"Gracias por la oportunidad en {empresa}. Me interesa esta posición junior porque mi experiencia sólida en Python/FastAPI y metodologías de testing me proporciona una excelente base para transicionar al ecosistema Java. Estoy motivado por aprender y aplicar mis conocimientos de backend en Java."
            else:  # semi_senior
                speech_java = f"Gracias por la oportunidad en {empresa}. Me motiva esta posición SSR porque mi experiencia en desarrollo backend con Python/FastAPI, combined con mi background en QA, me permite aportar una perspectiva integral al desarrollo Java. Mi experiencia en APIs REST y metodologías ágiles es directamente transferible al ecosistema Java/Spring."
        else:
            # Para casos que no sean Java, definir speech_java por defecto
            speech_java = f"Gracias por la oportunidad en {empresa}. Mi experiencia en desarrollo backend me proporciona una base sólida para trabajar con Java."
        
        speeches_base = {
            'qa_automatizacion': f"Gracias por la oportunidad en {empresa}. Me postulé porque tengo una experiencia única combinando desarrollo full stack y QA. Actualmente en la Municipalidad desarrollo funcionalidades con Python/FastAPI y Next.js, y también implemento automatización de pruebas con Locust y Selenium.",
            
            'qa_manual': f"Gracias por la oportunidad en {empresa}. Me entusiasma esta posición porque mi experiencia combina QA manual con desarrollo. En mis proyectos actuales desarrollo las funcionalidades y luego las testeo, lo que me da una perspectiva única para detectar problemas desde el diseño.",
            
            'desarrollador_python': f"Gracias por la oportunidad en {empresa}. Me motiva esta posición porque tengo experiencia sólida desarrollando con Python/FastAPI, PostgreSQL y frontend con Vue.js en proyectos municipales. Mi background en QA me permite desarrollar código más robusto desde el inicio.",
            
            'desarrollador_java': speech_java
        }
        
        speech_base = speeches_base.get(tipo_posicion, speeches_base['qa_manual'])
        
        speech_base += " Estoy entusiasmado por aportar valor al equipo y seguir creciendo profesionalmente en este rol."
        
        return speech_base

    def guardar_postulacion(self, texto_postulacion, empresa, tipo_posicion):
        """Guarda la postulación con metadatos"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"postulacion_{empresa}_{tipo_posicion}_{timestamp}.txt"
        path_completo = os.path.join(self.carpeta_salida, nombre_archivo)
        
        contenido = f"""EMPRESA: {empresa}
TIPO POSICIÓN: {tipo_posicion}
FECHA: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
=====================================

{texto_postulacion}
"""
        
        with open(path_completo, "w", encoding="utf-8") as f:
            f.write(contenido)
        
        return path_completo

    def procesar_postulacion(self, texto_postulacion, empresa):
        """Proceso principal: analiza postulación y genera CV personalizado"""
        print(f"\n>>> Analizando postulación de {empresa}...")
        
        # 1. Detectar tipo de posición y nivel
        tipo_posicion, nivel = self.detectar_tipo_posicion(texto_postulacion)
        
        # Si no detectó una posición válida, terminar aquí
        if tipo_posicion is None:
            return None
            
        print(f">>> Tipo detectado: {tipo_posicion} ({nivel})")
        
        # 2. Extraer keywords
        keywords = self.extraer_keywords_avanzado(texto_postulacion)
        print(f">>> Keywords encontradas: {', '.join(keywords[:5])}{'...' if len(keywords) > 5 else ''}")
        
        # 2.5. Detectar salario
        try:
            info_salario = self.detectar_salario(texto_postulacion)
            if info_salario['salario_detectado']:
                print(f">>> Salario detectado: {info_salario['rango_min']} {info_salario['moneda']}")
                for alerta in info_salario['alertas']:
                    print(f">>> {alerta}")
            else:
                print(">>> No se detectó información salarial")
        except Exception as e:
            logging.warning(f"Error detectando salario: {e}")
        
        # 3. Cargar y adaptar CV
        cv_base = self.cargar_cv_base()
        if not cv_base:
            print(">>> Error: No se pudo cargar el CV base")
            return None
            
        # 4. Generar análisis de fit ANTES de crear archivos
        analisis_fit = self.generar_analisis_fit(keywords, tipo_posicion, nivel, empresa)
        print(f">>> Análisis de Fit: {analisis_fit['fit_percentage']}%")
        
        # 5. Validar estrategia de aplicación según nivel
        if not self.validar_estrategia_aplicacion(tipo_posicion, nivel):
            print(f"\n🚫 POSICIÓN FUERA DE ESTRATEGIA")
            print(f">>> Tipo detectado: {tipo_posicion} ({nivel})")
            print(">>> Estrategia actual:")
            print("   • Junior: QA, Python, Java, Frontend, Full Stack")
            print("   • Semi-Senior: QA, Python, Java, Full Stack")
            print("   • Rechazados automáticos: Senior y áreas sin experiencia")
            print(">>> No se generará CV para esta postulación")
            return None
        
        # 6. Validar umbral mínimo
        if analisis_fit['fit_percentage'] < self.umbral_fit:
            print(f"\n>>> FIT INSUFICIENTE ({analisis_fit['fit_percentage']}%)")
            print(f">>> Mínimo requerido: {self.umbral_fit}%")
            print(">>> No se generará CV para esta postulación")
            
            if analisis_fit['brechas']:
                print(f">>> Principales brechas: {', '.join(analisis_fit['brechas'])}")
            
            if analisis_fit['recomendaciones']:
                print("\n💡 Recomendaciones para mejorar fit:")
                for rec in analisis_fit['recomendaciones']:
                    print(f"   • {rec}")
            
            return None
        
        print(f"✅ FIT APROPIADO ({analisis_fit['fit_percentage']}%) - Generando CV...")
        
        # 6. Adaptar CV (solo si fit >= 70%)
        cv_adaptado, titulo_adaptado = self.adaptar_cv(cv_base, tipo_posicion, nivel, keywords, empresa)
        
        # 7. Generar archivos
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        nombre_pdf = os.path.join(self.carpeta_salida, f"cv_{empresa.lower().replace(' ', '_')}_{tipo_posicion}_{timestamp}.pdf")
        
        if self.generar_cv_pdf(cv_adaptado, nombre_pdf):
            print(f">>> CV generado: {nombre_pdf}")
        else:
            print(">>> Error generando PDF")
            return None
        
        # 8. Guardar postulación
        path_postulacion = self.guardar_postulacion(texto_postulacion, empresa, tipo_posicion)
        print(f">>> Postulación guardada: {path_postulacion}")
        
        # 9. Generar speech
        speech = self.generar_speech_avanzado(empresa, tipo_posicion, nivel, keywords)
        print(f"\n>>> Speech para entrevista:")
        print(f"'{speech}'\n")
        
        # Mostrar áreas de mejora si las hay
        if analisis_fit['brechas']:
            print(f">>> Áreas a considerar en entrevista: {', '.join(analisis_fit['brechas'])}")
        
        # 10. Guardar resumen completo
        self.guardar_resumen(empresa, tipo_posicion, nivel, titulo_adaptado, keywords, speech, 
                           analisis_fit, nombre_pdf, path_postulacion)
        
        return {
            'empresa': empresa,
            'tipo_posicion': tipo_posicion,
            'titulo': titulo_adaptado,
            'keywords': keywords,
            'cv_path': nombre_pdf,
            'postulacion_path': path_postulacion,
            'speech': speech
        }

    def guardar_resumen(self, empresa, tipo_posicion, nivel, titulo, keywords, speech, analisis_fit, cv_path, postulacion_path):
        """Guarda un resumen completo de la postulación procesada"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        resumen_path = os.path.join(self.carpeta_salida, f"resumen_{empresa.lower().replace(' ', '_')}_{timestamp}.json")
        
        resumen = {
            'empresa': empresa,
            'fecha_procesamiento': datetime.now().isoformat(),
            'tipo_posicion': tipo_posicion,
            'nivel_seniority': nivel,
            'titulo_cv': titulo,
            'keywords_detectadas': keywords,
            'speech_entrevista': speech,
            'analisis_fit': analisis_fit,
            'archivos_generados': {
                'cv_pdf': cv_path,
                'postulacion': postulacion_path
            }
        }
        
        with open(resumen_path, 'w', encoding='utf-8') as f:
            json.dump(resumen, f, ensure_ascii=False, indent=2)

# FUNCIÓN PRINCIPAL
def main():
    try:
        generador = GeneradorCVInteligente()  # Usa config.json por defecto
        logging.info("🚀 Generador de CV iniciado correctamente")
    except (ConfigurationError, FileProcessingError) as e:
        print(f"❌ Error de inicialización: {e}")
        return
    except Exception as e:
        logging.error(f"Error inesperado: {e}")
        print(f"❌ Error inesperado: {e}")
        return
    
    print(">>> Generador de CV Inteligente v2.0")
    print("🎯 Estrategia de aplicación:")
    print("   • Junior: QA, Python, Java, Frontend, Full Stack")
    print("   • Semi-Senior: QA, Python, Java, Full Stack")
    print(f"   • Umbral mínimo de fit: {generador.umbral_fit}%")
    print("   • Rechazo automático: Áreas sin experiencia\n")
    
    while True:
        print("\n" + "="*50)
        empresa = input(">>> Nombre de la empresa (o 'salir' para terminar): ").strip()
        
        if empresa.lower() == 'salir':
            break
            
        texto_postulacion = input("\n>>> Pega la descripción de la postulación:\n").strip()
        
        if empresa and texto_postulacion:
            try:
                resultado = generador.procesar_postulacion(texto_postulacion, empresa)
                
                if resultado:
                    print(f"\n>>> ¡Proceso completado para {empresa}!")
                    print(f">>> Posición: {resultado['titulo']}")
                    print(f">>> CV guardado en: {resultado['cv_path']}")
                else:
                    print("\n>>> Postulación no procesada (fuera de estrategia o fit insuficiente)")
            except Exception as e:
                logging.error(f"Error procesando postulación de {empresa}: {e}")
                print(f"\n>>> ❌ Error procesando la postulación: {e}")
        else:
            print("\n>>> Empresa y postulación son requeridos")

if __name__ == "__main__":
    main()
