from setuptools import setup
from typing import List

#you can ignore List[str]



#declaring variables for setup functions

PROJECT_NAME= "housing-predictor"
VERSION="0.0.1"
AUTHOR="Pruthvi Belgaonkar"
DESCRIPTION="This is a first FSDS Nov Batch Machine Learning Project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

##THIS FN IS GOING TO RETURN LIST OF REQUIREMENT MENTION IN REQUIREMENT.TXT
def get_requirements_list()->List[str]: 
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()
)