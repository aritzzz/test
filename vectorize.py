

"""
This script does feature extraction over tweet data. The function features is defined which returns feature dictionary, and for now only unigrams and bigrams feature
have been added using another function gram_feature.
"""



import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
import string




def features(sentence):
    features = {}

    gram_feature(features,sentence)

    return features


def gram_feature(features, sentence):
        #words = " "
        tokens = word_tokenize(sentence)
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
    
    



##
##def main():
##    #aalist = []
##    #aalist = postproc(alist,aalist)
##    #print aalist
##    #X = vecto(aalist)
##    #print X
##    for strin in alist:
##        z = features(strin)
##        print z
##        
##        
##        
##
##if __name__ == '__main__':
##    main()



    
    


