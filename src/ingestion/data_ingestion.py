import pandas as pd
from src.utils.logger import get_logger
from src.utils.exception import ProjectException

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self, path):
        self.path = path

    def load(self):
        try:
            df = pd.read_csv(self.path)
            logger.info("Data loaded successfully.")
            return df
        except Exception as e:
            raise ProjectException(f"Failed to load data: {e}")
