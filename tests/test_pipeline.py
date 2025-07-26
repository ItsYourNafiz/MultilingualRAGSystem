import unittest
from app.retriever import retrieve_similar_chunks
from app.generator import generate_answer

class TestRAGPipeline(unittest.TestCase):

    def test_retriever_returns_chunks(self):
        query = "রবীন্দ্রনাথের কবিতা"
        chunks = retrieve_similar_chunks(query, top_k=2)
        self.assertTrue(len(chunks) > 0)
        for chunk in chunks:
            self.assertIsInstance(chunk, str)

    def test_generator_returns_answer(self):
        query = "Who is Rabindranath Tagore?"
        context = "Rabindranath Tagore was a Bengali poet and philosopher."
        answer = generate_answer(query, context)
        self.assertIsInstance(answer, str)
        self.assertTrue(len(answer) > 0)

if __name__ == "__main__":
    unittest.main()
