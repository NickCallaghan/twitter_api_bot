from keys import api_key, api_secret, access_token, access_token_secret
import tweepy


# Generate API Keys from developer.twitter.com
def auth():
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth, wait_on_rate_limit=True,
                      wait_on_rate_limit_notify=True)
