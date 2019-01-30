# To run this code, first edit config.py with your configuration
#

#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import string

import plotly.plotly as py
import plotly.graph_objs as go
import plotly
plotly.tools.set_credentials_file(username='ozgurural', api_key='ZGOxDzigX5NHgC7PGMnM')

import config
import sqliteOperations

from bs4 import BeautifulSoup


frequency = {}
totalcount = 0

def getFrequencyOfWords(row):
    match_pattern = re.findall(r'\b[a-z]{3,15}\b', row[2])
    global totalcount
    for word in match_pattern:
        count = frequency.get(word,0)
        frequency[word] = count + 1
        totalcount = totalcount + 1


conn = sqliteOperations.createConnection(sqliteOperations.database)
with conn:
    print("1. Query task by Status:")
    rows = sqliteOperations.selectTaskByStatus(conn,"0")
    for row in rows:
        getFrequencyOfWords(row);

    frequency_list = frequency.keys()

    for words in frequency_list:
        print(words, frequency[words])

    for selected_strings in config.STRING_VECTOR:
        print("results=>>>>>>>>>>>>>>>")
        print(selected_strings, frequency[selected_strings])
        print("frequecy of " + selected_strings + ":", frequency[selected_strings] / totalcount)


with open("hacked.html") as fp:
    soup = BeautifulSoup(fp)