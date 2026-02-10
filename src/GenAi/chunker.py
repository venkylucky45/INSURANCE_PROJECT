class Chunker:
    def chunk(self, documents, size=400, overlap=50):
        chunks = []
        for doc in documents:
            text = doc["text"]
            source = doc["source"]

            for i in range(0, len(text), size - overlap):
                chunks.append({
                    "text": text[i:i+size],
                    "source": source
                })
        return chunks
