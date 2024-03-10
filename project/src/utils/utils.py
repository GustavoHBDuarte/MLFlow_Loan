import os
import yaml


def load_config_file():
    """
    Essa função load_config_file() tem como objetivo abstrair o conjunto de comandos abaixo, necessários para 
    carregar o arquivo de configurações yaml.
    Uma vez que será necessário carregar esse arquivo ao longo de diferentes scripts desse projeto é mais conveniente
    executar a função que invoca esse arquivo ao invés de inserir explicitamente as linhas de código abaixo, tornando
    os códigos do projeto mais limpo
    """
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    
    caminho_relativo = os.path.join('..','..','config','config.yaml')
    
    config_file_path = os.path.abspath(os.path.join(diretorio_atual, caminho_relativo))
    
    config_file = yaml.safe_load(open(config_file_path, 'rb'))
    
    return config_file
