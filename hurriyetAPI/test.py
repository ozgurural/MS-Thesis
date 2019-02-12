from hurriyetApi import HurriyetApi

import sqlite3
import time

import sqliteOperations
import config

apikey = "58147a8ca752485fad3cf28e5e35a87d"
api = HurriyetApi(apikey)
writer = api.searchWriter("Adil")
articles = api.listArticles(42, 3)
searchKeyword = api.search("siber")


with open('hurriyet.html', 'w', encoding='utf-8') as the_file:
	the_file.write(str(searchKeyword))

try:
    sqliteOperations.createSqliteTable(data)
except BaseException as e:
    config.logger.error("Error on_data: %s" % str(e))
    time.sleep(5)
