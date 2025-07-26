import fitz  # PyMuPDF
import re
import os

def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    return text

def clean_text(text):
    text = re.sub(r'\n+', '\n', text)          # Collapse multiple newlines
    text = re.sub(r'[ \t]+', ' ', text)        # Normalize spaces/tabs
    return text.strip()

if __name__ == "__main__":
    input_path = "data/HSC26_Bangla1.pdf"  # Update to your actual file name
    output_path = "data/cleaned.txt"

    raw_text = extract_text_from_pdf(input_path)
    cleaned_text = clean_text(raw_text)

    os.makedirs("data", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print(f"✅ Cleaned text saved to {output_path}")
