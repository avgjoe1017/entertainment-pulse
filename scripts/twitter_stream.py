import os
import tweepy

# Twitter credentials
api_key = os.environ["TWITTER_API_KEY"]
api_secret = os.environ["TWITTER_API_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_secret = os.environ["TWITTER_ACCESS_SECRET"]

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
api = tweepy.API(auth)

# Define search query (example: "Taylor Swift")
query = "Taylor Swift -filter:retweets"
tweets = api.search_tweets(q=query, lang="en", result_type="recent", count=10)

for tweet in tweets:
    print(tweet.created_at, tweet.user.screen_name, tweet.text)
