# from fastapi import APIRouter
# import pandas as pd
# from pydantic import BaseModel

# from src.risk_model.risk_prediction import RiskModel

# router = APIRouter()

# risk_model = RiskModel("data/models/risk.pkl")


# class RiskRequest(BaseModel):
#     age: int
#     travel_frequency: float
#     loyalty_score: float
#     segment: int


# @router.post("/predict")
# def predict_risk(request: RiskRequest):
#     df = pd.DataFrame([request.dict()])
#     prediction = risk_model.predict(df)
#     return {
#         "risk_score": float(prediction[0]),
#         "message": "Risk predicted successfully."
#     }
