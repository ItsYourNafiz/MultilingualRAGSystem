# Multilingual Bilingual RAG System (Bangla & English)

## Overview

This repository contains a Retrieval-Augmented Generation (RAG) pipeline designed to answer questions in both Bengali and English by retrieving relevant context from a Bengali PDF corpus.

---

## Setup Guide

### Requirements

- Python 3.8+
- `pip install -r requirements.txt`
- Set environment variable `OPENROUTER_API_KEY` with your OpenRouter API key

## Used Tools, Libraries, and Packages

| Tool/Library          | Purpose                               | Reason for Choice                           |
| --------------------- | ------------------------------------- | ------------------------------------------- |
| PyMuPDF (fitz)        | Extract text from PDFs                | Robust Unicode support for Bengali          |
| sentence-transformers | Generate multilingual embeddings      | Efficient multilingual semantic vectors     |
| FAISS                 | Vector similarity search              | Fast nearest neighbor retrieval             |
| OpenRouter DeepSeek   | Language model completion             | Free tier, supports Bengali and English     |
| deep-translator       | Query translation fallback            | Improve retrieval coverage via translations |
| Streamlit             | Frontend UI                           | Easy prototyping & demo                     |
| python-dotenv         | Environment variable management       | Secure API key storage                      |
| Python stdlib         | File handling, logging, serialization | Basic utility functions                     |

### Sample Queries and Outputs

| Language    | Sample Query                                  | Sample Output (Summary)                                                                                         |
| ----------- | --------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Bengali** | `রবীন্দ্রনাথের সাহিত্যিক বৈশিষ্ট্য কী?`       | রবীন্দ্রনাথের সাহিত্যিক বৈশিষ্ট্যগুলি হলো মানবতাবাদ, প্রাকৃতিক ছবি, এবং গভীর ভাবনা।                             |
| **Bengali** | `বাংলা সাহিত্যে রবীন্দ্রনাথের অবদান কি?`      | রবীন্দ্রনাথ বাংলা সাহিত্যে নবজাগরণের সূচনা করেন এবং বিশ্বসাহিত্যে বাংলা ভাষার পরিচিতি করান।                     |
| **English** | `What are the main themes in Bengali poetry?` | The main themes include nature, humanism, spirituality, and patriotism.                                         |
| **English** | `Who was Rabindranath Tagore?`                | Rabindranath Tagore was a Bengali poet, writer, and Nobel laureate known for his literary works and philosophy. |

### FAQ

1. What method or library did you use to extract the text, and why? Did you face any formatting challenges with the PDF content?
We used PyMuPDF (fitz) for PDF text extraction because it provides robust and accurate extraction of Unicode text, which is essential for handling Bengali script without corrupting characters. PyMuPDF is also fast and handles complex PDF layouts better than many other libraries like PyPDF2.
Formatting challenges: Some PDFs contain inconsistent line breaks, multiple columns, or embedded fonts which can cause noise or irregular spacing. We mitigated this by applying simple text cleaning and normalization after extraction to improve chunk quality.

2. What chunking strategy did you choose (e.g., paragraph-based, sentence-based, character limit)? Why do you think it works well for semantic retrieval?
We adopted a fixed word count chunking strategy, splitting text into chunks of approximately 500 words each. This strikes a balance between chunk granularity and semantic coherence.

Too small chunks (sentence-based) can lose context,

Too large chunks (whole paragraphs or pages) can dilute semantic relevance.
This approach helps the embedding model capture meaningful semantic information in each chunk, enabling effective similarity search.

3. What embedding model did you use? Why did you choose it? How does it capture the meaning of the text?
We used the paraphrase-multilingual-MiniLM-L12-v2 model from sentence-transformers. It supports multiple languages, including Bengali and English, allowing us to embed queries and document chunks into a shared semantic space. It's lightweight and fast, suitable for moderate-sized corpora. 
The model captures contextual and semantic meaning beyond surface word matching by encoding sentences into dense vectors that reflect their overall meaning, allowing cross-lingual semantic search.

4. How are you comparing the query with your stored chunks? Why did you choose this similarity method and storage setup?
We compute cosine similarity between the embedded query vector and stored chunk embeddings using FAISS, a fast approximate nearest neighbor search library optimized for high-dimensional vectors. 
FAISS allows efficient real-time similarity search over large vector datasets. Cosine similarity is a standard measure for semantic closeness in embedding spaces. This setup balances speed and accuracy, enabling scalable retrieval with minimal latency.

5. How do you ensure that the question and the document chunks are compared meaningfully? What would happen if the query is vague or missing context?
By using a multilingual embedding model, both Bengali and English queries are embedded in the same semantic space as the chunks, allowing meaningful comparisons despite language differences. We also implement a fallback translation mechanism: if no relevant chunks are found, the query is translated (e.g., Bengali to English) and searched again, improving robustness to vague or out-of-domain queries. 
However, vague queries may still return less precise results because embeddings rely on semantic cues; more context or clearer questions yield better retrieval.

6. Do the results seem relevant? If not, what might improve them (e.g., better chunking, better embedding model, larger document)?
Overall, results are relevant and grounded in the document corpus. Potential improvements include:
Better chunking: Using semantic or paragraph boundary chunking rather than fixed word counts could improve coherence.
More powerful embeddings: Larger models or domain-finetuned embeddings might capture nuances better.
Expanded corpus: Incorporating more documents or external knowledge could enhance coverage.
Context-aware reranking: Using a reranker model to reorder retrieved chunks could improve answer quality.


### Installation

```bash
git clone <repo_url>
cd MultilingualRAGSystem
pip install -r requirements.txt

