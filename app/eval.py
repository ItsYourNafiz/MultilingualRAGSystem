from retriever import retrieve_similar_chunks
from generator import generate_answer
import logging
from deep_translator import GoogleTranslator

logging.basicConfig(level=logging.INFO)

def translate_to_bangla(query):
    return GoogleTranslator(source='auto', target='bn').translate(query)

def translate_to_english(query):
    return GoogleTranslator(source='auto', target='en').translate(query)

if __name__ == "__main__":
    query = input("🔍 Enter your question (EN/BN): ")

    try:
        chunks = retrieve_similar_chunks(query, top_k=3)
    except Exception as e:
        print(f"❌ Error retrieving chunks: {e}")
        exit()

    if not chunks or all(c.strip() == "" for c in chunks):
        print("⚠️ No relevant results found. Trying fallback translation...")
        fallback_query = translate_to_english(query) if any('\u0980' <= ch <= '\u09FF' for ch in query) else translate_to_bangla(query)
        print(f"🌐 Translated query: {fallback_query}")
        chunks = retrieve_similar_chunks(fallback_query, top_k=3)

    context = "\n\n".join(chunks)

    print("\n🤖 Generating answer...\n")
    try:
        answer = generate_answer(query, context)
        print("✅ Answer:\n", answer)
    except Exception as e:
        print(f"❌ Generation failed: {e}")
