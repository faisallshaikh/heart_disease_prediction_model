# import logging 
# import os 
# import sys 
# from src.exception import CustomException
# from datetime import datetime 

# try:

#     log_file = f"{datetime.now().strftime('%Y %m %d %H %M %S')}.log"

#     file_path = os.path.join(os.getcwd(), "logs", log_file)

#     os.makedirs(file_path,exist_ok=True)

#     log_file_path = os.path.join(file_path, log_file)

#     logging.basicConfig(
#         filename=log_file_path,
#         level=logging.DEBUG,
#         format=('%(asctime)s %(name)s %(message)s')
#     )


# except Exception as e:
#     raise CustomException(e,sys)