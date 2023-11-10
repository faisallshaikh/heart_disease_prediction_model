from setuptools import setup, find_packages
# from src.exception import CustomException
import os
import sys

HYPEN_DOT = "-e ."


def get_requirements(files):

    with open(files) as f:
        data = f.readlines()
        data = [i.replace("\n", "") for i in data]

        if HYPEN_DOT in data:
            data.remove(HYPEN_DOT)
    
    return (data)


setup(
    name = "ML_Project_hd",
    version= "0.0.1",
    author= "BOT",
    author_email= "phewpheww123@gmail.com",
    install_requires = get_requirements("requirements.txt"),
    packages=find_packages()

)
