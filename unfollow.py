from auth import auth
import tweepy
import csv
import sys

api = auth()


def unfollow(screen_name):
    try:
        api.destroy_friendship(screen_name)
        print("unfollowing: ❌", screen_name)
    except tweepy.TweepError as e:
        print(e)


def read_log_file(logfile):
    file = open('logs/' + logfile)
    reader = csv.reader(file)
    data = list(reader)
    return data


def set_log_file():
    print(sys.argv)
    if len(sys.argv) == 2:
        logfile = sys.argv[1]
        return logfile
    print("Please specify logfile name in args!!")
    exit()


def main():
    logfile = set_log_file()
    data = read_log_file(logfile)
    for user in data[1:]:
        screen_name = user[1]
        unfollow(screen_name)


if __name__ == "__main__":
    main()
