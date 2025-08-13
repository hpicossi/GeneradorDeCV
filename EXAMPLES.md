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

## 🛠️ Ejemplos de Configuración Avanzada

### **Umbral Personalizado:**
```bash
# Más estricto (solo fit > 85%)
python generador_cv_avanzado.py --umbral 85

# Menos estricto (fit > 60%)  
python generador_cv_avanzado.py --umbral 60
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
