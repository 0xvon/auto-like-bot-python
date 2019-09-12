from config import CONFIG_b as CONFIG
import tweepy


CONSUMER_KEY = CONFIG["CONSUMER_KEY"]
CONSUMER_SECRET = CONFIG["CONSUMER_SECRET"]
ACCESS_TOKEN = CONFIG["ACCESS_TOKEN"]
ACCESS_SECRET = CONFIG["ACCESS_SECRET"]


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
