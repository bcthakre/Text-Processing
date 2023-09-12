# Purpose: Sentiment Analysis using Hugging Face
# Author: Bhupendrasinh Thakre

# import libraries

import pandas as pd
from transformers import pipeline
from kaggle.api.kaggle_api_extended import KaggleApi
import os

# to see long review sentences

pd.set_option('display.max_colwidth', None)

# Initialize Kaggle API

api = KaggleApi()
api.authenticate()

# downalod the hotel review dataset

hotel_review = api.dataset_download_files('juhibhojani/hotel-reviews',path='.',unzip=True)

# download the Named Entity Recognition (NER) Corpus

ner_corpus = api.dataset_download_files('naseralqaydeh/named-entity-recognition-ner-corpus',path='.',unzip=True)

# read the hotel review csv file

hotel_review = pd.read_csv('Hotel_Reviews.csv')

# read the ner corpus csv file

ner_corpus = pd.read_csv('ner.csv',encoding='latin1')

# check the data and replace NAs in the Review_Text column with empty string

hotel_review['Review_Text'].fillna("",inplace=True)
ner_corpus['Sentence'].fillna("",inplace=True)

# sentiment Analysis

sentiment_pipeline = pipeline("sentiment-analysis",model="siebert/sentiment-roberta-large-english")

# topic classification

topic_pipeline = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment")

# apply the pipeline on the Review_Text column

hotel_review['sentiment'] = hotel_review['Review_Text'].apply(lambda x: sentiment_pipeline(x)[0]['label'])
hotel_review['sentiment_score'] = hotel_review['Review_Text'].apply(lambda x: sentiment_pipeline(x)[0]['score'])

# apply the pipeline on the Sentence column

ner_corpus['topic'] = ner_corpus['Review_Text'].apply(lambda x: topic_pipeline(x)[0]['label'])


# import libraries

from pybtex.database.input import bibtex

# Load the BibTeX file
parser = bibtex.Parser()
bibdata = parser.parse_file("references.bib")

# print(bibdata.entries)
def format_citation(key):
    entry = bibdata.entries[key]
    
    # Extracting authors
    authors = " and ".join([" ".join(author.first_names + author.middle_names + author.last_names) for author in entry.persons['author']])
    
    return f"{authors} ({entry.fields['year']}). {entry.fields['title']}."

# print the citation

print(format_citation("antypas-etal-2022-twitter"))
