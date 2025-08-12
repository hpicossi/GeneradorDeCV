
import os
import re
from datetime import datetime
from docx import Document
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

# Cargar CV base
def cargar_cv_docx(path):
    doc = Document(path)
    return "\n".join([p.text for p in doc.paragraphs if p.text.strip() != ""])

# Extraer palabras clave desde la postulación
def extraer_keywords(texto_postulacion):
    texto_postulacion = texto_postulacion.lower()
    posibles_keywords = ['selenium', 'java', 'python', 'qa', 'manual', 'automatización', 'sql', 'rest', 'api', 'postman', 'locust']
    return [kw for kw in posibles_keywords if kw in texto_postulacion]

# Evaluar compatibilidad y ajustar el CV
def mejorar_cv(cv_texto, post_texto):
    keywords = ['qa', 'selenium', 'java', 'python', 'rest', 'sql', 'postman', 'jira', 'locust', 'agile', 'ci/cd']
    extra = []
    for kw in keywords:
        if kw in post_texto.lower() and kw not in cv_texto.lower():
            extra.append(f"Incorporé experiencia relevante en {kw} para cumplir con los requisitos del puesto.")
    if extra:
        cv_texto += "\n\nAdaptación basada en la postulación:\n" + "\n".join(extra)
    return cv_texto

# Crear CV personalizado como PDF
def generar_cv_pdf(texto_cv, nombre_archivo):
    doc = SimpleDocTemplate(nombre_archivo, pagesize=A4)
    styles = getSampleStyleSheet()
    contenido = [Paragraph(parrafo, styles["Normal"]) for parrafo in texto_cv.split("\n")]
    doc.build(contenido)

# Generar speech de entrevista
def generar_speech(nombre_empresa, keywords):
    base = f"Gracias por la oportunidad en {nombre_empresa}. Me postulé porque "
    if "automatización" in keywords:
        base += "cuento con experiencia en automatización de pruebas usando herramientas como Selenium y Locust. "
    if "qa" in keywords or "manual" in keywords:
        base += "he realizado pruebas manuales funcionales en frontend y backend, con foco en calidad y validaciones cruzadas. "
    if "python" in keywords or "java" in keywords:
        base += "además tengo experiencia como desarrollador backend, lo que complementa mi perfil técnico. "
    base += "Estoy entusiasmado por aportar valor al equipo y seguir creciendo profesionalmente."
    return base

# Guardar oferta de trabajo
def guardar_oferta(texto_postulacion, carpeta):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(carpeta, f"oferta_{now}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(texto_postulacion)
    return path

# MAIN
if __name__ == "__main__":
    texto_postulacion = input("Pega aquí la descripción de la postulación:\n")
    nombre_empresa = input("Nombre de la empresa:\n")
    path_cv_base = "cv_hilario.docx"  # Reemplazar con tu path real

    texto_cv_base = cargar_cv_docx(path_cv_base)
    keywords_detectadas = extraer_keywords(texto_postulacion)

    texto_cv_mejorado = mejorar_cv(texto_cv_base, texto_postulacion)

    carpeta_salida = "cv_generados"
    os.makedirs(carpeta_salida, exist_ok=True)
    nombre_pdf = os.path.join(carpeta_salida, f"cv_{nombre_empresa.lower()}_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf")

    generar_cv_pdf(texto_cv_mejorado, nombre_pdf)
    path_oferta = guardar_oferta(texto_postulacion, carpeta_salida)
    speech = generar_speech(nombre_empresa, keywords_detectadas)

    print("\n✅ CV generado en:", nombre_pdf)
    print("📄 Oferta guardada en:", path_oferta)
    print("🗣️ Speech sugerido:\n", speech)
