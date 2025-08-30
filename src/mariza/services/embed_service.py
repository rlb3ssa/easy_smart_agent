from crewai_tools import Knowledge

def embed_file_to_knowledge(txt_path: str, case_id: str):
    # Isto irá salvar vetores no Chroma automaticamente
    knowledge = Knowledge(
        name=case_id,
        path=txt_path,
        embedder="ollama/nomic-embed-text"
    )
    return knowledge
