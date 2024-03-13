import os
import sys

import pandas as pd
from sklearn.pipeline import Pipeline
import structlog


# voltar ao diretório /src para poder importar o módulo utils
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

# importar yaml de configuração
from utils.utils import load_config_file 

# Obtendo o objecto logger da biblioteca structlog
logger = structlog.getLogger()



class DataPreprocessing:

    def __init__(self, pipeline: Pipeline):
        """
        This constructor method is responsible for storing X_train and scikit-learn Pipeline object
        """
        logger.info('Pipeline started...')
        self.pipeline = pipeline
        self.fitted_pipeline = None


    def fit_pipeline(self, dataframe: pd.DataFrame):
        """
        This method is responsible for fitting the pipeline
        """

        logger.info('Pipeline fitting started...')
        self.fitted_pipeline = self.pipeline.fit(dataframe)
        logger.info('Pipeline fitting finished!')   

    
    def transform_pipeline(self, dataframe: pd.DataFrame):
        """
        This method is responsible for taking any fitted pipeline and transform data
        """
        if self.fitted_pipeline is None:
            raise ValueError('Pipeline not fitted. Fitting required!')
        
        logger.info('Data transformation with fitted pipeline started...')
        transformed_data = self.fitted_pipeline.transform(dataframe)
        logger.info('Data transformation with fitted pipeline finished!')

        return transformed_data


