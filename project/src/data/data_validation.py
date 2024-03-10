import os
import sys

import pandas as pd
from pandera import Check, Column, DataFrameSchema
import structlog


# voltar ao diretório /src para poder importar o módulo utils
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

# importar yaml de configuração
from utils.utils import load_config_file 

# Obtendo o objecto logger da biblioteca structlog
logger = structlog.getLogger()




class DataValidation:
    """Class responsible for validating data input"""

    def __init__(self) -> None:
        
        # Loading yaml config file
        yaml_file = load_config_file()

        # getting columns to use in project from yaml config file
        self.columns_to_use = yaml_file.get('columns_to_use')

    def check_data_shape(self, dataframe: pd.DataFrame) -> bool:
        """Method responsible for data shape checking"""

        logger.info('Starting data shape checking')


        try: #tentar o código abaixo: check do shape das colunas à usar (passada no construtor) com as colunas do DataFrame
            logger.info('Data shape validation started!')
            dataframe.columns = self.columns_to_use
            return True

        except Exception as e: # Se o shape não bater vai ter exceção
            logger.error(f'Error: Data shape validation failed:{e}')
            return False

    def check_columns(self, dataframe: pd.DataFrame) -> bool:
        """Method responsible for data columns data type checking.
        Each column must have its own data type format.
        """

        logger.info('Starting column types validation')

        schema = DataFrameSchema(
            {
                "target": Column(int, Check.isin([0,1]), Check(lambda x: x>0), coerce=True),
                "TaxaDeUtilizacaoDeLinhasNaoGarantidas": Column(float, nullable=True),
                "Idade": Column(int, nullable=True),
                "NumeroDeVezes30-59DiasAtrasoNaoPior": Column(int, nullable=True),
                "TaxaDeEndividamento": Column(float, nullable=True),
                "RendaMensal": Column(float, nullable=True),
                "NumeroDeLinhasDeCreditoEEmprestimosAbertos": Column(int, nullable=True),
                "NumeroDeVezes90DiasAtraso": Column(int, nullable=True),
                "NumeroDeEmprestimosOuLinhasImobiliarias": Column(int, nullable=True),
                "NumeroDeVezes60-89DiasAtrasoNaoPior": Column(int, nullable=True),
                "NumeroDeDependentes": Column(int, nullable=True)
            }
        )
    
        try:
            schema.validate(dataframe)
            logger.info('Column validation passed!')        
            return True

        except pandera.errors.SchemaErrors as exc:
            logger.error('Error: Column validation failed!')
            pandera.display(exc.failure_cases)        
        return False

    def run(self, dataframe: pd.DataFrame) -> bool:
        if self.check_data_shape(dataframe) and self.check_columns(dataframe):
            logger.info('Validation step concluded!')
            return True
        
        else:
            logger.error('Validation failed!')
            return False