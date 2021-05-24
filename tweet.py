import time

import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
# Please fill the above details which u have to fill
# create using twitter api

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Your info
user = api.me()
print("Your details: ", user)


def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except StopIteration:
        time.sleep(300)
    except tweepy.RateLimitError:
        time.sleep(300)


search_string = ''  # String which u would use to like or retweet a tweet
no_of_tweets = 2  # You can modify the number as per ur requirement

for tweet in limit_handle(tweepy.Cursor(api.search, search_string).items(no_of_tweets)):
    try:
        tweet.favorite()
        tweet.retweet()
        print("I retweet the tweet")
        print("I liked the tweet")

    except tweepy.TweepError as e:
        print(e.reason)
