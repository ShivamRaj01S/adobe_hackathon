import os
import fitz  # PyMuPDF

def extract_text_from_pdfs(pdf_folder):
    full_text = ""
    for file in sorted(os.listdir(pdf_folder)):
        if file.lower().endswith('.pdf'):
            path = os.path.join(pdf_folder, file)
            doc = fitz.open(path)
            for page in doc:
                full_text += page.get_text()
            doc.close()
    return full_text
