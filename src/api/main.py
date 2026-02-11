from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routers.segment import router as segment_router
from src.api.routers.risk import router as risk_router
from src.api.routers.recommend import router as recommend_router
from src.api.routers.genai import router as genai_router

app = FastAPI(
    title="Travel Insurance Intelligence System",
    version="1.0.0",
    description="Segmentation, Risk ML, Recommendation and GenAI RAG Pipeline"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROUTERS
app.include_router(segment_router, prefix="/segmentation", tags=["Segmentation"])
app.include_router(risk_router, prefix="/risk", tags=["Risk Prediction"])
app.include_router(recommend_router, prefix="/recommend", tags=["Recommendation"])
app.include_router(genai_router, prefix="/genai", tags=["GenAI RAG"])


@app.get("/")
def home():
    return {"message": "Travel Insurance AI API is running"}

