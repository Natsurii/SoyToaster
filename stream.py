import tweepy
from connect import connectAPI
from renderer import soyImpose

class MyStreamListener(tweepy.StreamListener):

    def on_connect(self):
        print("tweepy connected to soyapi.")
        return super().on_connect()

    def on_status(self, status):
        print("received request from: " + str(status.id) + "|" + status.text)
        api = connectAPI()

        if "in_reply_to_user_id" in status._json:
            thread_owner = api.get_user(status._json["in_reply_to_user_id"])
            final_img = soyImpose(thread_owner._json["profile_image_url"])
            media = api.media_upload(final_img)
            api.update_status("OMG look at these soys.", in_reply_to_status_id = status.id , auto_populate_reply_metadata=True, media_ids=[media.media_id])

        else:
            api.update_status("Soy error! You should tag me in an existing tweet grrr..", in_reply_to_status_id = status.id, auto_populate_reply_metadata=True)