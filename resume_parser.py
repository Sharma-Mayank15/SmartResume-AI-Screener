import fitz  # PyMuPDF

def parse_resume(file_bytes: bytes) -> str:
    with open("temp_resume.pdf", "wb") as f:
        f.write(file_bytes)
    doc = fitz.open("temp_resume.pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text
