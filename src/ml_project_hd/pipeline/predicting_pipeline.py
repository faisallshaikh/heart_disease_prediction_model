from src.utils import load_object
import os
import sys 
from src.exception import CustomException
from src.logger import logging
import pandas as pd


class PredictPipeline:

    def predicting(self, features):
        try:
            model_path = os.path.join('Dataset', 'model.pkl')
            preprocessor_path = os.path.join('Dataset', 'preprocessor.pkl')

            model = load_object(model_path)
            preprocessor = load_object(preprocessor_path)

            scaled_data = preprocessor.transform(features)

            pred = model.predict(scaled_data)
            print(pred)
            return pred
        
        except Exception as e :
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self,  age , sex , cp , 
                 trestbps , chol , fbs , restecg , 
                 thalach , exang , oldpeak , slope , ca , thal):
        
        self.age = age
        self.sex =sex
        self.cp =cp
        self.trestbps =trestbps
        self.chol =chol
        self.fbs =fbs
        self.restecg = restecg
        self.thalach = thalach
        self.exang = exang
        self.oldpeak = oldpeak
        self.slope = slope
        self.ca = ca
        self.thal = thal
    
    def get_data_as_df(self):

        try:
            get_dictionary = {
                'age' : [self.age],  
                'sex':[self.sex],
                'cp':[self.cp],
                'trestbps':[self.trestbps],
                'chol':[self.chol],
                'fbs':[self.fbs],
                'restecg' :[self.restecg],
                'thalach':[self.thalach],
                'exang' :[self.exang],
                'oldpeak' :[self.oldpeak],
                'slope' :[self.slope],
                'ca' :[self.ca],
                'thal': [self.thal]
            }

            return pd.DataFrame(get_dictionary)
        except Exception as e:
            raise CustomException(e,sys)

