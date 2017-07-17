"""
the tweets are saved in sarcasmproc file, load that file and for every entry in that
do feature extraction. The script would return the feature dictionary for every tweet
and the aim of this script is get features for the entire dataset.
"""

import numpy as np
import vectorize

print 'loading data'

pos_data = np.load('sarcasmproc.npy')
#neg_data = np.load('regularproc.npy')

print 'no. of sarcastic tweets :', len(pos_data)
#print no.of regular tweets

cls_set = ['Regular', 'Sarcastic']
featuresets = []

for tweet in pos_data:
    featuresets.append((vectorize.features(tweet),cls_set[1]))

featuresets = np.array(featuresets)

print featuresets
