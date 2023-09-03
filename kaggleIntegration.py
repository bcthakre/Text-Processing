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

# remove whitespaces

data['RemovedWhitespaces'] = data['Review_Text'].apply(proceesor.trim_whitespace)

# normalize text

data['NormalizedText'] = data['Review_Text'].apply(proceesor.normalize_text)

# lemmatize text

data['LemmatizedText'] = data['Review_Text'].apply(proceesor.lemmatize_text)

# stem text
# probably the most unuseful one for NLP

data['StemmedText'] = data['Review_Text'].apply(proceesor.stem_text)

# all of the methods above

data['AllPreProcessing'] = data['Review_Text'].apply(proceesor.preprocess)

# applying the Transofmrer and Sentimenal Analysis

from transformers import pipeline

# sentiment Analysis

sentiment_pipeline = pipeline('sentiment-analysis')

# apply the pipeline on the Review_Text column

data['sentiment'] = data['Review_Text'].apply(lambda x: sentiment_pipeline(x)[0]['label'])
data['sentiment_score'] = data['Review_Text'].apply(lambda x: sentiment_pipeline(x)[0]['score'])

