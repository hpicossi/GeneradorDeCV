# 🤝 Guía de Contribución

¡Gracias por tu interés en contribuir al **Generador de CV Inteligente**! 🎉

## 🚀 Cómo Contribuir

### 1. **Fork del Repositorio**
```bash
# Fork en GitHub, luego clona tu fork
git clone https://github.com/tu-usuario/GeneradorDeCV.git
cd GeneradorDeCV
```

### 2. **Configurar Entorno de Desarrollo**
```bash
# Instalar dependencias
pip install python-docx reportlab python-dotenv

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus datos
```

### 3. **Crear Rama para tu Feature**
```bash
git checkout -b feature/nombre-descriptivo
# o
git checkout -b fix/descripcion-del-bug
```

### 4. **Hacer Cambios**

#### **Estilo de Código:**
- Usar **PEP 8** para Python
- Documentar funciones con **docstrings**
- Agregar **comentarios** para lógica compleja
- **4 espacios** para indentación

#### **Ejemplo de función bien documentada:**
```python
def detectar_tipo_posicion(self, texto_postulacion: str) -> Tuple[str, str]:
    """
    Detecta el tipo de posición y nivel de seniority.
    
    Args:
        texto_postulacion (str): Descripción de la postulación
        
    Returns:
        Tuple[str, str]: (tipo_posicion, nivel_seniority)
        
    Raises:
        ValueError: Si no se puede determinar el tipo
    """
```

### 5. **Testing**
```bash
# Probar funcionalidad básica
python generador_cv_avanzado.py --help

# Probar con datos de ejemplo
python generador_cv_avanzado.py --batch postulaciones_ejemplo.csv

# Probar web scraping (NUEVA FUNCIONALIDAD)
python generador_cv_avanzado.py --scrape qa

# Probar flujo completo con scraping
python generador_cv_avanzado.py --scrape python --save-jobs

# Verificar que no hay errores
python generador_cv_avanzado.py --stats
```

### 6. **Commit y Push**
```bash
# Commit descriptivo
git add .
git commit -m "Add: nueva funcionalidad de análisis de salarios"

# Push a tu fork
git push origin feature/nombre-descriptivo
```

### 7. **Crear Pull Request**

En GitHub:
1. Ve a tu fork
2. Click "New Pull Request"
3. Describe los cambios claramente
4. Incluye capturas si es relevante

## 🎯 Tipos de Contribuciones

### 🐛 **Bug Fixes**
- Reportar bugs con pasos para reproducir
- Incluir logs de error
- Proponer solución si es posible

### ✨ **Nuevas Funcionalidades**
- Discutir la idea primero en Issues
- Mantener compatibilidad hacia atrás
- Actualizar documentación

### 📚 **Documentación**
- Mejorar README
- Agregar ejemplos
- Traducciones bienvenidas

### 🧪 **Testing**
- Agregar tests unitarios
- Probar en diferentes OS
- Validar casos edge

## 📋 Checklist antes del PR

- [ ] ✅ Código sigue PEP 8
- [ ] 📚 Funciones documentadas
- [ ] 🧪 Testing realizado
- [ ] 📖 README actualizado si es necesario
- [ ] 🔒 No incluye datos sensibles
- [ ] 📝 Commit messages descriptivos

## 🚫 Qué NO hacer

- ❌ Hardcodear credenciales
- ❌ Cambios masivos sin discusión
- ❌ Romper funcionalidad existente
- ❌ Commits sin mensaje descriptivo
- ❌ Subir archivos personales (.env, CVs)

## 💡 Ideas de Contribuciones

### **Fáciles (Good First Issue):**
- Agregar nuevas tecnologías al diccionario
- Mejorar templates de email
- Traducir mensajes al inglés
- Agregar validaciones de entrada

### **Intermedias:**
- Sistema de plantillas de CV
- Integración con más proveedores de email
- Mejoras en detección de tipo de empresa
- Dashboard con más métricas
- Optimización de selectores de scraping
- Nuevos portales de trabajo (Bumeran, LinkedIn)

### **Avanzadas:**
- Web dashboard con Flask/FastAPI
- Machine Learning para optimización
- Integración con APIs de job boards
- Sistema de notificaciones
- Scraping con JavaScript (Selenium) para sitios SPA
- API REST para integraciones externas

## 📞 Soporte para Contribuidores

### **¿Dudas sobre el código?**
- Abre un Issue con tag `question`
- Revisa la documentación en código
- Mira ejemplos en el proyecto

### **¿Ideas para nuevas features?**
- Abre un Issue con tag `enhancement`
- Discute antes de implementar
- Considera impacto en usuarios existentes

### **¿Problemas técnicos?**
- Detalla tu entorno (OS, Python version)
- Incluye logs completos
- Pasos para reproducir el problema

## 🏆 Reconocimiento

Los contribuidores serán:

- 📝 Listados en README (si desean)
- 🏷️ Mencionados en release notes
- ⭐ Reconocidos en el historial de GitHub

## 📊 Proceso de Review

1. **Revisión Automática**: Checks de estilo y tests
2. **Revisión Manual**: Un maintainer revisará el código
3. **Feedback**: Comentarios y sugerencias
4. **Iteración**: Hacer cambios solicitados
5. **Merge**: Una vez aprobado, se integra

## 📜 Código de Conducta

- 🤝 Ser respetuoso y profesional
- 💬 Comunicación constructiva
- 🌟 Ayudar a otros contribuidores
- 📚 Compartir conocimiento

---

## 🙏 ¡Gracias por Contribuir!

Tu tiempo y esfuerzo ayudan a hacer este proyecto mejor para toda la comunidad. 

**¡Cada contribución cuenta!** 🚀
