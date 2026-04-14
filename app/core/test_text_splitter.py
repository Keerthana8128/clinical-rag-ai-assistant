from pdf_reader import extract_text_from_pdf
from text_splitter import split_text_into_chunks

pdf_path = "data/raw/clinical_notes.pdf"

text = extract_text_from_pdf(pdf_path)
chunks = split_text_into_chunks(text)

print(f"Total chunks created: {len(chunks)}\n")

for i, chunk in enumerate(chunks, start=1):
    print(f"--- Chunk {i} ---")
    print(chunk)
    print()