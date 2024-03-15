from mlProject.configsrc.configuration import ConfigurationManager
from mlProject.components.model_trainer import ModelTrainer
from mlProject import logger
from pathlib import Path


STAGE_NAME = "Model Training stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
            config = ConfigurationManager().get_model_trainer_config()
            model_trainer = ModelTrainer(config)
            model_trainer.train()
            logger.info("Model trained successfully")
            
            
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
           