# To run this code, first edit config.py with your configuration
#
#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy 
import string
import json
import datetime

import config


class MyListener(tweepy.StreamListener):
    """Custom StreamListener for streaming data."""

    def __init__(self, data_dir, query):
        query_fname = format_filename(query)
        i = datetime.datetime.now()
        self.outfile = "Step_1_output/"+i.strftime('%Y_%m_%d')+"_stream_%s.json" % (query_fname)

    def on_data(self, data):
        try:
            with open(self.outfile, 'a') as f:
                f.write(data)
                config.logger.info(data)
                return True
        except BaseException as e:
            config.logger.error("Error on_data: %s" % str(e))
            time.sleep(5)
        return True

    def on_error(self, status):
        config.logger.error(status)
        return True

def format_filename(fname):
    """Convert file name into a safe string.

    Arguments:
        fname -- the file name to convert
    Return:
        String -- converted file name
    """
    return ''.join(convert_valid(one_char) for one_char in fname)

def convert_valid(one_char):
    """Convert a character into '_' if invalid.

    Arguments:
        one_char -- the char to convert
    Return:
        Character -- converted char
    """
    valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
    if one_char in valid_chars:
        return one_char
    else:
        return '_'

if __name__ == '__main__':
    config.logger.info(config.STEP_1_QUERY)
    auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACESS_SECRET)
    api = tweepy.API(auth)

    twitter_stream = tweepy.Stream(auth, MyListener("Step_1_output", config.STEP_1_QUERY))
    twitter_stream.filter(languages=["tr"],track=[config.STEP_1_QUERY])
