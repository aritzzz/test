"""
The script reads a text file in a txt_fileobj and makes basic cleaning to the tweets in txt file.
It removes hashtags and friendtags(TO DO: check for hashtags other than #sarcasm or rather hashtags
in between the tweet text, like this: 'These #bloody #airtel wale are so considerable.#sarcasm';
This script would change this tweet to -- 'These wale are so considerable'. Plus all the @tags are
removed and only those tweets are taken into account which do not start with '@' and doesn't
contain links 'http'.
Script returns the list of cleaned tweets.
"""
import os
os.chdir('C:/Users/Dell/Desktop')

import re

#alist = []

def preprocessing(txt_fileobj):
    alist = []
    

    hashtags = re.compile(r'#(?P<htag>\w+)\s?', re.I)  #for hashtags
    atag = re.compile(r'@\w+\s?', re.I)  #for friend tags
    #for line in file_object:
    for line in txt_fileobj:
        if 'http' not in line and len(line)>0 and line[0]!='@':
         
            line = hashtags.sub('', line)
            
            line =  hashtags.sub('', line)
            line = atag.sub('',line)
            line = re.sub(r'RT :','', line)
            alist.append(line)
    return alist

with open('process.txt', 'r+') as f:
        alist = preprocessing(f)
        
    

