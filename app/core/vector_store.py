import faiss
import numpy as np
from typing import List


class FAISSVectorStore:
    def __init__(self):
        self.index = None
        self.text_chunks = []

    def build_index(self, embeddings: List[List[float]], chunks: List[str]):
        dimension = len(embeddings[0])

        self.index = faiss.IndexFlatL2(dimension)

        vectors = np.array(embeddings).astype("float32")
        self.index.add(vectors)

        self.text_chunks = chunks

    def search(self, query_embedding: List[float], top_k: int = 3):
        query_vector = np.array([query_embedding]).astype("float32")

        distances, indices = self.index.search(query_vector, top_k)

        results = [self.text_chunks[i] for i in indices[0]]

        return results