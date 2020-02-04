from hurriyetApi import HurriyetApi

import sqlite3
import time

import sqliteOperations
import config

apikey = "XXXXXXXXXXXXXXXXXXXXx"

def hurriyetApiToDb():
    api = HurriyetApi(apikey)

    for x in config.securityTermsList:
        searchKeyword = api.search(x)
        try:
            sqliteOperations.createSqliteTable(searchKeyword, "hurriyet")
        except BaseException as e:
            config.logger.error("Error on_data: %s" % str(e))
   
def startHurriyetApiToDb():
   while True:
       hurriyetApiToDb()
       time.sleep(36000)
