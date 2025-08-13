# 📚 Ejemplos de Uso

Esta guía muestra ejemplos prácticos de cómo usar el **Generador de CV Inteligente** en diferentes escenarios.

## 🚀 Casos de Uso Comunes

### 1. **Primer Uso - Configuración Rápida**

```bash
# Instalar dependencias
pip install python-docx reportlab python-dotenv

# Configurar entorno
cp .env.example .env

# Primer test
python generador_cv_avanzado.py --help
```

### 2. **Aplicación Individual**

```bash
# Modo interactivo
python generador_cv_avanzado.py

>>> Nombre de la empresa: Google
>>> Descripción: "Python Developer SSR para equipo de Search..."
```

### 3. **Procesamiento Masivo**

```bash
# Procesar 50 postulaciones automáticamente
python generador_cv_avanzado.py --batch mi_lista_postulaciones.csv
```

## 📊 Ejemplos por Tipo de Posición

### **QA Automation Engineer**

**Input:**
```
Empresa: TestCorp
Descripción: "Buscamos QA Automation Engineer SSR con Selenium, Python, 
Jenkins CI/CD. Salario $1600 USD. Empresa multinacional de fintech."
```

**Output Esperado:**
```
>>> Tipo detectado: qa_automatizacion (semi_senior)
>>> 🏢 Empresa tipo: corporacion
>>> Análisis de Fit: 88%
>>> Salario: $1600 USD ✅ Competitivo
>>> CV adaptado: "QA Automation Engineer | Experiencia en Proyectos Escalables"
```

### **Python Developer**

**Input:**
```
Empresa: StartupAI  
Descripción: "Python Full Stack para startup. FastAPI, Vue.js, PostgreSQL.
Ambiente dinámico, $1200 USD, equity options."
```

**Output Esperado:**
```
>>> Tipo detectado: desarrollador_python (semi_senior)
>>> 🏢 Empresa tipo: startup  
>>> Análisis de Fit: 92%
>>> CV adaptado: "Python Full Stack Developer | Apasionado por la Innovación"
```

### **Java Developer**

**Input:**
```
Empresa: EnterpriseCorp
Descripción: "Java Developer Junior, Spring Boot, MySQL, microservicios.
Gran empresa consolidada, $1000 USD."
```

**Output Esperado:**
```
>>> Tipo detectado: desarrollador_java (junior)
>>> 🏢 Empresa tipo: corporacion
>>> Análisis de Fit: 75%
>>> CV adaptado: "Java Junior Developer | Experiencia en Proyectos Escalables"
```

## 💼 Ejemplos de Archivos CSV

### **Archivo Simple:**
```csv
empresa,descripcion
TechCorp,"QA SSR con Selenium y Java, $1500 USD"
StartupX,"Python Developer para producto SaaS, FastAPI"
ConsultoraY,"Full Stack para múltiples clientes, Vue + Python"
```

### **Archivo Avanzado:**
```csv
empresa,descripcion,contacto,prioridad
Google,"Senior Software Engineer, Python/Go, $3000 USD",hiring@google.com,alta
Meta,"QA Engineer, Automation, React Testing",jobs@meta.com,media  
Netflix,"Backend Developer, Java/Spring, Microservices",careers@netflix.com,alta
Spotify,"Full Stack, Python/React, Music Streaming",tech-jobs@spotify.com,media
```

## 📧 Ejemplos con Email Automático

### **Configuración .env:**
```bash
EMAIL_ENABLED=true
EMAIL_ADDRESS=juan.perez@gmail.com
EMAIL_PASSWORD=abcd efgh ijkl mnop  # App Password de Gmail
EMAIL_NOMBRE_COMPLETO=Juan Pérez
EMAIL_TELEFONO=+54 9 11 1234-5678
```

### **Uso con Email:**
```bash
# Aplicación individual con email
python generador_cv_avanzado.py --empresa "TechCorp" --postulacion "QA SSR..." --email

# Batch con emails automáticos  
python generador_cv_avanzado.py --batch postulaciones.csv --email
```

