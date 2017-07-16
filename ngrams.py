import nltk



features = {}

def grams_feature(features, sentence):

    tokens = nltk.word_tokenize(sentence)
    #tokens = [porter.stem(t.lower()) for t in tokens] 
    bigrams = nltk.bigrams(tokens)
    bigrams = [tup[0]+' ' +tup[1] for tup in bigrams]
    #print bigrams
    grams = tokens + bigrams
    #print grams
    for t in grams:
        #features['contains(%s)' % t] = 1.0


sentence = "And here I am mulling over the emotional turmoil yet again, yet again without words"
grams_feature(features, sentence)
