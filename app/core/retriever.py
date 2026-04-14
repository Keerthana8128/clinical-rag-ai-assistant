from app.core.embedder import generate_embeddings
from app.core.store import rag_store


def retrieve_relevant_chunks(query: str, top_k: int = 3):
    query_embedding = generate_embeddings([query])[0]

    vector_store = rag_store["vector_store"]

    results = vector_store.search(query_embedding, top_k)

    return results