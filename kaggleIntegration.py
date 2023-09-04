import pandas as pd
import os
from kaggle.api.kaggle_api_extended import KaggleApi

from textPreProcessing import TextProcessor

# to see long review sentences

pd.set_option('display.max_colwidth', None)

# intiate the method

proceesor = TextProcessor()

# Initialize Kaggle API

api = KaggleApi()
api.authenticate()

# list of license
# 'all', 'cc', 'gpl', 'odb', 'other'
# to see the list of datasets with license odb and max size of 4000

api.dataset_list(max_size=4000,license_name='odb')

# list of competitions

api.competitions_list()

# Fetch datasets

api.dataset_download_files('juhibhojani/hotel-reviews',path='.',unzip=True)

# load the dataset
# Number 10 below may be different for you
# check the file name in the folder

print(os.listdir('.'))

# read the csv file

file_name = os.listdir('.')[10] 
data = pd.read_csv(file_name)

# check the data

print(data.head())
