import tweepy 

class TwitterAPI:
    
    def __init__(self):
        consumer_key = ""
        consumer_secret = ""
        access_token = ""
        access_token_secret = ""

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
        auth.set_access_token(access_token, access_token_secret) 
        self.api = tweepy.API(auth) 
    
    def tweet(self, message):
        self.api.update_status(status=message) 
        


