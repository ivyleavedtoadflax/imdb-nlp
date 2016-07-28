# coding: utf-8
import pandas as pd
train = pd.read_csv('data/labeledTrainData.tsv',header=0,delimiter="\t",quoting=3)
train
train.shape
train.columns.values
print(train['review'])
print(train['review'][0])
from bs4 import BeautifulSoup
example1 = BeautifulSoup(train['review'][0])
print(train['review'][0])
print(example1.get_text())
import re

letters_only = re.sub("[^a-zA-Z]", " ", example1.get_text() )

letters_only
print(letters_only)
lower_case = letters_only.lower()
words = lower_case.split()
words

import nltk
from nltk.corpus import stopwords
print(stopwords.words('english'))
words = [w for w in words if not w in stopwords.words('english')]
words

def review_to_words( raw_review ):
        # Function to convert a raw review to a string of words
        # The input is a single string (a raw movie review), and 
        # the output is a single string (a preprocessed movie review)
        #
        # 1. Remove HTML
        review_text = BeautifulSoup(raw_review).get_text() 
        #
        # 2. Remove non-letters        
        letters_only = re.sub("[^a-zA-Z]", " ", review_text) 
        #
        # 3. Convert to lower case, split into individual words
        words = letters_only.lower().split()                             
        #
        # 4. In Python, searching a set is much faster than searching
        #   a list, so convert the stop words to a set
        stops = set(stopwords.words("english"))                  
        # 
        # 5. Remove stop words
        meaningful_words = [w for w in words if not w in stops]   
        #
        # 6. Join the words back into one string separated by space, 
        # and return the result.
        return( " ".join( meaningful_words ))
clean_review = review_to_words(train['review'][0])
print(clean_review)

num_reviews = train['review'].size
num_reviews
clean_train_reviews = []
    
for i in range(0, num_reviews):
    clean_train_reviews.append( review_to_words( train['review'][i] ) )
    
print('# https://www.kaggle.com/c/word2vec-nlp-tutorial/details/part-1-for-beginners-bag-of-words')

