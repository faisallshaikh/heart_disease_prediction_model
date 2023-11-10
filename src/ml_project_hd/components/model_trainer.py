import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass 
from src.exception import CustomException
from src.logger import logging 
import pickle
from sklearn.linear_model import LogisticRegression # Despite the name its an classification model
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier,HistGradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from src.utils import evaluate_models
from sklearn.metrics import r2_score,confusion_matrix,classification_report
from src.utils import save_object
import matplotlib.pyplot as plt
import seaborn as sns


@dataclass 
class ModelTrainingConfig:
    trained_model_path : str = os.path.join("Dataset", "model.pkl") 

class ModelTraining:
    def __init__(self):
        self.model_train = ModelTrainingConfig()

    def initiate_model_training(self,train_data,test_data):
        logging.info("Initiating Model Training")
        try : 

            X_train,y_train,X_test,y_test=(
                train_data[:,:-1],
                train_data[:,-1],
                test_data[:,:-1],
                test_data[:,-1] )

            classification_models = {
                "RandomForestClassifier" : RandomForestClassifier(),
                "KNeighborsClassifier" : KNeighborsClassifier(),
                # "LogisticRegression" : LogisticRegression(),
                "SVC" : SVC(),
                "GradientBoostingClassifier" : GradientBoostingClassifier()
                # "HistGradientBoostingClassifier" : HistGradientBoostingClassifier()

            }

            params = {
            "RandomForestClassifier" : {"n_estimators" : np.arange(100,510,100),
                                        "max_features" : ['sqrt']},

                                    
                "KNeighborsClassifier" : { 'n_neighbors' : [5,7,9,11,13,15],
                'weights' : ['uniform','distance'],
                #    'metric' : ['minkowski','euclidean','manhattan']
                },

                # "LogisticRegression" : {
                #     # 'penalty' : ['l2'],
                #     'C' : np.logspace(-4, 4, 20),
                #     # 'solver' : ['liblinear','saga'],
                #     'max_iter' : np.arange(100,500,100)
                # },

                "SVC" : {'C': [0.1, 1, 10, 100],
                                'gamma': [0.1, 0.01, 0.001],
                                'kernel': ['rbf','linear']},

                "GradientBoostingClassifier" : {'loss': ['log_loss', 'exponential'],
                                'learning_rate': [0.001, 0.1],
                                'n_estimators': [100, 150, 180]}

            }


            # lets create a function to evaluate all these models and its parameters
            # refer utils.py

            report = evaluate_models(X_train=X_train,
                                     X_test=X_test,
                                     y_train=y_train,y_test=y_test,
                                     classification_models=classification_models,
                                     params=params)
            
            print(report)
            logging.info(f"Report Col {report}")
            
            best_model_score = max(report.values())

            best_model_name = ""

            for key in report:
                if report[key] == max(report.values()):
                    best_model_name += key

            print(f"{best_model_name} has the highest score : {best_model_score}")

            best_model = classification_models[best_model_name]

            logging.info(f"Best Model Found {best_model}")

            model_names = list(params.keys())

            actual_model = ""
            for name in model_names:
                if best_model_name == name:
                    actual_model += best_model_name

            best_params = params[actual_model]

            print(best_params)

            save_object(
                file_path=self.model_train.trained_model_path,
                obj=best_model
            )

            predicted = best_model.predict(X_test)

            confuse = confusion_matrix(y_test,predicted)
            fig , ax = plt.subplots(figsize=(3,3))
            sns.heatmap(confuse, annot=True)
            plt.show()
            

            final_report = classification_report(y_test,predicted)
            
            r2 = r2_score(y_test,predicted)

            print(final_report)

            return r2 , final_report

        except Exception as e :
            raise CustomException(e,sys)

