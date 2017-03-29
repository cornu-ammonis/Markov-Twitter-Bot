import os 
from markovbot import MarkovBot
import twitter
import fileinput
import secrets
import timerInput

tweetbot = MarkovBot()


dirname = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the book
book = os.path.join(dirname, 'Sacred-Texts finance.txt')
# Make your bot read the book!
tweetbot.read(book)

book = os.path.join(dirname, 'studyOfInnerCultivation.txt')
tweetbot.read(book)
my_first_text = []
for i in range(5):
    my_first_text.append(tweetbot.generate_text(25, seedword=["consumer"]))

for i in range(len(my_first_text)):
    print("option " + str(i) + " " + my_first_text[i])
response = timerInput.nonBlockingRawInput("make your selection: ", 30)
if len(response) > 0:
    try:
        print("tweetbot says:")
        print(my_first_text[int(response)])
    except ValueError:
        print("invalid input")
        print("tweetbot syas:")
        print(my_first_text[0])
else:
    print("tweetbot says")
    print(my_first_text[0])
        
#print("tweetbot says:")
#print(my_first_text)"""


"""
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

#targetstring = 'Nietzsche'
keywords = None
prefix = None
suffix = '#TaoJones'
maxconvdepth = 2
keywords = ['investments', 'price', 'consumer', 'stochastic', 'bitcoin', ]

# Start auto-responding to tweets
#tweetbot.twitter_autoreply_start(targetstring, keywords=keywords, prefix=prefix, suffix=suffix, maxconvdepth=maxconvdepth)

#TODO: edit this method so it lets me select among several tweet, defaults to random choice after specified interval
tweetbot.twitter_tweeting_start(days=0, hours=0, minutes=44, keywords=keywords, prefix=None, suffix=None, allowselection=True)
"""
import time; time.sleep(86400) 
