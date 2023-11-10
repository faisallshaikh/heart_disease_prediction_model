# Data Ingestion 

import os 
import sys
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
import pandas as pd
from sklearn.model_selection import train_test_split
from src.logger import logging

@dataclass 
class DataingestionConfiq:
    raw_data_path : str = os.path.join("Dataset", "raw_data.csv")
    train_data_path : str = os.path.join("Dataset", "train.csv")
    test_data_path : str = os.path.join("Dataset", "test.csv")


class DataIngestion:

    def __init__(self):
        
        try:
            self.data_ingestion_config = DataingestionConfiq()

        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_ingestion(self):
        logging.info("Data Initiating Started")
        try:
            path = r"D:\Faisal\telegram\Machine_Learning\11. Milestone Project 1 Supervised Learning - Part 01\6.1 heart-disease.csv"
            df = pd.read_csv(path)

            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path),exist_ok=True)

            df.to_csv(self.data_ingestion_config.raw_data_path,index=False,header=True)
            X_train, X_test = train_test_split(df,test_size=0.2,random_state=42)
            X_train.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)
            X_test.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)

            logging.info("Data Ingestion Completed")

            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path,
                self.data_ingestion_config.raw_data_path
            )
    
        except Exception as e:
            raise CustomException(e,sys) 




