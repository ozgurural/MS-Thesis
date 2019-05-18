#!/usr/bin/python
import sqlite3
import json
import datetime
from sqlite3 import Error
import config

from bs4 import BeautifulSoup

database = "securityEventsDataBase.sqlite"

def twitterCreateSqliteTable(data):
    d = json.loads(data)
    databaseTable = sqlite3.connect(database)
    i = datetime.datetime.now()

    im = databaseTable.cursor()
    im.execute("""CREATE TABLE IF NOT EXISTS
        databaseTable (Source, Date, UserName, Title, Text PRIMARY KEY, Status)""")

    insert = "INSERT INTO DataBaseTable VALUES (\"twitter\", ?, ?, '--', ?, 0)"
    query = (i.strftime('%Y-%m-%d') , d['user']['screen_name'], BeautifulSoup(d['text'], "lxml").text)

    im.execute(insert, query)

    databaseTable.commit()
    databaseTable.close()

 
def createSqliteTable(data, source):
    databaseTable = sqlite3.connect(database)
    i = datetime.datetime.now()

    im = databaseTable.cursor()
    im.execute("""CREATE TABLE IF NOT EXISTS
        databaseTable ( Source, Date, UserName, Title, Text PRIMARY KEY, Status)""")
    for x in data['List']:

        for fmt in ('%Y-%m-%dT%H:%M:%S.%f', '%Y-%m-%dT%H:%M:%S'):
            try:
                 datetime_object = datetime.datetime.strptime(x['StartDate'], fmt)
            except ValueError:
                pass

        if(datetime_object.year < 2019):
            continue

        insert = "INSERT INTO databaseTable VALUES (\"hurriyet\", ?, '--', ?, ?, 0)"
        query = (str(datetime_object.date()), str(x['Title']), BeautifulSoup(x['Text'], "lxml").text)

        try: 
            im.execute(insert, query)
        except BaseException as e:
            config.logger.error("Error on_data: %s" % str(e))
            pass

    databaseTable.commit()
    databaseTable.close()
 
def createConnection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None
 
 
def selectTaskByStatus(conn, status):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    #cur.execute("SELECT * FROM databaseTable WHERE Status=\"0\" ")
    select = "SELECT * FROM databaseTable WHERE Status=" + status
    cur.execute(select,)
 
    rows = cur.fetchall()
 
    #for row in rows:
    #    print(row)

    conn.commit()
    return rows

def UpdateTaskByStatus(conn, status):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()

    update_1 = "UPDATE databaseTable SET Status = '" + status + "'  WHERE Status = 1"
    cur.execute(update_1,)

    conn.commit()

def UpdateTextByStatusWithItuNlpApi(conn, status, textBefore, textAfter):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    update_1 = """UPDATE databaseTable SET Status = ? WHERE Status = 0 AND Text = ? """ 
    update_2 = """UPDATE databaseTable SET Text = ? WHERE Text = ? """

    cur = conn.cursor()
  
    query_input_1 = (status, textBefore)
    query_input_2 = (textAfter, textBefore)
    
    cur.execute(update_1, query_input_1)
    cur.execute(update_2, query_input_2)

    conn.commit()
