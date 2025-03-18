from ml_project import logger
from ml_project.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from ml_project.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from ml_project.pipeline.stage03_data_transformation import DatatransformationTrainingPipeline
from ml_project.pipeline.stage04_model_trainer import ModelTrainerTrainingPipeline
from ml_project.pipeline.stage05_model_evaluation import ModelEvaluationTrainingPipeline

logger.info("Sairam please bless me")

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f">>>>>>> {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Validation Stage'

try:
    logger.info(f">>>>>>> {STAGE_NAME} started <<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>> {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Transformation Stage'

try:
    logger.info(f">>>>>>> {STAGE_NAME} started <<<<<<<")
    data_transformation = DatatransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>> {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Model trainer Stage'

try:
    logger.info(f">>>>>>> {STAGE_NAME} started <<<<<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>>>> {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Model Evaluation Stage'

try:
    logger.info(f">>>>>>> {STAGE_NAME} started <<<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>> {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
    