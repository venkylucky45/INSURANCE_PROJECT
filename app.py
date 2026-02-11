from src.ingestion.data_ingestion import DataIngestion
from src.preprocessing.preprocess import DataPreprocessing
from src.feature_engineering.feature_builder import FeatureBuilder
from src.segmentation.segmentation import SegmentationModel
from src.risk_model.risk_prediction import RiskModel
from src.recommendation.recommend_engine import RecommendEngine
from src.GenAi.document_loader import DocumentLoader
from src.GenAi.chunker import Chunker
from src.GenAi.embedder import Embedder
from src.GenAi.vector_store import VectorStore
from src.GenAi.retriever import PineconeRetriever
from langchain_ollama import ChatOllama
from src.GenAi.rag_pipeline import RAGPipeline



ob = DataIngestion('data/raw/travel_insurance_customers.csv')
df = ob.load()

preprocess = DataPreprocessing()
clean_df = preprocess.clean(df)

feature = FeatureBuilder()
feature_df = feature.transform(clean_df)

segmenter = SegmentationModel('data/models/segmentation.pkl')

segmenter.train(feature_df)
segmenter.predict(feature_df[["travel_frequency", "loyalty_score", "past_claims"]])

risk = RiskModel('data/models/riskprediction.pkl')
risk.train(feature_df)
risk.predict(feature_df[["age", "travel_frequency", "loyalty_score", "segment"]])

recommend = RecommendEngine()
seg_val = feature_df.loc[0, "segment"]
recommend.recommend(seg_val)

document_loader = DocumentLoader("data/policy_docs")
docs = document_loader.load()

chunking = Chunker()
chunks = chunking.chunk(docs)

embedding = Embedder(model="nomic-embed-text")
vectors = embedding.embed_many(chunks)

print("Number of chunks:", len(chunks))
print("Number of embeddings:", len(vectors))
print("Embedding dimension:", len(vectors[0]))

store = VectorStore(index_name="insurance-index", dim=len(vectors[0]))
store.insert(vectors, chunks)

retriever = PineconeRetriever(store, embedding, top_k=3)

llm = ChatOllama(model="gemma3:4b")

rag = RAGPipeline(retriever, llm)

# Ask a question
query = "I don't travel frequently which plan is suitable for me"
answer = rag.run(query)

print("\n================ RAG Answer ================\n")
print(answer)

