from ml_project.config.configuration import ConfigurationManager
from ml_project.components.model_trainer import ModelTrainer
from ml_project import logger
from pathlib import Path

STAGE_NAME = "Model Trainer Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            Model_trainer = ModelTrainer(config=model_trainer_config)
            Model_trainer.train()
            
        except Exception as e:
            print(e)