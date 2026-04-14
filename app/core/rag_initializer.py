from app.core.pdf_reader import extract_text_from_pdf
from app.core.text_splitter import split_text_into_chunks
from app.core.embedder import generate_embeddings
from app.core.store import rag_store


def initialize_rag_pipeline(pdf_path: str | None = None) -> None:
    if pdf_path:
        rag_store["pdf_path"] = pdf_path

    active_pdf_path = rag_store["pdf_path"]

    text = extract_text_from_pdf(active_pdf_path)
    chunks = split_text_into_chunks(text)
    embeddings = generate_embeddings(chunks)

    rag_store["text"] = text
    rag_store["chunks"] = chunks
    rag_store["embeddings"] = embeddings

    rag_store["vector_store"] = rag_store["vector_store"].__class__()
    rag_store["vector_store"].build_index(embeddings, chunks)

    print("RAG pipeline initialized with FAISS.")
    print(f"Loaded PDF: {active_pdf_path}")
    print(f"Total chunks: {len(chunks)}")
    print(f"Total embeddings: {len(embeddings)}")