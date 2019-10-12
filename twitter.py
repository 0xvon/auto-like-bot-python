import tweepy
import os


CONSUMER_KEY = os.environ["CONSUMER_KEY_b"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET_b"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN_b"]
ACCESS_SECRET = os.environ["ACCESS_SECRET_b"]


def like_tag():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    # api.update_status("HELLO")

    for status in api.search(q='music fm', count=1):
        tweet_id = status.id
        try:
            api.create_favorite(tweet_id)
        except:
            print('error')


if __name__ == '__main__':
    like_tag()
