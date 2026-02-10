from langchain_ollama.embeddings import OllamaEmbeddings

class Embedder:
    def __init__(self, model="nomic-embed-text"):
        self.client = OllamaEmbeddings(model=model)

    # Single query embedding
    def embed(self, text: str):
        return self.client.embed_query(text)

    # Embed all chunks
    def embed_many(self, chunks: list):
        texts = [c["text"] for c in chunks]
        return self.client.embed_documents(texts)
