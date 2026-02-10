# from fastapi import APIRouter
# from pydantic import BaseModel

# from src.GenAi.document_loader import DocumentLoader
# from src.GenAi.chunker import Chunker
# from src.GenAi.embedder import Embedder
# from src.GenAi.vector_store import VectorStore
# from src.GenAi.retriever import PineconeRetriever
# from src.GenAi.rag_pipeline import RAGPipeline

# router = APIRouter()

# # ---------- Initialize RAG System ----------
# loader = DocumentLoader("policy_docs/")
# docs = loader.load()

# chunker = Chunker()
# chunks = chunker.chunk(docs)

# embedder = Embedder()
# vector_db = VectorStore()

# # Insert embeddings
# vectors = []
# for i, chunk in enumerate(chunks):
#     vectors.append({
#         "id": f"chunk_{i}",
#         "values": embedder.embed(chunk["text"]),
#         "metadata": {
#             "text": chunk["text"],
#             "source": chunk["source"]
#         }
#     })

# vector_db.insert(vectors)

# retriever = PineconeRetriever(vector_db, embedder)
# rag = RAGPipeline(retriever)


# class Query(BaseModel):
#     question: str


# @router.post("/ask")
# def genai_answer(q: Query):
#     answer = rag.run(q.question)
#     return {
#         "response": answer,
#         "message": "GenAI RAG response generated successfully."
#     }
