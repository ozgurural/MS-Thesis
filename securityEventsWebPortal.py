# To run this code, first edit config.py with your configuration
#

#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import string
import datetime

import config
import sqliteOperations

from bs4 import BeautifulSoup
import time

rowList = {}

def securityEventsWebPortalStart():
    while True:
        start()
        time.sleep(60)

def findInRow(row):
    for selected_strings in config.STRING_VECTOR:
        if selected_strings.lower() in row[4].lower():
            if selected_strings.lower() in rowList:
                rowList[selected_strings.lower()] = rowList[selected_strings.lower()][0] + 1,row
            else:
                rowList[selected_strings.lower()] = 1,row


def start():

    conn = sqliteOperations.createConnection(sqliteOperations.database)
    with conn:
        rows = sqliteOperations.selectTaskByStatus(conn,'1')
        for row in rows:
            findInRow(row)

        sqliteOperations.UpdateTaskByStatus(conn,"2")

    conn.close()
    with open("hacked.html", encoding='utf8') as fp:
        soup = BeautifulSoup(fp, 'html.parser')



    for name, tuple in rowList.items():
        ###
        findCheck = soup.find(id = tuple[1][1])
        if findCheck == None:
            title = soup.find(id = "1")
            meta = soup.new_tag('div')
            meta['class'] = "panel panel-primary"
            meta['id'] = tuple[1][1]
            title.insert(0,meta)

            title = soup.find(id=tuple[1][1])
            meta = soup.new_tag('div')
            meta['class'] = "panel-heading"
            meta['id'] = "panel-heading::" + tuple[1][1]
            meta.string = tuple[1][1]
            title.append(meta)

            title = soup.find(id = tuple[1][1])
            meta = soup.new_tag('div')
            meta['class'] = "panel-body"
            meta['id'] = "panel-body::" + tuple[1][1]
            title.append(meta)

            title = soup.find(id="panel-body::" + tuple[1][1])
            table = soup.new_tag('table')
            table['class'] = "table table-striped"
            table['id'] = "table table-striped" + tuple[1][1]
            title.append(table)

            tbody = soup.new_tag("tbody")
            tbody['id'] = "tbody::" + tuple[1][1]
            header = soup.new_tag("tr")
            for heading in ["Entity", "Representative News Title or Tweet", "Count"]:
                th = soup.new_tag("th")
                th.string = heading
                header.append(th)

            tbody.append(header)
        else: 
            tbody = soup.find(id = "tbody::" + tuple[1][1])
            table = soup.find(id = "table table-striped" + tuple[1][1])
            title = soup.find(id = "panel-body::" + tuple[1][1])
        
        ##
        badgeCheck = soup.find(id = name + "::" + tuple[1][1])
        ##
        if badgeCheck == None:
            td = soup.new_tag('td')
            tr = soup.new_tag("tr")
            a = soup.new_tag('a', href = '?section={}&action=whdw&question={}'.format(name,tuple),)
            a.string = name 
            td.append(a)
            tr.append(td)

            td = soup.new_tag("td")
            if tuple[1][3] == "--":
                td.string = tuple[1][4]
            else:
                td.string = tuple[1][3]
            tr.append(td)
            tbody.append(tr)

            td = soup.new_tag("td")
            span = soup.new_tag('span')
            span["class"] = "badge"
            span["id"] = name + "::" + tuple[1][1]
            span.string = str(tuple[0])
            td.append(span)
            tr.append(td)
            tbody.append(tr)
            
            table.append(tbody)   
            title.append(table)
        else: 
            badgeCheck.string.replace_with(str( int(badgeCheck.string) + tuple[0] ) )
        ###

    with open("hacked.html","w", encoding='utf8') as fp:
        fp.write(soup.prettify())
       
    rowList.clear()