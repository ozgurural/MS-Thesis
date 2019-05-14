# To run this code, first edit config.py with your configuration
#

#!/usr/bin/python3
#-*- coding: utf-8 -*-
import time
import re
import urllib.parse
import urllib.request

import config
import sqliteOperations

rowList = {}

def findInRow(row):
    for selected_strings in config.STRING_VECTOR:
        if selected_strings.lower() in row[4].lower():
            if selected_strings.lower() in rowList:
                rowList[selected_strings.lower()] = rowList[selected_strings.lower()][0] + 1,row
            else:
                rowList[selected_strings.lower()] = 1,row


class PipelineCaller(object):

    DEFAULT_SENTENCE_SPLIT_DELIMITER_CLASS = '[\.\?:;!]'

    def __init__(self, tool='normalize', text='example', token=config.ITU_NLP_API_TOKEN, processing_type='sentence'):
        self.tool = tool
        self.text = text
        self.token = token
        self.processing_type = processing_type

        self.sentences = []
        self.words = []

    def call(self):

        if self.processing_type == 'whole':
            params = self.encode_parameters(self.text)
            return self.request(params)

        if self.processing_type == 'sentence':
            results = []
            self.parse_sentences()

            for sentence in self.sentences:
                params = self.encode_parameters(sentence)
                results.append(self.request(params))

            return "\n".join(results)

        if self.processing_type == 'word':
            results = []
            self.parse_words()

            for word in self.words:
                params = self.encode_parameters(word)
                results.append(self.request(params))

            return "\n".join(results)

    def parse_sentences(self):
        r = re.compile(r'(?<=(?:{}))\s+'.format(PipelineCaller.DEFAULT_SENTENCE_SPLIT_DELIMITER_CLASS))
        self.sentences = r.split(self.text)

        if re.match('^\s*$', self.sentences[-1]):
            self.sentences.pop(-1)

    def parse_words(self):
        self.parse_sentences()

        for sentence in self.sentences:
            for word in sentence.split():
                self.words.append(word)

    def encode_parameters(self, text):
        return urllib.parse.urlencode({'tool': self.tool, 'input': text, 'token': self.token}).encode(config.PIPELINE_ENCODING)
    
    def request(self, params):
        response = urllib.request.urlopen(config.API_URL, params)
        return response.read().decode(config.PIPELINE_ENCODING)

"""
def startItuNlpApi():   
    text = "beniim adiim ozgüür"
    config.logger.info(text)
    config.logger.info(config.ITU_NLP_API_TOKEN)
    config.logger.info(config.API_URL)
    config.logger.info(config.PIPELINE_ENCODING)


    REQUEST_URL = config.API_URL + "?" + "tool=" + config.DEFAULT_TOOL + "&input=" + "MERHABAAAAAA" + "&token=" + config.ITU_NLP_API_TOKEN
    config.logger.info(REQUEST_URL)
    config.logger.info(config.DEFAULT_TOOL)

    start_time = time.time()

    caller = PipelineCaller(config.DEFAULT_TOOL, text, config.ITU_NLP_API_TOKEN, 'sentence')
    config.logger.info(caller.call())
    process_time = time.time() - start_time

    config.logger.info("[DONE] It took {0:.0f} seconds to process whole text.".format(process_time))

"""
def startItuNlpApi():
    # create a database connection
    conn = sqliteOperations.createConnection(sqliteOperations.database)
    with conn:
        while True:
            rows = sqliteOperations.selectTaskByStatus(conn, '0')
            for row in rows:
                config.logger.info(row[4])
                caller = PipelineCaller(config.DEFAULT_TOOL, row[4], config.ITU_NLP_API_TOKEN, 'sentence')
                sqliteOperations.UpdateTextByStatusWithItuNlpApi(conn, "1", row[4], row[4])
                time.sleep(10)
            time.sleep(60)
