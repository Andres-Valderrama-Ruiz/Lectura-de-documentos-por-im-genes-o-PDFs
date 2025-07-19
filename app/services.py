import os
import pytesseract
from pdf2image import convert_from_path
from app.database import save_to_db

# Configura Tesseract y Poppler
os.environ["PATH"] += os.pathsep + r'C:\poppler\poppler-24.08.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

async def process_document(file):
    """
    Procesa un documento (imagen o PDF) y devuelve el tipo de documento y texto extraído
    """
    # Guardar archivo temporal
    contents = await file.read()
    temp_filepath = f"temp_{file.filename}"

    with open(temp_filepath, "wb") as f:
        f.write(contents)

    # Extraer texto del archivo
    text = ""
    if temp_filepath.endswith(".pdf"):
        images = convert_from_path(temp_filepath)
        for page in images:
            text += pytesseract.image_to_string(page)
    else:
        text = pytesseract.image_to_string(temp_filepath)

    # Identificar tipo de documento (versión mejorada)
    doc_type = "Desconocido"
    text_upper = text.upper()  # Convertir todo a mayúsculas para comparación
    
    # Patrones para cédula (incluyendo variaciones comunes)
    cedula_patterns = [
        "CEDULA DE CIUDADANIA",
        "CÉDULA DE CIUDADANÍA",  
        "IDENTIFICACION PERSONAL", 
        "REGISTRADOR NACIONAL"
    ]
    
    # Patrones para pasaporte
    pasaporte_patterns = [
        "PASAPORTE",
        "PASSPORT",
        "DOCUMENTO DE VIAJE"
    ]
    
    # Verificar primero cédula (más común)
    if any(pattern in text_upper for pattern in cedula_patterns):
        doc_type = "Cédula de Ciudadanía"
    elif any(pattern in text_upper for pattern in pasaporte_patterns):
        doc_type = "Pasaporte"

    # Guardar en la base de datos
    save_to_db(doc_type, text)

    # Eliminar archivo temporal
    os.remove(temp_filepath)

    return {
        "tipo_documento": doc_type,
        "texto_extraido": text
    }