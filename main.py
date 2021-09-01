### SOY BOT version Lousy. ####
import time
import tweepy
from stream import MyStreamListener
from connect import connectAPI


def main():
    soyapi = connectAPI()
    myStreamListener = MyStreamListener(api=soyapi)
    stream = tweepy.Stream(auth = soyapi.auth, listener=myStreamListener, daemon = True)
    stream.filter(track=['@2Soyjacks'])

def magicRecursiveLoop():
    try:
        main()
    except:
        time.sleep(2)
        magicRecursiveLoop()

magicRecursiveLoop()
