# from fastapi import APIRouter
# from pydantic import BaseModel

# from src.recommendation.recommend_engine import RecommendEngine

# router = APIRouter()

# recommender = RecommendEngine()


# class RecommendRequest(BaseModel):
#     segment: int


# @router.post("/plan")
# def recommend_plan(request: RecommendRequest):
#     plan = recommender.recommend(request.segment)
#     return {
#         "recommended_plan": plan,
#         "message": "Plan recommended successfully."
#     }
