import os
import sys

import pandas as pd
import structlog
from sklearn.model_selection import train_test_split

# Obtendo o objecto logger da biblioteca structlog
logger = structlog.getLogger()

# voltar ao diretório /src para poder importar o módulo utils
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))  

# importar yaml de configuração
from utils.utils import load_config_file 



class DataTransformation:
    """
    Class responsible for data transformations.
    
    """

    def __init__(self, dataframe: pd.DataFrame):
        
        
        try:
            # Loading yaml config file
            yaml_file = load_config_file()

            if not yaml_file:
                raise ValueError('Failed do load YAM config file')
            
        except Exception as e:
            logger.error(f'Error loading config file: {e}')
            raise   
        
        self.dataframe = dataframe
        self.target_variable = yaml_file.get('target_variable')

    def train_test_data_split(self):

        try:
            # Loading yaml config file
            yaml_file = load_config_file()

            if not yaml_file:
                raise ValueError('Failed do load YAML config file')

        except Exception as e:
            logger.error(f'Error loading config file: {e}')
            raise


        try:
            # Check if target variable is present in the dataframe
            if self.target_variable not in self.dataframe.columns:
                raise ValueError(f"Target variable '{self.target_variable}' not found in the dataframe")

            logger.info(f"Target '{self.target_variable}' variable found in the dataframe. Performing X, y split and train/val split")
            
            X = self.dataframe.drop(columns=[self.target_variable])
            y = self.dataframe[self.target_variable]

            # Perform split
            X_train, X_val, y_train, y_val = train_test_split(X,
                                                              y,
                                                              stratify=y,
                                                              test_size=yaml_file.get('test_size'),
                                                              random_state=yaml_file.get('random_state')
                                                              )
            
            logger.info(f'Data split performed successfully!')

            

        except Exception as e:
            logger.error(f'Error during data split: {e}')
            raise

        return X_train, X_val, y_train, y_val 