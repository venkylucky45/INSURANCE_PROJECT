import glob
from langchain_community.document_loaders import PyPDFLoader

class DocumentLoader:
    def __init__(self, folder):
        self.folder = folder

    def load(self):
        docs = []
        for f in glob.glob(f"{self.folder}/*.pdf"):
            loaded_docs = PyPDFLoader(f).load()
            for doc in loaded_docs:
                docs.append({
                    "text": doc.page_content,
                    "source": doc.metadata.get("source", f)
                })
        return docs
