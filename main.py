from src.exception import CustomException
from src.logger import logging
import sys 
import os
from src.ml_project_hd.components.data_ingestion import DataIngestion
from src.ml_project_hd.components.data_transform import DataTransformation
from src.ml_project_hd.components.model_trainer import ModelTraining
from src.ml_project_hd.pipeline.predicting_pipeline import CustomData,PredictPipeline

if __name__ == '__main__':
    try:
        
        data_ingestion_obj = DataIngestion()
        # returning three paths to initiate_data_ingestion(), thus accessing the last path
        train_data,test_data,raw_data = data_ingestion_obj.initiate_data_ingestion()

        ini_data_transform = DataTransformation()
        transform_train_data,transform_test_data,_ = ini_data_transform.initiate_data_tranform(raw_data)

        model_training_object = ModelTraining()
        model_training_object.initiate_model_training(transform_train_data,transform_test_data)

        
        data = CustomData()
        df_to_be_predicted = data.get_data_as_df()
        
        data_pipeline = PredictPipeline()
        data_pipeline.predicting(df_to_be_predicted)

    except Exception as e :
        raise CustomException(e ,sys)
