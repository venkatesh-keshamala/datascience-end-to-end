from src.datascience.config.configuaration import ConfiguarationManager
from src.datascience.components.model_trainer import ModelTrainer
from src.datascience import logger


STAGE_NAME = 'Model Trainer Stage'

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfiguarationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()