## 🕷️ Ejemplos de Web Scraping

### **Búsqueda Básica por Área:**

```bash
# Buscar trabajos QA en Buenos Aires (default)
python generador_cv_avanzado.py --scrape qa

# Buscar Python en Córdoba
python generador_cv_avanzado.py --scrape python --location "Córdoba"

# Buscar Java en Rosario
python generador_cv_avanzado.py --scrape java --location "Rosario"

# Buscar Backend en Buenos Aires
python generador_cv_avanzado.py --scrape backend

# Buscar Full Stack en cualquier ubicación
python generador_cv_avanzado.py --scrape fullstack --location "Argentina"
```

### **Output Típico del Scraping:**

```bash
python generador_cv_avanzado.py --scrape qa --save-jobs
```

**Resultado:**
```
>>> Generador de CV Inteligente v3.0 - MODO WEB SCRAPING
🔍 Buscando: qa
📍 Ubicación: Buenos Aires
🕷️ Scraping habilitado: SÍ

🔍 BÚSQUEDA AUTOMÁTICA DE TRABAJOS
📍 Área: qa
🌎 Ubicación: Buenos Aires
🔑 Keywords: qa engineer, tester, quality assurance, automation, selenium
==================================================

🕷️ Scrapeando COMPUTRABAJO...
🕷️ Scrapeando computrabajo: qa engineer en Buenos Aires
✅ computrabajo: 8 trabajos encontrados
   └── 'qa engineer': 8 trabajos
   [delay 2 segundos]
🕷️ Scrapeando computrabajo: tester en Buenos Aires  
✅ computrabajo: 5 trabajos encontrados
   └── 'tester': 5 trabajos
   [delay 2 segundos]
🕷️ Scrapeando computrabajo: automation en Buenos Aires
✅ computrabajo: 7 trabajos encontrados
   └── 'automation': 7 trabajos

🕷️ Scrapeando ZONAJOBS...
   └── 'qa engineer': 4 trabajos
   └── 'tester': 2 trabajos

🕷️ Scrapeando INDEED...
   └── 'qa engineer': 6 trabajos
   └── 'automation': 3 trabajos

📊 RESUMEN DE BÚSQUEDA:
   • Total encontrados: 35
   • Únicos (sin duplicados): 23
   • Portales consultados: 3

💾 Trabajos guardados en: cv_generados/trabajos_encontrados_20250113_1500.csv

¿Procesar estos 23 trabajos automáticamente? (y/N): y

🚀 Procesando trabajos con modo batch...
==================================================
📝 Procesando 1: TechCorp Argentina
>>> Analizando postulación de TechCorp Argentina...
>>> Tipo detectado: qa_automatizacion (semi_senior)
✅ TechCorp Argentina: CV generado exitosamente

📝 Procesando 2: StartupTech
>>> Analizando postulación de StartupTech...
❌ StartupTech: Rechazada (fit insuficiente)

[... procesando los 23 trabajos ...]

📊 RESUMEN DE PROCESAMIENTO BATCH
============================================================
📈 ESTADÍSTICAS:
   • Total procesadas: 23
   • ✅ Exitosas: 15
   • ❌ Rechazadas: 8
   • 💥 Errores: 0
   • 📊 Tasa de éxito: 65.2%
```

### **Flujo Completo Automatizado:**

```bash
# Comando que automatiza TODO el proceso de búsqueda laboral
python generador_cv_avanzado.py --scrape fullstack --save-jobs --email --umbral 75
```

**Lo que hace:**
1. 🕷️ **Busca trabajos** Full Stack en 3 portales
2. 🧹 **Filtra spam** automáticamente  
3. 💾 **Guarda en CSV** los trabajos válidos
4. 🤖 **Procesa cada trabajo** con el algoritmo de fit
5. ✨ **Genera CVs personalizados** para los que tengan fit ≥75%
6. 📧 **Envía emails automáticamente** con CVs adjuntos
7. 📊 **Actualiza estadísticas** en base de datos

