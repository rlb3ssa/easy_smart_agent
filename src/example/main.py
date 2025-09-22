import os
import shutil
import uuid
from datetime import datetime

from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from pydantic import BaseModel
from mariza.crews.artigo.crew import ArtigoCrew
from mariza.crews.concurso.crew import ConcursoCrew
from mariza.crews.envolvido.crew import EnvolvidoCrew
from mariza.crews.resumo.crew import ResumoCrew
from mariza.dto import BaseResponse
from mariza.dto import Process
from typing import Optional, Dict, Any, List

from mariza.service.embed_service import embed_file_to_knowledge
from mariza.service.extract_service import extract_and_save
from mariza.service.ocr_service import process_pdfs

app = FastAPI(
    title="Example Project",
    description="You are ready to create your own crewai project!",
    version="1.0.0"
)


@app.get("/", response_model=BaseResponse)
async def root():
    return BaseResponse(
        status=True,
        message="Assistant AI online.",
        timestamp=datetime.now().isoformat()
    )


@app.post("/process", response_model=BaseResponse)
async def process_example(
    arquivos: List[UploadFile] = File(...),
    texto: Optional[str] = Form(None),
):
    try:
        # Gerar ID único para o caso
        case_id = str(uuid.uuid4())
        temp_dir = f"/tmp/{case_id}"
        os.makedirs(temp_dir, exist_ok=True)

        # 1. Salvar arquivos temporários
        pdf_paths = []
        for arquivo in arquivos:
            file_path = os.path.join(temp_dir, arquivo.filename)
            with open(file_path, "wb") as f:
                shutil.copyfileobj(arquivo.file, f)
            pdf_paths.append(file_path)

        # 2. Aplicar OCR se necessário
        final_pdfs = process_pdfs(pdf_paths)

        # 3. Extrair, limpar e dividir o conteúdo
        knowledge_path = f"./knowledge/{case_id}.txt"
        os.makedirs("./knowledge", exist_ok=True)
        extract_and_save(final_pdfs, knowledge_path)

        # 4. Vetorizar no Chroma via CrewAI Knowledge
        embed_file_to_knowledge(knowledge_path, case_id)

        inputs = {
            'instrucao': texto,
            'case_id': case_id
        }

        data = {}

        data["case_id"] = case_id

        data["artigos"] = ArtigoCrew().crew().kickoff(inputs=inputs).raw

        data["concursos"] = ConcursoCrew().crew().kickoff(inputs=inputs).raw

        data["envolvidos"] = EnvolvidoCrew().crew().kickoff(inputs=inputs).raw

        data["resumo_comentado"] = ResumoCrew().crew().kickoff(inputs=inputs).raw

        process_data = Process(**data)

        return BaseResponse(
            status=True,
            timestamp=datetime.now().isoformat(),
            data=process_data
        )
    except Exception as e:
        return BaseResponse(
            status=False,
            message=f"Erro na execução da crew: {e}",
            timestamp=datetime.now().isoformat()
        )




