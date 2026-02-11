from fastapi import APIRouter
from pydantic import BaseModel

from src.GenAi.document_loader import DocumentLoader
from src.GenAi.chunker import Chunker
from src.GenAi.embedder import Embedder
from src.GenAi.vector_store import VectorStore
from src.GenAi.retriever import PineconeRetriever
from src.GenAi.rag_pipeline import RAGPipeline

from langchain_ollama import ChatOllama

router = APIRouter()

# ------------------ LOAD DOCUMENTS ---------------------
loader = DocumentLoader("data/policy_docs")
docs = loader.load()

chunker = Chunker()
chunks = chunker.chunk(docs)

embedding = Embedder(model="nomic-embed-text")
vectors = embedding.embed_many(chunks)

vector_store = VectorStore(index_name="insurance-index", dim=len(vectors[0]))
vector_store.insert(vectors, chunks)

retriever = PineconeRetriever(vector_store, embedding, top_k=3)

llm = ChatOllama(model="gemma3:4b")

rag = RAGPipeline(retriever, llm)

# ------------------ API REQUEST MODEL ---------------------
class RAGRequest(BaseModel):
    question: str


@router.post("/ask")
def ask_question(req: RAGRequest):
    answer = rag.run(req.question)
    return {
        "query": req.question,
        "response": answer
    }
