from langchain_core.documents import Document

class PineconeRetriever:
    def __init__(self, vector_store, embedder, top_k=3):
        self.vector_store = vector_store     # Pinecone VectorStore object
        self.embedder = embedder             # Embedder (Ollama)
        self.top_k = top_k

    def get_relevant_documents(self, query):
        # 1. Convert query → embedding vector
        query_vector = self.embedder.embed(query)

        # 2. Search in Pinecone
        results = self.vector_store.search(query_vector, top_k=self.top_k)

        # 3. Convert Pinecone matches → LangChain Documents
        docs = []
        for match in results["matches"]:
            text = match["metadata"]["text"]
            source = match["metadata"]["source"]

            docs.append(
                Document(
                    page_content=text,
                    metadata={"source": source}
                )
            )

        return docs
