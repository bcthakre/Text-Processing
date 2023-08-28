import unicodedata
import string
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download content for lemmenization

import nltk
nltk.download('wordnet')
nltk.download('punkt')


class TextProcessor:

    def __init__(self):
        """
        Initialize TextProcessor with a lemmatizer and a stemmer
    
        """

        self.lemmatizer = WordNetLemmatizer()
        self.stemmer = PorterStemmer()


    def strip_accents(self,text):
        """
        Strip accents from input String.

        Args:
        - text (str) : Input text

        Returns:
        - str: Text without accents

        """
        print("Stripping accents...")
        return ''.join(c for c in unicodedata.normalize('NFD', text)
            if unicodedata.category(c) != 'Mn')
    
    def preprocess(self,sentence):
        """
        Process a list of sentences sequentially with the following steps

        1. Lowering
        2. Punctuation Removal
        3. Trim Whitespaces
        4. NFKD normlaization
        5. Strip accents
        6. Lemmatization
        7. Steming

        Args:
        - sentence (str) : List of sentecnes to process

        Returns:

        -list : Proceesed Sentecnes
        
        """

        processed_sentences = []

        for sentence in sentences:
            print("/nProcessing sentence: ", sentence)

            #1. Lowering

            print("Lowering...")
            sentence = sentence.lower()

            #2. Punctuation Removal
            print("Removing punctuation...")
            sentence = sentence.translate(str.maketrans('', '', string.punctuation))

            #3. Trim whitespaces
            print("Trimming whitespaces...")
            sentence = sentence.strip()

            #4. NFKD normalization
            print("Applying NFKD Normalizing...")
            sentence = unicodedata.normalize('NFKD',sentence)

            #5. Strip accents
            print("Stripping accents...")
            sentence = self.strip_accents(sentence)

            #6 Lemmatization
            print("Lemmatizing...")
            words = word_tokenize(sentence)
            sentence = ' '.join([self.lemmatizer.lemmatize(word) for word in words])

            #7. Stemming
            print("Stemming...")
            words = word_tokenize(sentence)
            sentence = ' '.join([self.stemmer.stem(word) for word in words])

            processed_sentences.append(sentence)

        return processed_sentences
    
if __name__ == "__main__":
    # Famous sentences from literature and historical figures
    
# Famouse sentences from literature and historical figures

    sentences = [
                "To be or not to be, that is the question.",  # William Shakespeare
                "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.",  # Jane Austen
                "All that glitters is not gold.",  # William Shakespeare
                "That's one small step for man, one giant leap for mankind.",  # Neil Armstrong
                "The only thing we have to fear is fear itself.",  # Franklin D. Roosevelt
                "I think, therefore I am.",  # René Descartes
                "In the beginning was the Word, and the Word was with God, and the Word was God.",  # The Bible
                "It was the best of times, it was the worst of times.",  # Charles Dickens
                "The future belongs to those who believe in the beauty of their dreams."  # Eleanor Roosevelt
                ]
    
    preprocessor = TextProcessor()

    processed_sentences = preprocessor.preprocess(sentences)

    for s in processed_sentences:
        print("\nProcessed sentence: ", s)