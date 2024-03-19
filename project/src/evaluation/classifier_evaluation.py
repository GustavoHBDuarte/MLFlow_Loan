import os
import sys

import pandas as pd
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold, cross_val_score
import structlog

# voltar ao diretório /src para poder importar o módulo utils
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

# importar yaml de configuração
from utils.utils import load_config_file 

# Obtendo o objecto logger da biblioteca structlog
logger = structlog.getLogger()




class ModelEvaluating:
    """
    """

    def __init__(self, fitted_model, X: pd.DataFrame, y, nsplits=load_config_file().get('stratified_k_folder_n_splits')):
        """
        Método construtor definido de forma a reunir as informações necessárias para os experimentos de 
        validação cruzada k-fold (modelo instanciado, X, y e qtde de splits)
        """
        
        self.fitted_model = fitted_model
        self.X = X
        self.y = y
        self.nsplits = nsplits


    def cross_val_evaluation(self):
        """
        Método destinado a realizar a validação cruzada k-fold stratificada retornando o resultado da métrica para
        cada fold aplicado.
        """
        logger.info('Cross validation started...')
        stratified_k_folder = StratifiedKFold(n_splits=self.nsplits,
                                              shuffle=True,
                                              random_state=load_config_file().get('random_state'))

        scores = cross_val_score(self.fitted_model,
                                 self.X,
                                 self.y,
                                 cv=stratified_k_folder,
                                 scoring=load_config_file().get('cross_val_scoring_metric'))

        logger.info(f'Fitted model: {self.fitted_model}')
        logger.info(f'Scoring metric: {load_config_file().get('cross_val_scoring_metric')}')
        logger.info('Cross validation finished successfully!')
        
        return scores

    def roc_auc_scorer(self, fitted_model, X: pd.DataFrame, y):
        """
        Método definido para cálculo do ROC AUC à partir de um modelo treinado, X e y fornecidos.
        """

        y_pred = fitted_model.predict_proba(X)[:,1]

        return roc_auc_score(y, y_pred)
    

    staticmethod
    def evaluate_predictions(self, y_true, y_predict_proba):
        """
        Método definido para cálculo do ROC AUC à partir de uma lista de y e y_proba fornecidos.
        """
        logger.info('Model validation started...')

        return roc_auc_score(y_true, y_predict_proba)