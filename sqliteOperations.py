#!/usr/bin/python
import sqlite3
import json
import datetime
from sqlite3 import Error
import config

database = "securityEventsDataBase.sqlite"

def twitterCreateSqliteTable(data):
    d = json.loads(data)
    rawTwitterDB = sqlite3.connect(database)
    i = datetime.datetime.now()

    im = rawTwitterDB.cursor()
    im.execute("""CREATE TABLE IF NOT EXISTS
        rawTwitterDBtable (Source, Date, UserName, Title, Text, Status)""")

    im.execute("""INSERT INTO rawTwitterDBtable VALUES
        (\"""" + 'twitter' + """\",
        \"""" + i.strftime('%Y_%m_%d') + """\",
        \"""" + d['user']['screen_name'] + """\", 
        \"""" + '--' + """\", 
        \"""" + d['text'] + """\",
        0 )""")

    rawTwitterDB.commit()
    rawTwitterDB.close()

 
def createSqliteTable(data, source):
    rawTwitterDB = sqlite3.connect(database)
    i = datetime.datetime.now()

    im = rawTwitterDB.cursor()
    im.execute("""CREATE TABLE IF NOT EXISTS
        rawTwitterDBtable (Source, Date, UserName, Title, Text, Status)""")
    for x in data['List']:
        #print(x['StartDate'])
        #print(x['Title'])

        for fmt in ('%Y-%m-%dT%H:%M:%S.%f', '%Y-%m-%dT%H:%M:%S'):
            try:
                 datetime_object = datetime.datetime.strptime(x['StartDate'], fmt)
            except ValueError:
                pass

        try: 
            im.execute("""INSERT INTO rawTwitterDBtable VALUES
                (\"""" + "hurriyet" + """\", 
                \"""" + str(datetime_object.date()) + """\",
                \"""" + '--' + """\",
                \"""" + str(x['Title']) + """\",
                \"""" + str(x['Text']) + """\",
                0 )""")
        except BaseException as e:
            config.logger.error("Error on_data: %s" % str(e))
            pass

    rawTwitterDB.commit()
    rawTwitterDB.close()
 
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
 
 
def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM rawTwitterDBtable")
 
    rows = cur.fetchall()

 
 
def selectTaskByStatus(conn, status):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM rawTwitterDBtable WHERE Status=" + status)
 
    rows = cur.fetchall()
 
    #for row in rows:
    #    print(row)

    return rows

def UpdateTaskByStatus(conn, status):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("UPDATE rawTwitterDBtable SET Status ="+status+" WHERE Status=\"0\"")
