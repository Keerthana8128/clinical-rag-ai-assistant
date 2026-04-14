from pdf_reader import extract_text_from_pdf

pdf_path = "data/raw/clinical_notes.pdf"

text = extract_text_from_pdf(pdf_path)

print("PDF text extracted successfully:\n")
print(text[:2000])