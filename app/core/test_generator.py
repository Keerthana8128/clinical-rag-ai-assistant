from pdf_reader import extract_text_from_pdf
from text_splitter import split_text_into_chunks
from embedder import generate_embeddings
from retriever import retrieve_relevant_chunks
from generator import generate_answer

pdf_path = "data/raw/clinical_notes.pdf"

text = extract_text_from_pdf(pdf_path)
chunks = split_text_into_chunks(text)
embeddings = generate_embeddings(chunks)

query = "What is the diagnosis?"

relevant_chunks = retrieve_relevant_chunks(query, chunks, embeddings)

answer = generate_answer(query, relevant_chunks)

print(f"Question: {query}\n")
print("Answer:")
print(answer)