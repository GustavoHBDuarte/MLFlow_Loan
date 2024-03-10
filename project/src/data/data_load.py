import os
import sys
import pandas as pd
import structlog

# Obtendo o objecto logger da biblioteca structlog
logger = structlog.getLogger()

# voltar ao diretório /src para poder importar o módulo utils
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))  

# importar yaml de configuração
from utils.utils import load_config_file 


class DataLoad:
    """Class responsible for data loading"""

    
    def __init__(self) -> None:
        pass

    def load_data(self, dataset_name: str) -> pd.DataFrame:
        """Method for data loading"""

        logger.info(f'Staring data loading with: {dataset_name}')
        
        # Loading yaml file
        yaml_file = load_config_file()
        
        
        try: # Verificar se o nome fornecido do dataset bate com o nome do arquivo yaml config:                   
                  
            # Getting dataset name from yaml file
            dataset = yaml_file.get(dataset_name)

            if dataset is None:

                raise ValueError(f'The dataset name provided is incorrect! Please provide the correct name: {dataset}')

        
        
            # Loading csv as dataframe
            df_loaded_data = pd.read_csv(f'../data/raw/{dataset}',
                                         index_col=[0],
                                         dtype={'target':pd.Int64Dtype(),
                                                'TaxaDeUtilizacaoDeLinhasNaoGarantidas':pd.Float64Dtype(),
                                                'Idade':pd.Int64Dtype(),
                                                'NumeroDeVezes30-59DiasAtrasoNaoPior':pd.Int64Dtype(),
                                                'TaxaDeEndividamento':pd.Float64Dtype(),
                                                'RendaMensal':pd.Float64Dtype(),
                                                'NumeroDeLinhasDeCreditoEEmprestimosAbertos':pd.Int64Dtype(),
                                                'NumeroDeVezes90DiasAtraso':pd.Int64Dtype(),
                                                'NumeroDeEmprestimosOuLinhasImobiliarias':pd.Int64Dtype(),
                                                'NumeroDeVezes60-89DiasAtrasoNaoPior':pd.Int64Dtype(),
                                                'NumeroDeDependentes':pd.Int64Dtype()})

            logger.info('Data loaded successfully!')
            
            return df_loaded_data[yaml_file.get('columns_to_use')]
        
        except ValueError as ve:
            logger.error(str(ve))

        except Exception as e:
            logger.error(f'Unexpected error: {str(ve)}')   


