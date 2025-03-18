from sklearn.model_selection import train_test_split
import os
import pandas as pd
import urllib.request as request
import zipfile
from ml_project import logger   
from ml_project.utils.common import get_size
from ml_project.entity.config_entity import DataTransformationConfig
from pathlib import Path

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    def train_test_splitting(self) -> bool:
        data = pd.read_csv(self.config.data_path)
        
        train, test = train_test_split(data)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        
        logger.info(f"Splitted the data in train & test")
        logger.info(f"Train shape: {train.shape}")
        logger.info(f"Test shape: {test.shape}")