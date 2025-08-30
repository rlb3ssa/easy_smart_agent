import os
import subprocess
from PyPDF2 import PdfReader

def needs_ocr(pdf_path: str, threshold: float = 0.2) -> bool:
    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)
    pages_with_text = sum(1 for page in reader.pages if page.extract_text())
    return (pages_with_text / total_pages) < threshold

def process_pdfs(pdf_paths: list[str]) -> list[str]:
    output_paths = []
    for path in pdf_paths:
        if needs_ocr(path):
            out_path = path.replace(".pdf", "_ocr.pdf")
            subprocess.run(["ocrmypdf", path, out_path])
            output_paths.append(out_path)
        else:
            output_paths.append(path)
    return output_paths
