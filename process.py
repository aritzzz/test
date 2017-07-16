"""
The script reads a text file in a txt_fileobj and makes basic cleaning to the tweets in txt file.
It removes hashtags and friendtags(TO DO: check for hashtags other than #sarcasm or rather hashtags
in between the tweet text, like this: 'These #bloody #airtel wale are so considerable.#sarcasm';
This script would change this tweet to -- 'These wale are so considerable'. Plus all the @tags are
removed and only those tweets are taken into account which do not start with '@' and doesn't
contain links 'http'.



Script returns numpy array of cleaned tweets.
"""



#import os
#os.chdir('C:/Users/Dell/Desktop/tweets_data')
import numpy as np

import re
import string

#alist = []

def preprocessing(txt_fileobj):
    alist = []
    

    hashtags = re.compile(r'#(?P<htag>\w+)\s?', re.I)  #for hashtags
    atag = re.compile(r'@\w+\s?', re.I)  #for friend tags
    #for line in file_object:
    for line in txt_fileobj:
        #print line 
        if 'http' not in line and len(line)>0 and line[0]!='@':
         
            line = hashtags.sub('', line)
            
            line =  hashtags.sub('', line)
            line = atag.sub('',line)
            line = re.sub(r'RT :','', line)
            line = line.translate(string.maketrans("",""),string.punctuation)  #remove all sort of punctuation from line
            alist.append(line)
            
    alist = list(set(alist))
    alist = np.array(alist)
    return alist

### for file containing sarcastic tweets   

with open('positive.txt', 'r+') as f:
        pdata = preprocessing(f)
### for file containing regular tweets

##with open('regular.txt', 'r+') as f:
##        ndata = preprocessing(f)

np.save('sarcasmproc', pdata)
#np.save('regularproc',ndata)

        
    


