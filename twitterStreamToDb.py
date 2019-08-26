# To run this code, first edit config.py with your configuration
#
#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy 
import string

import sqlite3
import time

import config
import sqliteOperations


class MyListener(tweepy.StreamListener):
    """Custom StreamListener for streaming data."""

    def on_data(self, data):
        try:
            sqliteOperations.twitterCreateSqliteTable(data);
            return True
        except BaseException as e:
            config.logger.error("Error on_data: %s" % str(e))
            time.sleep(5)
        return True

    def on_error(self, status):
        config.logger.error(status)
        return True

def startTwitterStreamToDb():
    config.logger.info(config.STEP_1_QUERY)
    auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)
    api = tweepy.API(auth)

    twitter_stream = tweepy.Stream(auth, MyListener())
    twitter_stream.filter(languages=["tr"],track=[config.STEP_1_QUERY])
