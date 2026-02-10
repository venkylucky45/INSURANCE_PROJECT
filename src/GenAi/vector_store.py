from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
load_dotenv()

class VectorStore:
    def __init__(self, index_name="insurance-index", dim=768):
        self.pc = Pinecone()

        # create index if not exists
        if index_name not in [idx["name"] for idx in self.pc.list_indexes()]:
            self.pc.create_index(
                name=index_name,
                dimension=dim,              # embedding dimension (768 for Ollama)
                metric="cosine",
                spec=ServerlessSpec(
                    cloud="aws",
                    region="us-east-1"
                )
            )

        self.index = self.pc.Index(index_name)

    def insert(self, vectors, chunks):
        payload = []
        for i, (vec, chunk) in enumerate(zip(vectors, chunks)):
            payload.append({
                "id": str(i),
                "values": vec,
                "metadata": {
                    "source": chunk["source"],
                    "text": chunk["text"]
                }
            })

        self.index.upsert(payload)
        return True

    def search(self, vector, top_k=5):
        result = self.index.query(
            vector=vector,
            top_k=top_k,
            include_metadata=True
        )
        return result
