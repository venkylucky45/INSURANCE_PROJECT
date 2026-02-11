from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel

from src.risk_model.risk_prediction import RiskModel

router = APIRouter()
risk_model = RiskModel("data/models/riskprediction.pkl")


class RiskRequest(BaseModel):
    age: int
    travel_frequency: float
    loyalty_score: float
    segment: int


@router.post("/predict")
def predict_risk(req: RiskRequest):
    df = pd.DataFrame([req.dict()])
    pred = risk_model.predict(df)
    return {"risk_score": float(pred[0])}
