import pandas as pd
import os

from src.ingestion.data_ingestion import DataIngestion
from src.preprocessing.preprocess import DataPreprocessing
from src.feature_engineering.feature_builder import FeatureBuilder
from src.segmentation.segmentation import SegmentationModel
from src.risk_model.risk_prediction import RiskModel
from src.recommendation.recommend_engine import RecommendEngine

from src.utils.logger import get_logger

logger = get_logger(__name__)


class BatchPredictionPipeline:

    def __init__(self, input_path, output_path="data/output/batch_results.csv"):
        self.input_path = input_path
        self.output_path = output_path

        self.segmentation_model_path = "data/models/segmentation.pkl"
        self.risk_model_path = "data/models/riskprediction.pkl"

    def run(self):
        logger.info("🚀 Starting Batch Prediction Pipeline...")

        # 1. Load Data
        ingestion = DataIngestion(self.input_path)
        df = ingestion.load()
        logger.info("📌 Input CSV Loaded.")

        # 2. Preprocess
        preprocess = DataPreprocessing()
        clean_df = preprocess.clean(df)
        logger.info("📌 Preprocessing Done.")

        # 3. Feature Engineering
        features = FeatureBuilder()
        feature_df = features.transform(clean_df)
        logger.info("📌 Feature Engineering Completed.")

        # 4. Predict Segments
        segmenter = SegmentationModel(self.segmentation_model_path)
        feature_df["segment"] = segmenter.predict(
            feature_df[["travel_frequency", "loyalty_score", "past_claims"]]
        )
        logger.info("📌 Customer Segments Assigned.")

        # 5. Predict Risk Score
        risk_model = RiskModel(self.risk_model_path)
        feature_df["risk_score_pred"] = risk_model.predict(
            feature_df[["age", "travel_frequency", "loyalty_score", "segment"]]
        )
        logger.info("📌 Risk Prediction Completed.")

        # 6. Recommend Plan
        recommender = RecommendEngine()
        feature_df["recommended_plan"] = feature_df["segment"].apply(recommender.recommend)
        logger.info("📌 Recommendation Completed.")

        # 7. Save Output
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        feature_df.to_csv(self.output_path, index=False)
        logger.info(f"📁 Batch Results Saved At: {self.output_path}")

        logger.info("🎉 Batch Prediction Pipeline Completed Successfully!")

        return feature_df


if __name__ == "__main__":
    pipeline = BatchPredictionPipeline("data/raw/travel_insurance_customers.csv")
    pipeline.run()
