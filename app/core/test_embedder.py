from pdf_reader import extract_text_from_pdf
from text_splitter import split_text_into_chunks
from embedder import generate_embeddings

pdf_path = "data/raw/clinical_notes.pdf"

text = extract_text_from_pdf(pdf_path)
chunks = split_text_into_chunks(text)
embeddings = generate_embeddings(chunks)

print(f"Total chunks: {len(chunks)}")
print(f"Total embeddings: {len(embeddings)}")
print(f"Embedding dimension: {len(embeddings[0])}")