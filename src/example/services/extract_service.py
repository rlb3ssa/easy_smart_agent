import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import re

def clean_text(text: str) -> str:
    # Remove cabeçalho, rodapé, números de página etc.
    text = re.sub(r'Página \d+ de \d+', '', text)
    text = re.sub(r'\s{2,}', ' ', text)
    return text.strip()

def extract_and_save(pdfs: list[str], output_txt_path: str):
    all_docs = []
    for pdf in pdfs:
        loader = PyPDFLoader(pdf)
        pages = loader.load_and_split()
        for doc in pages:
            doc.page_content = clean_text(doc.page_content)
            all_docs.append(doc)

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(all_docs)

    with open(output_txt_path, "w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(chunk.page_content + "\n\n")
