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
totalcount = 0

def getFrequencyOfWords(row):
    match_pattern = re.findall(r'\b[a-z]{3,15}\b', row[2])
    global totalcount
    for word in match_pattern:
        count = frequency.get(word.lower(),0)
        if word.lower() in frequency:
            frequency[word.lower()] = count[0]+1, row[0]
        else:
            frequency[word.lower()] = count+1, row[0]


conn = sqliteOperations.createConnection(sqliteOperations.database)
with conn:
    print("1. Query task by Status:")
    rows = sqliteOperations.selectTaskByStatus(conn,"0")
    for row in rows:
        getFrequencyOfWords(row)

    for selected_strings in config.STRING_VECTOR:
        if selected_strings.lower() in frequency:
            entity[selected_strings.lower()] = frequency[selected_strings.lower()]

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
header = soup.new_tag("tr")

for heading in ["Entity", "Representative Tweet", "Count"]:
    th = soup.new_tag("th")
    th.string = heading
    header.append(th)
table.append(header)
title.append(table)

for name, counts in frequency.items():
    print(name,":",counts)
    tr = soup.new_tag("tr")
    td = soup.new_tag("td")
    a = soup.new_tag("a")
    #td["class"] = "table table-striped"
    #td.string = name
    #td["class"] = "text-left"
    #tr.append(td)
    
    for key in ["Entity", "Representative Tweet", "Count"]:
        td = soup.new_tag("td")
        td.string = name
        #td["class"] = "text-left"
        tr.append(td)
        table.append(tr)
    
title.append(table)

with open("hacked.html","w", encoding='utf8') as fp:
    fp.write(soup.prettify())
