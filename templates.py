import os
import sys
from pathlib import Path



list_of_files = [
    "\\src\\__init__.py",
    "\\src\\ml_project_hd\\__init__.py",
    "\\src\\ml_project_hd\\components\\__init__.py",
    "\\src\\ml_project_hd\\components\\data_ingestion.py",
    "\\src\\ml_project_hd\\components\\data_transform.py",
    "\\src\\ml_project_hd\\components\\model_trainer.py",
    "\\src\\ml_project_hd\\pipeline\\__init__.py",
    "\\src\\ml_project_hd\\pipeline\\predicting_pipeline.py",
    "\\src\\exception.py",
    "\\src\\logger.py",
    "\\src\\utils.py",
    "\\setup.py",
    "\\src\\notebooks\\code_1.ipynb",
    "\\requirements.txt"   
]

path_dir = os.getcwd()
# print(path_dir)i

for file in list_of_files:

    file_path = path_dir + file
    whole_path = Path(file_path)
    dir_path , file_name = os.path.split(whole_path)

    os.makedirs(dir_path,exist_ok=True)

    if os.path.exists(file_path):
        print(f"Alreadt Exist {file_name}")

    if (not os.path.exists(file_path)):
        with open(file_path, 'w') as f:
            pass




