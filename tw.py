# test access twitter

import tweepy
from dotenv import load_dotenv
import os

from pymongo import MongoClient

load_dotenv()

client = MongoClient(os.getenv('MONGO_HOST'), int(os.getenv('MONGO_PORT')))
x = [x for x in client.tweets.tweets.find({'Rating':'BBB'})]

auth = tweepy.OAuth2BearerHandler(os.getenv('BEARER_TOKEN'))
api = tweepy.API(auth)

tweet_client = tweepy.Client(os.getenv('BEARER_TOKEN'))

query = 'from:suhemparack -is:retweet'
tweets = tweet_client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)


tweets = tweepy.Cursor(api.search_tweets, "#AAPL", lang="en", since_id='2022-10-01', tweet_mode='extended').items(100)
for tweet in tweets:
    pass