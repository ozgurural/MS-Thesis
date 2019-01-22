#!/usr/bin/python
import sqlite3
from sqlite3 import Error
 
def createSqliteTable(data):
    d = json.loads(data)
    rawTwitterDB = sqlite3.connect("twitterDataDb.sqlite")
    i = datetime.datetime.now()

    im = rawTwitterDB.cursor()
    im.execute("""CREATE TABLE IF NOT EXISTS
        rawTwitterDBtable (Name, Date, Text, Status)""")

    im.execute("""INSERT INTO rawTwitterDBtable VALUES
        (\""""+ d['user']['screen_name'] +"""\", 
        \""""+ i.strftime('%Y_%m_%d') +"""\",
        \""""+ d['text'] +"""\",
        0 )""")

    rawTwitterDB.commit()
    rawTwitterDB.close()
 
def create_connection(db_file):
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
 
    for row in rows:
        print(row)
 
 
def select_task_by_status(conn, Status):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM rawTwitterDBtable WHERE Status=0")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
""" 
def main():
    database = "twitterDataDb.sqlite"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query task by priority:")
        select_task_by_priority(conn,1)
 
        print("2. Query all tasks")
        select_all_tasks(conn)
 
 
if __name__ == '__main__':
    main()
"""