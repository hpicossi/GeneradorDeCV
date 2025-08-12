# 🚀 Generador de CV Inteligente

Un sistema automatizado e inteligente para generar CVs personalizados basados en análisis de postulaciones laborales. Analiza automáticamente las descripciones de trabajo, detecta el tipo de posición y nivel de seniority, y adapta tu CV para maximizar las posibilidades de éxito.

## 📋 ¿Qué hace este script?

El **Generador de CV Inteligente** es una herramienta que:

- 🎯 **Analiza postulaciones** automáticamente y detecta tipo de posición (QA, Python, Java, Frontend, etc.)
- 📊 **Calcula porcentaje de fit** entre tu perfil y los requisitos del puesto
- ✨ **Adapta tu CV** automáticamente según el tipo de posición detectada
- 💰 **Detecta salarios** en las postulaciones y evalúa competitividad
- 📝 **Genera speech personalizado** para entrevistas
- 📈 **Filtra oportunidades** según tu estrategia de aplicación
- 🗂️ **Organiza todo** en archivos PDF y resúmenes JSON

## 🌟 Características Principales

### ✅ **Detección Inteligente**
- Identifica automáticamente QA, Python, Java, Frontend, Full Stack
- Detecta nivel de seniority (Junior, Semi-Senior, Senior)
- Rechaza automáticamente posiciones fuera de tu perfil

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
pip install python-docx reportlab
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
pip install python-docx reportlab
```

### 3. **Verificar archivos necesarios**
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
- Python, Java, Frontend, Full Stack

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

## 📈 Métricas y Estadísticas

Cada postulación procesada genera:
- ✅ **Tasa de éxito** por tipo de posición
- 📊 **Keywords más exitosas**
- 💰 **Rangos salariales detectados**
- 🎯 **Fit promedio** por empresa

## 🤝 Contribuciones

¿Tienes ideas para mejorar el sistema? ¡Las contribuciones son bienvenidas!

### **Próximas mejoras:**
- Dashboard web con estadísticas
- Integración con APIs de trabajo
- Sistema de follow-up automático
- Análisis de competencia

## 📞 Soporte

Si tienes problemas:
1. Revisa el archivo `cv_generator.log`
2. Verifica que todos los archivos estén presentes
3. Confirma que las dependencias estén instaladas

---

**¡Automatiza tu búsqueda laboral y maximiza tus oportunidades! 🚀**
