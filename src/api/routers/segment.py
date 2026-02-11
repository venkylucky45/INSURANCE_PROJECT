from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel

from src.segmentation.segmentation import SegmentationModel

router = APIRouter()
segmenter = SegmentationModel("data/models/segmentation.pkl")


class SegmentRequest(BaseModel):
    travel_frequency: float
    loyalty_score: float
    past_claims: float


@router.post("/predict")
def segment_customer(req: SegmentRequest):
    df = pd.DataFrame([req.dict()])
    seg = segmenter.predict(df)
    return {"segment": int(seg[0])}
