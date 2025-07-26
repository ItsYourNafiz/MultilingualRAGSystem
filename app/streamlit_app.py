import streamlit as st
from retriever import retrieve_similar_chunks
from generator import generate_answer
import logging

logging.basicConfig(level=logging.INFO)

st.title("🌐 Multilingual RAG System (Bangla & English)")

query = st.text_input("Enter your question (Bangla or English):")

if st.button("Ask") and query.strip():
    with st.spinner("Retrieving relevant documents..."):
        try:
            chunks = retrieve_similar_chunks(query, top_k=3)
            context = "\n\n".join(chunks)
            st.markdown("**Retrieved Context:**")
            st.write(context)
        except Exception as e:
            st.error(f"Error retrieving chunks: {e}")
            st.stop()

    with st.spinner("Generating answer..."):
        try:
            answer = generate_answer(query, context)
            st.markdown("**Answer:**")
            st.success(answer)
        except Exception as e:
            st.error(f"Error generating answer: {e}")
