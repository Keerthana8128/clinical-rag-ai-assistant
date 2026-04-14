from pathlib import Path

from fastapi import APIRouter, File, UploadFile
from pydantic import BaseModel

from app.core.generator import generate_answer
from app.core.rag_initializer import initialize_rag_pipeline
from app.core.retriever import retrieve_relevant_chunks
from app.core.store import rag_store

router = APIRouter()


class QueryRequest(BaseModel):
    question: str


@router.get("/health")
def health_check():
    chunks = rag_store.get("chunks")
    embeddings = rag_store.get("embeddings")

    return {
        "status": "OK",
        "message": "API is healthy",
        "rag_loaded": chunks is not None and embeddings is not None,
        "active_pdf": rag_store.get("pdf_path"),
    }


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename:
        return {"error": "No file selected."}

    if not file.filename.lower().endswith(".pdf"):
        return {"error": "Only PDF files are allowed."}

    save_dir = Path("data/raw")
    save_dir.mkdir(parents=True, exist_ok=True)

    save_path = save_dir / file.filename

    file_bytes = await file.read()
    save_path.write_bytes(file_bytes)

    initialize_rag_pipeline(str(save_path))

    return {
        "message": "PDF uploaded and RAG pipeline reinitialized successfully.",
        "filename": file.filename,
        "pdf_path": str(save_path),
    }


@router.post("/ask")
def ask_question(request: QueryRequest):
    chunks = rag_store.get("chunks")
    embeddings = rag_store.get("embeddings")

    if not chunks or not embeddings:
        return {"error": "RAG pipeline is not initialized."}

    relevant_chunks = retrieve_relevant_chunks(request.question)
    answer = generate_answer(request.question, relevant_chunks)

    return {
        "question": request.question,
        "answer": answer,
        "sources": relevant_chunks,
    }