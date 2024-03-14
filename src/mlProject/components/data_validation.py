import os
from mlProject import logger
from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_all_columns(self) -> bool:
        
        try:
            validation_status = None
            
            data = pd.read_csv(self.config.unzip_data_dir)
            all_columns = list(data.columns)
            schema_columns = self.config.all_schema.keys()
            
            for column in all_columns:
                if column not in schema_columns:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as file:
                        file.write(f"Validation status: {validation_status} \n")
                    break
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, "w") as file:
                        file.write(f"Validation status: {validation_status} \n")
            
            return validation_status
        
        except Exception as e:
            raise e