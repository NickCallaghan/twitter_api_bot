import tweepy
import time
import json
import sys
import csv
import datetime


from auth import auth
api = auth()


# Terminal Text Colors
class text_colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Follow user by passing in their screen_name


def follow_user(screen_name):
    try:
        api.create_friendship(screen_name)
        log_entry = [datetime.datetime.today(), screen_name]
        print_line_to_log(log_entry, "follows.csv")
        print(text_colors.OKGREEN + "followed  🙋‍♂️",
              screen_name + text_colors.ENDC)
    except tweepy.TweepError as e:
        print(e)


# Re-tweet by passing in the tweet_id
def retweet_tweet(tweet_id):
    try:
        api.retweet(tweet_id)
        print(text_colors.OKBLUE + "🐦  RE-TWEETED 🐦" + text_colors.ENDC)
    except tweepy.TweepError as e:
        print(e)


# Set the search term to the commandline args or the default
def set_search_term():
    if len(sys.argv) > 1:
        search_term = " ".join(sys.argv[1:])
        return search_term
    return "Python"


# Appends a single line to the end of a specified log file
def print_line_to_log(line, logfile):
    outputFile = open("logs/" + logfile, 'a', newline='')
    outputWriter = csv.writer(outputFile)
    outputWriter.writerow(line)
    outputFile.close()


# Search for tweets based on the search term.
def search_for_tweets_to_like(
        search_term, numTweets, follow=True, retweet=True, min_num_to_retweet=20):
    for tweet in tweepy.Cursor(api.search, search_term, lang="en").items(numTweets):
        try:
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
    print(text_colors.WARNING + "Twitter Bot Running...." + text_colors.ENDC)
    # Sets search_term from args or a default of "Python"
    search_term = set_search_term()
    print(text_colors.BOLD + "Searching twitter for: " +
          text_colors.ENDC + search_term)
    while True:
        # App will run continuously
        search_for_tweets_to_like(search_term, 50)


if __name__ == "__main__":
    main()
