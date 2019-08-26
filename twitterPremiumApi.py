from TwitterAPI import TwitterAPI
from TwitterAPI import TwitterPager

import csv
import config

import re


def startTwitterPremiumApi2():
    SEARCH_TERM = 'nic.tr lang:tr'
    PRODUCT = 'fullarchive'
    LABEL = 'production'

    api = TwitterAPI(config.CONSUMER_KEY, 
                 config.CONSUMER_SECRET, 
                 config.ACCESS_TOKEN, 
                 config.ACCESS_SECRET)

    r = TwitterPager(api, 'tweets/search/%s/:%s' % (PRODUCT, LABEL),
        {'query':SEARCH_TERM, 
        'fromDate':'201512100000',
        'toDate':'201512282359',
        "maxResults": "100"
        }).get_iterator()

    csvFile = open('data.csv', 'w',encoding='UTF-8')
    csvWriter = csv.writer(csvFile)

    for item in r:
        csvWriter.writerow([item['created_at'],
                        item["id_str"],
                        item["source"],                    
                        item['user']['screen_name'],
                        item["user"]["location"],
                        item["geo"],
                        item["coordinates"], 
                        item['text'] if 'text' in item else item])


freqList = {}
def findInRow(row):
    print(row)
    for elements in row:
       if elements.lower() in freqList:
            freqList[elements.lower()] = freqList[elements.lower()] + 1
       else:
            freqList[elements.lower()] = 1

    sorted(freqList.items(), key=lambda item: item[1])
    for i in freqList:
        print(i +":"+ str(freqList[i]))


def startTwitterPremiumApi():
    csv.register_dialect('myDialect',
    delimiter = ',',
    quoting=csv.QUOTE_ALL,
    skipinitialspace=True)

    with open('data.csv', 'r', encoding='utf-8') as csvFile:
        reader = csv.reader(csvFile, dialect='myDialect')
        for row in reader:
            print(row[7].split())
            findInRow(row[7].split())
    csvFile.close()