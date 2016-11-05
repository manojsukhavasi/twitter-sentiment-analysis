import tweepy

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "233210035-wCnsinyihbnEaa476dG0AOFtn8xh1v6R64MVDIV5"
access_token_secret = "JkyW3WKXCQElfra8SXNWHC8pdB1GJm7ghcN9AHnTsZ21j"
consumer_key = "nRX7YC54zuxeQcnPeSM9K2o4S"
consumer_secret = "RMc4XX5QlyqS8XCSRQDNVEoYtOtHy5b9MxskiM1oVoFASpMoqX"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class MyListener(StreamListener):

    def on_data(self,status):
        print(status.text)
		        
    def on_error(self,status_code):
        if status_code == 420:
            return False
						        

myListener = MyListener()
myStream = Stream(auth, listener=myListener)
myStream.filter(track = ['Bangalore'], async=True)
