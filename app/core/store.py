from typing import Any
from app.core.vector_store import FAISSVectorStore

rag_store: dict[str, Any] = {
    "pdf_path": "data/raw/clinical_notes.pdf",
    "text": None,
    "chunks": None,
    "embeddings": None,
    "vector_store": FAISSVectorStore(),
}