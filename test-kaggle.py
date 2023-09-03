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

# Fetch datasets

api.dataset_download_files('juhibhojani/hotel-reviews',path='.',unzip=True)

# load the dataset

file_name = os.listdir('.')[5] 
data = pd.read_csv(file_name)

# Replace the NaN values with empty strings

data['Review_Text'].fillna("",inplace=True)

# Use the methods sequentially on the Review_Text column

# Lowering the sentences

data['LoweredSentence'] = data['Review_Text'].apply(proceesor.to_lower)

# strip accents

data['StripedAccents'] = data['Review_Text'].apply(proceesor.strip_accents)

# remove punctuation

data['RemovedPunctuation'] = data['Review_Text'].apply(proceesor.remove_punctuation)
