import os
import sys
import joblib
from utils.utils import get_model_path


import pandas as pd
import structlog

# voltar ao diretório /src para poder importar o módulo utils
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

# importar yaml de configuração
from utils.utils import load_config_file 

# Obtendo o objecto logger da biblioteca structlog
logger = structlog.getLogger()



class ModelTraining:
    """
    """

    def __init__(self, X: pd.DataFrame, y: pd.Series):
        """
        """
        self.X = X
        self.y = y
        self.model_name = load_config_file().get('model_name')

    def fit(self, model_instance):
        """
        """
        model_instance.fit(self.X, self.y)
        joblib.dump(model_instance, get_model_path(self.model_name)+'.joblib')
        print(get_model_path(self.model_name)+'.joblib')
        return model_instance

