#import alist from preproc.py. It returns list)
#for every entry in the list, remove punctution, perform tokenization
#and stemming to get words/stemmed data, also remove stop words(optional)
##"""
##first use bag of words approach, tfidf vectorizer to get features.
##
##"""

from preproc import alist
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import string


    
##function postproc take two lists, an empty list aalist and alist(the one returned from preproc.py)
##and remove punctuation, tokenizes and after stemming append the strin for every entry in list alist
##to aalist and returns aalist.

def features(sentence):
    features = {}

    gram_feature(features,sentence)

    return features


def gram_feature(features, sentence):
    #for strin in alist:
        #words = ""
        strp = sentence.translate(string.maketrans("",""),string.punctuation)
        tokens = word_tokenize(strp)
        stemmer = SnowballStemmer("english")
        stem = [stemmer.stem(token.lower()) for token in tokens]
        bigrams = nltk.bigrams(stem)
        bigrams = [gram[0]+ ' ' + gram[1] for gram in bigrams]
        grams = stem + bigrams
        #words = " ".join(stem)
        #print words
        for t in grams:
            features['contains(%s)' %t] = 1.0
        #aalist.append(words)

    #return aalist
##
##def vecto(aalist):
####    tf_transformer = TfidfTransformer(use_idf = False).fit(aalist)
####    X_train_tf = tf_transformer.transform(aalist)
####    return X_train_tf
##
##      count_vect = CountVectorizer()
##      bag_of_words = count_vect.fit(aalist)
##      bag_of_words = count_vect.transform(aalist)
##      tf = TfidfTransformer()
##      X_tfidf = tf.fit_transform(bag_of_words)
##      return X_tfidf
##      
##      
##    
    
    




def main():
    #aalist = []
    #aalist = postproc(alist,aalist)
    #print aalist
    #X = vecto(aalist)
    #print X
    for strin in alist:
        z = features(strin)
        print z
        
        
        

if __name__ == '__main__':
    main()



    
    


