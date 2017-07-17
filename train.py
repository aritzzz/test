"""
sarcasmproc.npy file loaded in this script contains clean tweets, stemmed as well. This script takes every tweet and append it to featuresets 
list. Also label( 1 for sarcastic tweet and 0 for regular tweet) is appended to labelset for every tweet. The featuresets list is then 
represented as Vector Space Model using sklearn.feature_extraction.text CountVectorizer class whose parameters ngram_range
and stop_words do the necessary work.
"""

import numpy as np
#import vectorize
from sklearn.feature_extraction.text import CountVectorizer



print 'loading data'

pos_data = np.load('sarcasmproc.npy')
#neg_data = np.load('regularproc.npy')

print 'no. of sarcastic tweets :', len(pos_data)
#print no.of regular tweets


featuresets = []
labelset = []

for tweet in pos_data:
    featuresets.append(tweet)
    labelset.append(1)

featuresets = np.array(featuresets)
labelset = np.array(labelset)

#print featuresets
#print labelset

vectorizer = CountVectorizer(ngram_range=(1,2),stop_words = 'english', analyzer = 'word')
X = vectorizer.fit_transform(featuresets)
