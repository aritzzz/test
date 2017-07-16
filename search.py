import os
os.chdir("C:\Users\Dell\Desktop")

try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '955013773-aigu0eUcaoTmfkrDGjD9tRG6T26iCO62530K0ZNr'
ACCESS_SECRET = '7MIC05XZSTJjIiz0LdFFUO3DGHNdttKDrEsxMK6MpFRYd'
CONSUMER_KEY = 'ctKceIbGHdt39BC9KTjUOmSRV'
CONSUMER_SECRET = 'VBbiFuR1BYNcu0P0xWuY7ji5s11PzgoXiuNyEt5jZXWVhuvRvf'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter = Twitter(auth = oauth)

query = twitter.search.tweets(q = '#sarcasm', result_type = 'recent', lang ='en', count = 40)

#for tweet in query:
data = json.dumps(query, indent = 2)
with open('processed.txt', 'a') as f1:
    f1.write(data)
for result in query['statuses']:
    with open('process.txt', 'a') as f:
        try:
           # f.write(result['user']['screen_name'])
           # f.write('--')
            f.write(result['text'])
            f.write('\n')
        except:
            continue

        
