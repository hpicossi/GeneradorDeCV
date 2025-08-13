# 🚀 Generador de CV Inteligente

[![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

Un sistema automatizado e inteligente para generar CVs personalizados basados en análisis de postulaciones laborales. Analiza automáticamente las descripciones de trabajo, detecta el tipo de posición y nivel de seniority, y adapta tu CV para maximizar las posibilidades de éxito.

> 🎯 **Automatiza tu búsqueda laboral con IA y maximiza tus oportunidades**

## 📑 Tabla de Contenidos

- [🚀 Generador de CV Inteligente](#-generador-de-cv-inteligente)
  - [📋 ¿Qué hace este script?](#-qué-hace-este-script)
  - [🌟 Características Principales](#-características-principales)
  - [🛠️ Requisitos del Sistema](#️-requisitos-del-sistema)
  - [📦 Instalación](#-instalación)
  - [⚙️ Configuración](#️-configuración)
  - [🚀 Uso](#-uso)
  - [📁 Estructura de Archivos](#-estructura-de-archivos)
  - [🎯 Estrategia de Aplicación](#-estrategia-de-aplicación)
  - [📧 Configuración de Email](#-configuración-de-email)
  - [🎨 Personalización](#-personalización)
  - [📈 Métricas y Estadísticas](#-métricas-y-estadísticas)
  - [🛠️ Stack Tecnológico](#️-stack-tecnológico)
  - [🔧 Troubleshooting](#-troubleshooting)
  - [🤝 Contribuciones](#-contribuciones)
  - [📜 Licencia](#-licencia)

## 📋 ¿Qué hace este script?

El **Generador de CV Inteligente** es una herramienta que:

- 🎯 **Analiza postulaciones** automáticamente y detecta tipo de posición (QA, Python, Java, Frontend, etc.)
- 📊 **Calcula porcentaje de fit** entre tu perfil y los requisitos del puesto
- ✨ **Adapta tu CV** automáticamente según el tipo de posición detectada
- 💰 **Detecta salarios** en las postulaciones y evalúa competitividad
- 📝 **Genera speech personalizado** para entrevistas
- 📈 **Filtra oportunidades** según tu estrategia de aplicación
- 🗂️ **Organiza todo** en archivos PDF y resúmenes JSON
- 🕷️ **Busca trabajos automáticamente** en múltiples portales web
- 🌐 **Scrapea Computrabajo, ZoneJobs, Indeed** con filtros inteligentes

## 🌟 Características Principales

### ✅ **Detección Inteligente**
- Identifica automáticamente QA, Python, Java, Backend, Full Stack
- Detecta nivel de seniority (Junior, Semi-Senior, Senior)
- Rechaza automáticamente posiciones fuera de tu perfil

### ✅ **Web Scraping Automático**
- Busca trabajos en Computrabajo, ZoneJobs, Indeed automáticamente
- 5 áreas predefinidas: QA, Python, Java, Backend, Full Stack
- Filtros anti-spam y validación de calidad
- Delays configurables para scraping ético

### ✅ **Análisis de Fit Avanzado**
- Calcula porcentaje de compatibilidad con la postulación
- Identifica keywords relevantes de tu experiencia
- Umbral mínimo configurable (por defecto 70%)

### ✅ **Adaptación Automática del CV**
- Cambia título profesional según el puesto
- Añade experiencias técnicas relevantes
- Destaca tecnologías específicas mencionadas en la postulación

### ✅ **Detección de Salarios**
- Identifica rangos salariales en USD y ARS
- Evalúa competitividad según tus expectativas
- Alertas automáticas por salarios bajos/altos

### ✅ **Sistema de Logging**
- Registro detallado de todas las operaciones
- Archivo de log para debugging (`cv_generator.log`)
- Manejo robusto de errores

## 🛠️ Requisitos del Sistema

### **Python 3.7+**
### **Librerías necesarias:**
```bash
pip install python-docx reportlab python-dotenv requests beautifulsoup4
```

### **Archivos requeridos:**
- `cv_hilario.docx` - Tu CV base en formato Word
- `config.json` - Archivo de configuración (se crea automáticamente)

## 📦 Instalación

### 1. **Clonar o descargar el proyecto**
```bash
git clone https://github.com/tu-usuario/GeneradorDeCV.git
cd GeneradorDeCV
```

### 2. **Instalar dependencias**
```bash
pip install python-docx reportlab python-dotenv requests beautifulsoup4
```

### 3. **Configurar variables de entorno (IMPORTANTE)**
```bash
# Copiar archivo de ejemplo
cp .env.example .env

# Editar .env con tus datos reales
# Configurar EMAIL_ADDRESS, EMAIL_PASSWORD, etc.
```

### 4. **Verificar archivos necesarios**
Asegúrate de tener:
- ✅ `generador_cv_avanzado.py`
- ✅ `config.json`
- ✅ `cv_hilario.docx` (tu CV base)

## ⚙️ Configuración

### **config.json**
El archivo `config.json` contiene toda la configuración del sistema:

```json
{
  "configuracion_general": {
    "umbral_fit": 70,
    "cv_base_path": "cv_hilario.docx",
    "carpeta_salida": "cv_generados"
  },
  "perfil_tecnico": {
    "qa_manual": ["testing", "qa", "manual", "casos de prueba"],
    "qa_automatizacion": ["selenium", "automation", "locust"],
    "backend_python": ["python", "fastapi", "flask", "django"],
    // ... más configuraciones
  },
  "deteccion_salarios": {
    "salario_minimo_esperado_usd": 800,
    "salario_maximo_esperado_usd": 2500
  }
}
```

### **Parámetros principales:**
- `umbral_fit`: Porcentaje mínimo para generar CV (recomendado: 70%)
- `cv_base_path`: Ruta a tu CV base en Word
- `salario_minimo_esperado_usd`: Tu expectativa salarial mínima

## 🚀 Uso

### **Ejecutar el script:**
```bash
python generador_cv_avanzado.py
```

### **Flujo de uso:**
1. **Ejecuta el script**
2. **Ingresa el nombre de la empresa**
3. **Pega la descripción de la postulación**
4. **El sistema analiza automáticamente:**
   - Tipo de posición y nivel
   - Keywords relevantes
   - Información salarial
   - Porcentaje de fit
5. **Si el fit es ≥70%, genera:**
   - CV personalizado en PDF
   - Speech para entrevista
   - Resumen completo en JSON

### **Ejemplo de uso:**
```
>>> Nombre de la empresa: TechCorp
>>> Pega la descripción de la postulación:
Buscamos QA Automation Engineer SSR con experiencia en Selenium...

>>> Analizando postulación de TechCorp...
>>> Detección: qa_automatizacion (puntos: 4)
>>> Tipo detectado: qa_automatizacion (semi_senior)
>>> Keywords encontradas: selenium, automation, qa, testing...
>>> Salario detectado: 1500 USD
>>> ✅ Salario competitivo: $1500 USD
>>> Análisis de Fit: 85%
✅ FIT APROPIADO (85%) - Generando CV...
>>> CV generado: cv_generados/cv_techcorp_qa_automatizacion_20250812_1030.pdf
```

## 📁 Estructura de Archivos

```
scriptCV/
├── generador_cv_avanzado.py    # Script principal
├── config.json                 # Configuración del sistema
├── cv_hilario.docx             # Tu CV base (Word)
├── cv_generator.log            # Archivo de logs
├── cv_generados/               # Carpeta de salida
│   ├── cv_empresa_tipo_fecha.pdf
│   ├── postulacion_empresa_tipo_fecha.txt
│   └── resumen_empresa_fecha.json
└── README.md                   # Este archivo
```

### **Archivos generados:**
- **CV PDF**: CV adaptado para la posición específica
- **Postulación TXT**: Descripción original guardada
- **Resumen JSON**: Análisis completo con metadata

## 🎯 Estrategia de Aplicación

El sistema sigue una estrategia definida:

### **Junior** ✅
- QA Manual y Automatización
- Python, Java, Backend, Full Stack

### **Semi-Senior** ✅
- QA Manual y Automatización  
- Python, Java, Full Stack

### **Senior** ❌
- No aplica automáticamente (requiere experiencia adicional)

### **Fuera de perfil** ❌
- Tecnologías no conocidas (.NET, PHP, Ruby, etc.)
- Áreas sin experiencia (DevOps puro, Mobile, etc.)

## 🔧 Troubleshooting

### **Error: "CV base no encontrado"**
```bash
❌ Error: CV base no encontrado: cv_hilario.docx
```
**Solución:** Asegúrate de que `cv_hilario.docx` existe en la carpeta del script.

### **Error: "Archivo de configuración no encontrado"**
```bash
❌ Error: Archivo de configuración no encontrado: config.json
```
**Solución:** El archivo `config.json` debe estar en la misma carpeta que el script.

### **Error: "ModuleNotFoundError"**
```bash
ModuleNotFoundError: No module named 'docx'
```
**Solución:** Instala las dependencias:
```bash
pip install python-docx reportlab
```

### **Error: "Fit insuficiente"**
```bash
>>> FIT INSUFICIENTE (45%) - Mínimo requerido: 70%
```
**Solución:** Esto es normal. El sistema está filtrando posiciones que no coinciden con tu perfil.

## 📊 Logs y Debugging

El sistema genera un archivo `cv_generator.log` con información detallada:

```
2025-01-08 10:30:15 - INFO - ✅ Configuración cargada desde config.json
2025-01-08 10:30:15 - INFO - ✅ CV base validado: cv_hilario.docx
2025-01-08 10:30:15 - INFO - 🚀 Generador de CV iniciado correctamente
```

## 🎨 Personalización

### **Agregar nuevas tecnologías:**
Edita `config.json` en la sección `perfil_tecnico`:
```json
"backend_python": ["python", "fastapi", "flask", "nueva_tecnologia"]
```

### **Cambiar umbral de fit:**
```json
"configuracion_general": {
  "umbral_fit": 75  // Más estricto
}
```

### **Ajustar expectativas salariales:**
```json
"deteccion_salarios": {
  "salario_minimo_esperado_usd": 1000,
  "salario_maximo_esperado_usd": 3000
}
```

## 📧 Configuración de Email

### **1. Configurar archivo .env:**
```bash
# Editar .env con tus datos reales
EMAIL_ENABLED=true
EMAIL_ADDRESS=tu_email@gmail.com
EMAIL_PASSWORD=tu_app_password_16_caracteres
EMAIL_NOMBRE_COMPLETO=Tu Nombre Completo
EMAIL_TELEFONO=+54 9 11 1234-5678
```

### **2. Para Gmail - Generar App Password:**
1. Ir a [Google Account Settings](https://myaccount.google.com/security)
2. Habilitar verificación en 2 pasos
3. Generar "App Password" para la aplicación
4. Usar ese password de 16 caracteres en `EMAIL_PASSWORD`

### **3. Seguridad:**
- ✅ El archivo `.env` está en `.gitignore` (no se sube al repositorio)
- ✅ Nunca hardcodees credenciales en el código
- ✅ Usa App Passwords, no tu contraseña personal

### **4. Uso con emails:**
```bash
# Habilitar emails en modo interactivo
python generador_cv_avanzado.py --email

# Modo batch con emails automáticos
python generador_cv_avanzado.py --batch postulaciones.csv --email
```

## 🕷️ Web Scraping Automático

### **Buscar trabajos automáticamente:**
```bash
# Buscar trabajos QA en Buenos Aires
python generador_cv_avanzado.py --scrape qa --save-jobs

# Buscar Python en Córdoba
python generador_cv_avanzado.py --scrape python --location "Córdoba"

# Buscar Java y procesar automáticamente
python generador_cv_avanzado.py --scrape java --save-jobs
```

### **Portales soportados:**
- 🇦🇷 **Computrabajo** - Portal líder en Latinoamérica
- 🇦🇷 **ZoneJobs** - Popular en Argentina
- 🌎 **Indeed** - Portal global

### **Áreas de búsqueda disponibles:**
- `qa` - QA Engineer, Tester, Quality Assurance, Automation, Selenium
- `python` - Python Developer, Backend Python, Django, FastAPI, Flask
- `java` - Java Developer, Spring Boot, Java Programmer, Spring, Hibernate
- `backend` - Backend Developer, API Developer, Microservicios, REST API, Node.js
- `fullstack` - Full Stack Developer, Fullstack, Desarrollador Full Stack, Full-Stack

### **Flujo completo automatizado:**
```bash
# 1. Buscar trabajos automáticamente
python generador_cv_avanzado.py --scrape qa --save-jobs

# 2. El sistema encuentra trabajos y pregunta si procesar
# 3. Si aceptas, procesa todos automáticamente
# 4. Genera CVs personalizados para cada uno
# 5. Envía emails si está configurado
```

## 📈 Métricas y Estadísticas

Cada postulación procesada genera:
- ✅ **Tasa de éxito** por tipo de posición
- 📊 **Keywords más exitosas**
- 💰 **Rangos salariales detectados**
- 🎯 **Fit promedio** por empresa

## 🛠️ Stack Tecnológico

- **Python 3.7+** - Lenguaje principal
- **python-docx** - Manipulación de documentos Word
- **ReportLab** - Generación de PDFs
- **SQLite** - Base de datos local
- **SMTP** - Envío de emails
- **python-dotenv** - Manejo de variables de entorno
- **requests** - HTTP client para web scraping
- **BeautifulSoup4** - Parser HTML para extraer datos
- **argparse** - Interfaz CLI avanzada

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si quieres mejorar el proyecto:

### **Cómo contribuir:**

1. **Fork** el repositorio
2. **Crea** una rama para tu feature: `git checkout -b feature/nueva-funcionalidad`
3. **Commit** tus cambios: `git commit -m 'Add: nueva funcionalidad'`
4. **Push** a la rama: `git push origin feature/nueva-funcionalidad`
5. **Abre** un Pull Request

### **Tipos de contribuciones bienvenidas:**

- 🐛 **Bug fixes**
- ✨ **Nuevas funcionalidades**
- 📚 **Documentación**
- 🎨 **Mejoras de UI/UX**
- 🧪 **Tests automatizados**
- 🌐 **Traducciones**

### **Próximas mejoras en roadmap:**

- [x] **Web scraping automático** ✅ COMPLETADO v3.1.0
- [ ] Dashboard web con Flask/FastAPI
- [ ] Machine Learning para optimización de fit
- [ ] Sistema de follow-up automático
- [ ] Análisis de competencia avanzado
- [ ] Plantillas de CV múltiples
- [ ] Notificaciones push/Slack
- [ ] Tests automatizados
- [ ] Integración con LinkedIn API
- [ ] Scraping de más portales (Bumeran, Empleos Clarin)

## 📊 Estadísticas del Proyecto

- 📈 **+3000 líneas de código**
- 🚀 **12+ funcionalidades principales**
- 📧 **Integración de email automática**
- 📊 **Dashboard de estadísticas completo**
- 🎯 **Sistema de fit inteligente**
- 💾 **Base de datos SQLite integrada**

## 🐛 Reporte de Issues

¿Encontraste un bug? ¡Ayúdanos a mejorarlo!

1. **Verifica** que no esté ya reportado en [Issues](../../issues)
2. **Crea** un nuevo issue con:
   - Descripción clara del problema
   - Pasos para reproducir
   - Mensaje de error completo
   - Tu configuración (OS, Python version)

## 📞 Soporte y Comunidad

### **Si tienes problemas:**

1. 📋 Revisa el archivo `cv_generator.log`
2. 🔍 Consulta la sección [Troubleshooting](#-troubleshooting)
3. 📖 Lee la documentación completa
4. 🐛 [Reporta issues](../../issues) en GitHub
5. 💬 Inicia una [Discusión](../../discussions) para preguntas generales

### **Canales de soporte:**

- 🐛 **Bugs**: [GitHub Issues](../../issues)
- 💡 **Feature Requests**: [GitHub Discussions](../../discussions)
- 📚 **Documentación**: Este README
- 📧 **Email**: Disponible en el perfil de GitHub

## 📜 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

```
MIT License

Copyright (c) 2025 GeneradorDeCV

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...
```

## ⭐ ¿Te gustó el proyecto?

¡Dale una **estrella** ⭐ al repositorio si te fue útil!

### **Ayuda a hacer crecer el proyecto:**

- ⭐ **Star** el repositorio
- 🍴 **Fork** para contribuir
- 📣 **Comparte** con otros desarrolladores
- 💬 **Feedback** en discusiones
- 🐛 **Reporta** bugs para mejorarlo

## 🙏 Agradecimientos

- 💡 Inspirado por la necesidad de automatizar aplicaciones laborales
- 🤝 Agradecimiento a la comunidad open source
- 📚 Construido con excelentes librerías de Python
- 🚀 Diseñado para desarrolladores que buscan empleo

---

<div align="center">

**¡Automatiza tu búsqueda laboral y maximiza tus oportunidades! 🚀**

[⬆ Volver al inicio](#-generador-de-cv-inteligente)

</div>
