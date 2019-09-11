import tweepy
from config import CONFIG
import tweepy


CONSUMER_KEY = CONFIG["CONSUMER_KEY"]
CONSUMER_SECRET = CONFIG["CONSUMER_SECRET"]
ACCESS_TOKEN = CONFIG["ACCESS_TOKEN"]
ACCESS_SECRET = CONFIG["ACCESS_SECRET"]


def like_tag():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)

    for status in api.search(q='#日曜だし邦ロック好きな人と繋がりたい', count=100):
        tweet_id = status.id
        # 例外処理をする
        try:
            # いいね実行
            api.create_favorite(tweet_id)
        except:
            print('error')


if __name__ == '__main__':
    like_tag()
