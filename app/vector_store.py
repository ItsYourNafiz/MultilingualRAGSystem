from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
import os


def load_chunks(path):
    with open(path, 'r', encoding='utf-8') as f:
        return [chunk.strip() for chunk in f.read().split("\n\n") if chunk.strip()]


def embed_chunks(chunks, model_name='paraphrase-multilingual-MiniLM-L12-v2'):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(chunks, show_progress_bar=True)
    return np.array(embeddings), model


def save_faiss_index(embeddings, chunks, index_path="embeddings/faiss.index", metadata_path="embeddings/meta.pkl"):
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    os.makedirs("embeddings", exist_ok=True)
    faiss.write_index(index, index_path)

    with open(metadata_path, 'wb') as f:
        pickle.dump(chunks, f)

    print(f"✅ FAISS index and metadata saved to {index_path} and {metadata_path}")


if __name__ == "__main__":
    chunk_file_path = "data/chunks.txt"
    chunks = load_chunks(chunk_file_path)
    embeddings, _ = embed_chunks(chunks)
    save_faiss_index(embeddings, chunks)
