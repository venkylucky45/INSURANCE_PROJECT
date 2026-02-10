# from fastapi import APIRouter
# import pandas as pd
# from pydantic import BaseModel

# from src.segmentation.segmentation import SegmentationModel

# router = APIRouter()

# segmenter = SegmentationModel("data/models/segmentation.pkl")


# class SegmentRequest(BaseModel):
#     travel_frequency: float
#     loyalty_score: float
#     past_claims: float


# @router.post("/predict")
# def segment_customer(request: SegmentRequest):
#     df = pd.DataFrame([request.dict()])
#     prediction = segmenter.predict(df)
#     return {
#         "segment": int(prediction[0]),
#         "message": "Customer segmented successfully."
#     }
