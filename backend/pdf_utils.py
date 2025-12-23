from PyPDF2 import PdfReader

def extract_text(files):
    text = ""
    for file in files:
        reader = PdfReader(file.file)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text
