#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
consumer_key = 'RWZFHdGbyt6pm5cT07PoYjNGy'
consumer_secret = 'SKf3426W0q7ZQ8S9aHbySDvCjXeFKb41LKS94IuAWPlrXnkVuH'
access_token = '87668698-FosGyxLDgwCDEjoi8H1Pz2u03m7flyIKU5aWnqx6O'
access_secret = 'dG761PxEt2MwVtxJyiMzNtlMJpfUg8Gp7lwK0bYSlhH58'


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])