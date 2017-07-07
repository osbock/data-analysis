import json
from tweepy import OAuthHandler, Stream,API
from tweepy.streaming import StreamListener

consumer_key ='nGEEp7jtrtfP7CBomWswStiH6'
consumer_secret='E4KDsgK61kKo8EOzeSZrwnNpC2mP8QySkXJjA2vlcNKxgXNgNi'
access_token='9135972-xiGzUPBuLn0lHlBeyaqQ7XcfzjsP6vhSHVPDkSgv6E'
access_token_secret='W9oxKn039Qj0erQbHDiUQHz6VLe7NpH7TPEAROs8wIONt'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)


class PrintListener(StreamListener):
    def on_status(self, status):
        if not status.text[:3] == 'RT ':
            print(status.text)
            print(status.author.screen_name,
                  status.created_at,
                  status.source,
                  '\n')

    def on_error(self, status_code):
        print("Error code: {}".format(status_code))
        return True #Keep stream alive

    def on_timeout(self):
        print('Listener timed out!')
        return True # Keep stream alive

def print_to_terminal():
    listener=PrintListener()
    stream = Stream(auth,listener)
    languages = ('en'  ,)
    stream.sample(languages=languages)
def pull_down_tweets(screen_name):
    api = API(auth)
    tweets = api.user_timeline(screen_name=screen_name, count = 200)
    for tweet in tweets:
#        print(json.dumps(tweet._json,indent=4))
        print( tweet.text )

if __name__ == '__main__':
#    print_to_terminal()
    pull_down_tweets('osbock')