### **Ejemplo por Ubicación:**

```bash
# Buscar en diferentes ciudades
python generador_cv_avanzado.py --scrape python --location "Córdoba"
python generador_cv_avanzado.py --scrape java --location "Rosario"  
python generador_cv_avanzado.py --scrape backend --location "Mendoza"
```

### **Template de Email Generado:**
```
Asunto: Aplicación para QA Automation Engineer - Juan Pérez

Estimados,

Me dirijo a ustedes para aplicar a la posición de QA Automation Engineer 
publicada por TechCorp.

Adjunto mi CV actualizado donde podrán encontrar mi experiencia en 
Python, Selenium, QA.

Gracias por la oportunidad en TechCorp. Me postulé porque tengo una 
experiencia única combinando desarrollo full stack y QA...

Quedo a disposición para una entrevista.

Saludos cordiales,
Juan Pérez
+54 9 11 1234-5678
juan.perez@gmail.com
```

## 📊 Ejemplos de Dashboard

### **Comando:**
```bash
python generador_cv_avanzado.py --stats
```

### **Output:**
```
📊 DASHBOARD DE ESTADÍSTICAS
============================================================

📈 RESUMEN GENERAL:
   • Total aplicaciones: 25  
   • Fit promedio: 78.5%

🎯 POR TIPO DE POSICIÓN:
   • qa_automatizacion: 12 aplicaciones | Fit: 82.1% | Salario prom: $1450
   • desarrollador_python: 8 aplicaciones | Fit: 85.3% | Salario prom: $1300
   • desarrollador_java: 5 aplicaciones | Fit: 71.2% | Salario prom: $1150

🏢 TOP EMPRESAS:
   • Google: 3 aplicaciones | Última: 2025-01-08
   • Microsoft: 2 aplicaciones | Última: 2025-01-07
   • Amazon: 2 aplicaciones | Última: 2025-01-06

💰 SALARIOS DETECTADOS:
   • USD: $1325 promedio ($800 - $2000)

🕒 ÚLTIMAS APLICACIONES:
   • Google (desarrollador_python) | 89% | 2025-01-08
   • Microsoft (qa_automatizacion) | 85% | 2025-01-07
   • Amazon (desarrollador_java) | 72% | 2025-01-06
```

## ⏱️ Configuración de Delays en Web Scraping

### **¿Qué son los delays y por qué son importantes?**

Los **delays** son pausas entre requests para simular comportamiento humano:

```python
# Sin delays (MALO - pueden bloquearte)
request1 -> Computrabajo (tiempo 0s)
request2 -> Computrabajo (tiempo 0.1s)  
request3 -> Computrabajo (tiempo 0.2s)
# Resultado: IP bloqueada por "bot behavior"

# Con delays (BUENO - comportamiento humano)
request1 -> Computrabajo (tiempo 0s)
[delay 2 segundos]
request2 -> Computrabajo (tiempo 2s)
[delay 2 segundos]  
request3 -> Computrabajo (tiempo 4s)
# Resultado: Scraping exitoso y ético
```

### **Configuraciones de Delay Recomendadas:**

#### **⚡ Rápido (1 segundo):**
```json
"delay_between_requests": 1
```
- **Tiempo total**: ~15 segundos para búsqueda completa
- **Riesgo**: Medio - algunos portales pueden detectar
- **Recomendado para**: Testing rápido

#### **⚖️ Equilibrado (2 segundos - DEFAULT):**
```json
"delay_between_requests": 2  
```
- **Tiempo total**: ~30 segundos para búsqueda completa
- **Riesgo**: Bajo - comportamiento humano aceptable
- **Recomendado para**: Uso normal diario

#### **🛡️ Conservador (5 segundos):**
```json
"delay_between_requests": 5
```
- **Tiempo total**: ~75 segundos para búsqueda completa  
- **Riesgo**: Prácticamente nulo
- **Recomendado para**: Cuentas muy valiosas o uso intensivo

