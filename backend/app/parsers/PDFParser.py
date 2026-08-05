import fitz  # PyMuPDF

class PDFParser:
    def extract_text(self, pdf_path):
        text = ""
        with fitz.open(pdf_path) as pdf:
            for page in pdf:
                text += page.get_text()
                text += "\n"
        fitz.close(pdf)
        return text