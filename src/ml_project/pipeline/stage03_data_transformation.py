from ml_project.config.configuration import ConfigurationManager
from ml_project.components.data_transformation import DataTransformation
from ml_project import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DatatransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), 'r') as f:
                status = f.read().split(':')[-1]
                
            if status:
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                logger.info(f"Data validation NOK so transformation not triggered")
            
        except Exception as e:
            print(e)