import faiss
import pickle
from sentence_transformers import SentenceTransformer
import os
import logging

logging.basicConfig(level=logging.INFO)

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

INDEX_PATH = "embeddings/faiss.index"
META_PATH = "embeddings/meta.pkl"

if not os.path.exists(INDEX_PATH) or not os.path.exists(META_PATH):
    raise FileNotFoundError("❌ FAISS index or metadata file not found. Run vector_store.py first.")

index = faiss.read_index(INDEX_PATH)

with open(META_PATH, 'rb') as f:
    chunks = pickle.load(f)

def retrieve_similar_chunks(query, top_k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, top_k)

    logging.info(f"🔍 Similarity distances: {distances[0]}")

    return [chunks[i] for i in indices[0]]
