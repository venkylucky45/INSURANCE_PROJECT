import pandas as pd
from src.ingestion.data_ingestion import DataIngestion
from src.preprocessing.preprocess import DataPreprocessing
from src.feature_engineering.feature_builder import FeatureBuilder
from src.segmentation.segmentation import SegmentationModel
from src.risk_model.risk_prediction import RiskModel
from src.recommendation.recommend_engine import RecommendEngine
from src.utils.logger import get_logger

logger = get_logger(__name__)


class TrainingPipeline:

    def __init__(self):
        self.data_path = "data/raw/travel_insurance_customers.csv"
        self.segmentation_model_path = "data/models/segmentation.pkl"
        self.risk_model_path = "data/models/riskprediction.pkl"

    def run(self):
        logger.info("🚀 Starting Training Pipeline...")

        # 1. Load Data
        ingestion = DataIngestion(self.data_path)
        df = ingestion.load()
        logger.info("📌 Data Loaded Successfully.")

        # 2. Preprocess
        preprocess = DataPreprocessing()
        clean_df = preprocess.clean(df)
        logger.info("📌 Preprocessing Completed.")

        # 3. Feature Engineering
        features = FeatureBuilder()
        feature_df = features.transform(clean_df)
        logger.info("📌 Feature Engineering Completed.")

        # 4. Train Segmentation Model
        segmenter = SegmentationModel(self.segmentation_model_path)
        feature_df = segmenter.train(feature_df)
        logger.info("📌 Segmentation Model Trained & Saved.")

        # 5. Train Risk Model
        risk_model = RiskModel(self.risk_model_path)
        risk_model.train(feature_df)
        logger.info("📌 Risk Model Trained & Saved.")

        logger.info("🎉 Training Pipeline Completed Successfully!")
        return feature_df  # return processed data for further steps


if __name__ == "__main__":
    pipeline = TrainingPipeline()
    pipeline.run()
