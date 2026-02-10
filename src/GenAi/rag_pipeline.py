class RAGPipeline:
    def __init__(self, retriever, llm):
        self.retriever = retriever
        self.llm = llm

    def run(self, query):
        docs = self.retriever.get_relevant_documents(query)

        context = "\n".join([d.page_content for d in docs])

        final_prompt = f"""
Use ONLY the context below to answer the question.

Context:
{context}

Question:
{query}

Answer:
"""

        response = self.llm.invoke(final_prompt)
        return response.content
