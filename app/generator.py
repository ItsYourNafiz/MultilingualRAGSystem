from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def generate_answer(query, context):
    prompt = f"""You are a helpful assistant fluent in Bengali and English.

Context:
{context}

Question:
{query}

Answer:"""

    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "https://your-site.com",
            "X-Title": "Bilingual RAG System",
        },
        model="deepseek/deepseek-r1:free",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message.content
