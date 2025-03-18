from ml_project.config.configuration import ConfigurationManager
from ml_project.components.model_evaluation import ModelEvaluation
from ml_project import logger
from pathlib import Path

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            Model_evaluation = ModelEvaluation(config=model_evaluation_config)
            Model_evaluation.save_results()
            
        except Exception as e:
            print(e)