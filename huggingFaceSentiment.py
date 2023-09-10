# Purpose: Sentiment Analysis using Hugging Face
# Author: Bhupendrasinh Thakre

# import libraries

import pandas as pd
from transformers import pipeline

# read the csv file

data = pd.read_csv('Hotel_Reviews.csv')

# check the data and replace NAs in the Review_Text column with empty string

data['Review_Text'].fillna("",inplace=True)

# sentiment Analysis

sentiment_pipeline = pipeline('sentiment-analysis')

# apply the pipeline on the Review_Text column

data['sentiment'] = data['Review_Text'].apply(lambda x: sentiment_pipeline(x)[0]['label'])
data['sentiment_score'] = data['Review_Text'].apply(lambda x: sentiment_pipeline(x)[0]['score'])

