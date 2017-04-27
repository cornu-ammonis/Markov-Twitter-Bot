#scikitlearn - ML API 

import os 
from markovbot import MarkovBot
import twitter
import fileinput
import secrets
tweetbot = MarkovBot()


dirname = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the book
book = os.path.join(dirname, 'Sacred-Texts finance.txt')
# Make your bot read the book!
tweetbot.read(book)
#my_first_text = tweetbot.generate_text(25, seedword=['price'])
#print("tweetbot says:")
#print(my_first_text)

 
 
#### API SECTION INTENTIONALLY OBFUSCATED####
# Consumer Key (API Key)
cons_key = secrets.cons_key
# Consumer Secret (API Secret)
cons_secret = secrets.cons_secret
# Access Token
access_token = secrets.access_token
# Access Token Secret
access_token_secret = secrets.access_token_secret

tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)
######

targetstring = "@TaoJonesIndstrl"
keywords = None
prefix = None
suffix = '#TaoJones'
maxconvdepth = 5
#keywords = ['investments', 'price', 'become', 'self', 'analysis', 'meditation', 'consumer', 'stochastic']

# Start auto-responding to tweets
tweetbot.twitter_autoreply_start(targetstring, keywords=keywords, prefix=prefix, suffix=None, maxconvdepth=maxconvdepth)

#TODO: edit this method so it lets me select among several tweet, defaults to random choice after specified interval
#tweetbot.twitter_tweeting_start(days=0, hours=0, minutes=30, keywords=keywords, prefix=None, suffix=None)

import time; time.sleep(86400)
