import tweepy
import time
import json

# Generate API Keys from developer.twitter.com
from keys import api_key, api_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()


def follow_user(screen_name):
    try:
        api.create_friendship(screen_name)
        print("followed user: ", screen_name)
    except tweepy.TweepError as e:
        print(e)


def search_for_tweets_to_like(search_term, numTweets, follow=True):
    for tweet in tweepy.Cursor(api.search, search_term).items(numTweets):
        try:
            tweet.favorite()
            print("Tweet Liked")
            print(tweet.text)
            if follow == True:
                follow_user(tweet.user.screen_name)
            time.sleep(10)

        except tweepy.TweepError as e:
            e.reason


search_for_tweets_to_like("Javascript", 50)
