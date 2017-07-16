# Import the necessary package to process data in JSON format
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

# Initiate the connection to Twitter Streaming API
#twitter_stream = TwitterStream(auth=oauth)
twitter = Twitter(auth = oauth)
# Get a sample of the public data following through Twitter
#iterator = twitter_stream.statuses.filter(lang = 'en', track = '#sarcasm')
iterator = twitter.search.tweets(q = '#sarcasm', result_type = 'recent', lang ='en', count = 10)
# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 10
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    data =  json.dumps(tweet, indent = 2)
    #print data['id']
    with open("twitter_streaming.txt", "w") as f:
        f.write(data)
    with open("twitter_streaming.txt", "r") as f1:
        data1 = json.load(f1)
    with open("processed.txt", "a") as f2:
        try:
          if "text" in data1:
              f2.write(data1["text"])
              f2.write(data1['user']['name'])
              f2.write('--')
              #f2.write(data1["text"])
              #f2.write(data1['entities']['hashtags'])
              #f2.write('...\n')
              hashtags = []
              for hashtag in data1['entities']['hashtags']:
                 hashtags.append(hashtag["text"])
              json.dump(hashtags, f2)
              f2.write('...\n')

        except:
          continue
    #with open("twitter_streaming.txt", "w") as f3:
         #f3.truncate()   
     # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
       
    if tweet_count <= 0:
        break 