### **Cálculo de Tiempo Total:**

```
Tiempo = Portales × Keywords × Delay

Ejemplo con QA:
3 portales × 5 keywords × 2 segundos = 30 segundos total

Ejemplo con todas las áreas:
3 portales × (5+5+5+5+4) keywords × 2 segundos = 144 segundos = ~2.4 minutos
```

## 🛠️ Ejemplos de Configuración Avanzada

### **Scraping + Umbral Personalizado:**
```bash
# Más estricto (solo fit > 85%)
python generador_cv_avanzado.py --scrape qa --umbral 85 --save-jobs

# Menos estricto (fit > 60%)  
python generador_cv_avanzado.py --scrape python --umbral 60 --save-jobs
```

### **Scraping Multi-Área:**
```bash
# Buscar en todas las áreas (ejecutar uno por uno)
python generador_cv_avanzado.py --scrape qa --save-jobs
python generador_cv_avanzado.py --scrape python --save-jobs  
python generador_cv_avanzado.py --scrape java --save-jobs
python generador_cv_avanzado.py --scrape backend --save-jobs
python generador_cv_avanzado.py --scrape fullstack --save-jobs
```

### **Configuración Personalizada:**
```bash
# Con archivo de config personalizado
python generador_cv_avanzado.py --config mi_config.json --umbral 80 --email
```

## 🎯 Casos Edge y Troubleshooting

### **Postulación Rechazada - Tecnología Desconocida:**
```
Input: "Senior .NET Developer con C# y Visual Basic"
Output: >>> 🚫 Tecnologías detectadas fuera de nuestro perfil: ['.net', 'c#']
```

### **Postulación Rechazada - Fit Insuficiente:**
```
Input: "Data Scientist con R y machine learning"  
Output: >>> FIT INSUFICIENTE (45%) - Mínimo requerido: 70%
```

### **Postulación Rechazada - Senior:**
```
Input: "Senior Java Architect, 8+ años experiencia"
Output: >>> POSICIÓN FUERA DE ESTRATEGIA (senior no se aplica automáticamente)
```

## 📋 Lista de Verificación

### **Antes de usar:**
- [ ] ✅ Dependencias instaladas
- [ ] ✅ Archivo .env configurado (si usas email)
- [ ] ✅ CV base (cv_hilario.docx) presente
- [ ] ✅ Permisos de escritura en carpeta

### **Para uso productivo:**
- [ ] 📧 Email configurado con App Password
- [ ] 📊 Umbral de fit ajustado a tu estrategia
- [ ] 📝 CSV con postulaciones preparado
- [ ] 🔍 Revisión de logs para debugging

## 🚀 Tips Avanzados

### **Optimizar Tasa de Éxito:**
```bash
# Ver estadísticas actuales
python generador_cv_avanzado.py --stats

# Ajustar umbral según results
python generador_cv_avanzado.py --umbral 75  # Si muchos rechazos
python generador_cv_avanzado.py --umbral 85  # Si quieres más selectivo
```

### **Automatización con Cron (Linux/Mac):**
```bash
# Ejecutar batch diariamente a las 9 AM
0 9 * * * cd /ruta/al/script && python generador_cv_avanzado.py --batch nuevas_postulaciones.csv --email
```

### **Automatización con Task Scheduler (Windows):**
- Programa tarea diaria
- Comando: `python C:\ruta\generador_cv_avanzado.py --batch postulaciones.csv`

---

## 📞 ¿Necesitas Más Ejemplos?

Si tienes un caso específico no cubierto aquí:

1. 🐛 Abre un [Issue](../../issues) con tag `documentation`
2. 💬 Inicia una [Discusión](../../discussions)  
3. 🤝 Contribuye agregando tu ejemplo a esta guía

**¡Cada ejemplo ayuda a la comunidad!** 🚀
