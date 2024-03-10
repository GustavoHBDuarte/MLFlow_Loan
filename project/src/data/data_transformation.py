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
        
        # Loading yaml config file
        yaml_file = load_config_file()
        
        self.dataframe = dataframe
        self.target_variable = yaml_file.get('target_variable')

    def train_test_data_split(self):

        # Loading yaml config file
        yaml_file = load_config_file()

        X = self.dataframe.drop(columns=[self.target_variable])
        y = self.dataframe[self.target_variable]

        X_train, X_val, y_train, y_val = train_test_split(X,
                                                          y,
                                                          stratify=y,
                                                          test_size=yaml_file.get('test_size'),
                                                          random_state=yaml_file.get('random_state')
                                                          )

        return X_train, X_val, y_train, y_val 