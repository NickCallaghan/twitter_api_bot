import tweepy
import time
import json


# Generate API Keys from developer.twitter.com
from keys import api_key, api_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def follow_user(screen_name):
    try:
        api.create_friendship(screen_name)
        print("followed  🙋‍♂️", screen_name)
    except tweepy.TweepError as e:
        print(e)


def retweet_tweet(tweet_id):
    try:
        api.retweet(tweet_id)
        print("🐦  RE-TWEETED 🐦")
    except tweepy.TweepError as e:
        print(e)


def search_for_tweets_to_like(
        search_term, numTweets, follow=True, retweet=True, min_num_to_retweet=1):
    for tweet in tweepy.Cursor(api.search, search_term).items(numTweets):
        try:
            if tweet.lang == "en":
                print('\n\n--------------------------------------------')
                print(tweet.text)
                tweet.favorite()
                print("🔥 Tweet Liked! 🔥")
                # Decide whether to FOLLOW or RETWEET
                if follow == True:
                    follow_user(tweet.user.screen_name)
                if tweet.retweet_count > min_num_to_retweet and retweet == True:
                    retweet_tweet(tweet.id)
            time.sleep(10)

        except tweepy.TweepError as e:
            e.reason


def main():
    print("Twitter Bot Running....")
    search_for_tweets_to_like("javascript", 50)


if __name__ == "__main__":
    main()
