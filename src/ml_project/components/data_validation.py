import os
import pandas as pd
import urllib.request as request
import zipfile
from ml_project import logger   
from ml_project.utils.common import get_size
from ml_project.entity.config_entity import DataValidationConfig
from pathlib import Path

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_all_colummns(self) -> bool:
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            
            all_schema = self.config.all_schema.keys()
            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    break
                else:
                    validation_status = True
                    
            with open(self.config.STATUS_FILE, "w") as file:
                        file.write(f"Validation status: {validation_status}")
            
            return validation_status        
            
        except Exception as e:
            logger.exception(e)
            raise e