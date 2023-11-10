import os
import sys
import pickle
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score


def save_object(file_path,obj):
    try: 

        os.makedirs(os.path.dirname(file_path),exist_ok=True)

        with open(file_path,'wb') as f:
            return pickle.dump(obj, f)
        
    except Exception as e:
        raise CustomException(e,sys)
    

def evaluate_models(X_train,X_test,y_train,y_test,classification_models,params):
    logging.info("Model Evaluation Started")
    try:

        report = {}
        train_data_report = {}

        for i in range(len(classification_models)):
            # Getting models
            model = list(classification_models.values())[i] # converting to list, otherwise wont be subscriptable
            param = params[list(classification_models.keys())[i]]
            """we will get the keys from classification_models and as the keys of params are 
            same, we will access the values of params using classification_models keys"""

            gs_model = GridSearchCV(model,
                                    param,
                                    cv = 3)
            
            gs_model.fit(X_train,y_train)
            
            model.set_params(**gs_model.best_params_)
            """gs_model.best_params_ will give us best parameters from the parameters (params) we provide """
            model.fit(X_train,y_train)

            model.score(X_test,y_test)

            X_train_preds = model.predict(X_train)

            X_test_preds = model.predict(X_test)

            X_train_preds_score = r2_score(y_train, X_train_preds)

            X_test_preds_score = r2_score(y_test, X_test_preds)

            """we will save model name as key and r2_score as value in dictionary"""

            train_data_report[list(classification_models.keys())[i]] = X_train_preds_score

            report[list(classification_models.keys())[i]] = X_test_preds_score

            logging.info("Report Collected")

        return report

    except Exception as e:
        raise CustomException(e,sys)
    

def load_object(file_path):
    try:

        with open(file_path, 'rb') as f:
            return pickle.load(f)

    except Exception as e:
        raise CustomException(e,sys)
    




