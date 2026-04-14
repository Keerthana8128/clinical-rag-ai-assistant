from pdf_reader import extract_text_from_pdf
from text_splitter import split_text_into_chunks
from embedder import generate_embeddings
from retriever import retrieve_relevant_chunks

pdf_path = "data/raw/clinical_notes.pdf"

text = extract_text_from_pdf(pdf_path)
chunks = split_text_into_chunks(text)
embeddings = generate_embeddings(chunks)

query = "What is the diagnosis?"
results = retrieve_relevant_chunks(query, chunks, embeddings, top_k=2)

print(f"Question: {query}\n")

for i, result in enumerate(results, start=1):
    print(f"--- Result {i} ---")
    print(result)
    print()