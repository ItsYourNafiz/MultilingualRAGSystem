import os

def chunk_text(text, max_chunk_size=500):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(current_chunk) >= max_chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = []

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

if __name__ == "__main__":
    input_path = "data/cleaned.txt"
    output_path = "data/chunks.txt"

    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = chunk_text(text)

    os.makedirs("data", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(chunks))

    print(f"✅ Chunks saved to {output_path}")
