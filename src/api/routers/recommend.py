from fastapi import APIRouter
from pydantic import BaseModel

from src.recommendation.recommend_engine import RecommendEngine

router = APIRouter()
recommender = RecommendEngine()


class RecommendRequest(BaseModel):
    segment: int


@router.post("/plan")
def recommend_plan(req: RecommendRequest):
    plan = recommender.recommend(req.segment)
    return {"recommended_plan": plan}
