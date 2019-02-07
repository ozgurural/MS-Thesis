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


frequency = {}
entity = {}
rowList = {}
totalcount = 0

"""
def getFrequencyOfWords(row):
    match_pattern = re.findall(r'\b[a-z]{3,15}\b', row[2])
    global totalcount
    for word in match_pattern:
        count = frequency.get(word.lower(),0)
        if word.lower() in frequency:
            frequency[word.lower()] = count[0] + 1, row[0]
        else:
            frequency[word.lower()] = count + 1, row[0]
"""

def findInRow(row):
    for selected_strings in config.STRING_VECTOR:
        if selected_strings.lower() in row[2]:
            if selected_strings.lower() in rowList:
                rowList[selected_strings.lower()] += 1,row
            else:
                rowList[selected_strings.lower()] = 1,row
    

conn = sqliteOperations.createConnection(sqliteOperations.database)
with conn:
    print("1. Query task by Status:")
    rows = sqliteOperations.selectTaskByStatus(conn,"0")
    for row in rows:
        findInRow(row)

with open("hacked.html", encoding='utf8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

title = soup.find(id="1")
meta = soup.new_tag('div')
meta['class'] = "panel panel-primary"
meta['id'] = "11"
title.insert(0,meta)

title = soup.find(id="11")
meta = soup.new_tag('div')
meta['class'] = "panel-heading"
meta['id'] = "111"
meta.string = datetime.datetime.now().strftime("%Y-%m-%d")
title.append(meta)

title = soup.find(id="11")
meta = soup.new_tag('div')
meta['class'] = "panel-body"
meta['id'] = "112"
title.append(meta)

title = soup.find(id="112")
table = soup.new_tag('table')
table['class'] = "table table-striped"
table['id'] = "1121"

tbody = soup.new_tag("tbody")
header = soup.new_tag("tr")
for heading in ["Entity", "Representative Tweet", "Count"]:
    th = soup.new_tag("th")
    th.string = heading
    header.append(th)

tbody.append(header)

for name, tuple in rowList.items():
    #print(name,":",counts)
    td = soup.new_tag('td')
    tr = soup.new_tag("tr")
    a = soup.new_tag('a', href = '?section={}&action=whdw&question={}'.format(name,tuple),)
    a.string = name 
    td.append(a)
    tr.append(td)

    td = soup.new_tag("td")
    td.string = tuple[1][2]
    tr.append(td)
    tbody.append(tr)

    td = soup.new_tag("td")
    span = soup.new_tag('span')
    span["class"] = "badge"
    span.string = str(tuple[0])
    td.append(span)
    tr.append(td)
    tbody.append(tr)

table.append(tbody)   
title.append(table)

with open("hacked.html","w", encoding='utf8') as fp:
    fp.write(soup.prettify())
