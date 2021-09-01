import tweepy
from os import environ
from dotenv import load_dotenv

def connectAPI():
    load_dotenv()
    auth = tweepy.OAuthHandler(environ.get("CONSUMER_KEY"),environ.get("CONSUMER_SECRET"))
    auth.set_access_token(environ.get("ACCESS_TOKEN"), environ.get("ACCESS_TOKEN_SECRET"))
    return tweepy.API(auth)
