from ml_project.config.configuration import ConfigurationManager
from ml_project.components.data_validation import DataValidation
from ml_project import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_colummns()
            
        except Exception as e:
            print(e)