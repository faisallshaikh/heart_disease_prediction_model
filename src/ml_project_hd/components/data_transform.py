import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass 
from src.exception import CustomException
from src.logger import logging 
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder,StandardScaler
from sklearn.model_selection import train_test_split
import pickle
from src.utils import save_object


@dataclass 
class DataTransformationConfig:
    """Creating Transformation object so that we can transform the input which is to be predicted"""
    # creating a path for the transformation object to save
    preprocessor_object_path : str = os.path.join("Dataset", "preprocessor.pkl")

class DataTransformation:
    """Creating the object of or initiating the DataTransformationConfig"""
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_preprocessor_object(self):
        """PUTTING IT ALL TOGETHER... Creating a Pipeline"""
        """Here we will transform our data like, Filing the missing values using 
        SimpleImputer and Converting our categorical features into numerical features
        using OneHotEncoder or OrdinalEncoder and then we use ColumnTransformer to 
        fit and transform our train_data and transform our test_data"""
        try : 
            # categorical_features = []   # categorical_column_names
            # categorical_imputer = Pipeline(steps=[
            #     ("numerical_imputer", SimpleImputer(strategy="most_frequent")),
            #     ("one_hot", OneHotEncoder())
            # ])

            numerical_features = [] # numerical columns which are missing values
            numerical_imputer = Pipeline(steps=[
                ("numerical_imputer", SimpleImputer(strategy="median")),
                ("Standard_Scaler", StandardScaler() )
            ])

            preprocessor = ColumnTransformer(transformers=[
                # ("categorical_imputer", categorical_imputer,categorical_features),
                ("numerical_imputer", numerical_imputer,numerical_features)
            ],remainder="passthrough")

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_tranform(self,df_data_path):
        # Transforming train_data and test_data
        try:
            df = pd.read_csv(df_data_path)

            X = df.drop("target",axis = 1)
            y = df["target"]

            preprocessor_object = self.get_preprocessor_object()

            X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
            transformed_X_train = preprocessor_object.fit_transform(X_train)
            transformed_X_test = preprocessor_object.transform(X_test)

            """np.c_ (Concatinating)"""
            transformed_train_data = np.c_[transformed_X_train, y_train]
            transformed_test_data = np.c_[transformed_X_test,y_test]

            """saving the preprocessor pickle object"""
            save_object(
                file_path=self.data_transformation_config.preprocessor_object_path,
                obj=preprocessor_object
            )

            return (
                transformed_train_data,
                transformed_test_data,
                self.data_transformation_config.preprocessor_object_path
            )
        
        except Exception as e:
            raise CustomException(e,sys)
        






