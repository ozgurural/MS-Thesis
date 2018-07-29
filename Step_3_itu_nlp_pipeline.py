#!/usr/bin/python3
#-*- coding: utf-8 -*-

import time
import re

import urllib.parse
import urllib.request

API_TOKEN = "mV8gEbWRDGnaSKwcRyFnwwp11S6tUmCZ"
DEFAULT_OUTPUT_DIR = 'Step_3_output/output.txt'
API_URL = 'http://tools.nlp.itu.edu.tr/SimpleApi?tool='
PIPELINE_ENCODING = 'UTF-8'
INPUT_DIR = "Step_2_output/extractedlines.txt"
DEFAULT_TOOL =  "normalize"

class PipelineCaller(object):
    API_URL = 'http://tools.nlp.itu.edu.tr/SimpleApi'
    PIPELINE_ENCODING = 'UTF-8'

    DEFAULT_SENTENCE_SPLIT_DELIMITER_CLASS = '[\.\?:;!]'

    def __init__(self, tool='normalize', text='example', token=API_TOKEN, processing_type='sentence'):
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
        return urllib.parse.urlencode({'tool': self.tool, 'input': text, 'token': self.token}).encode(self.PIPELINE_ENCODING)
    
    def request(self, params):
        response = urllib.request.urlopen(self.API_URL, params)
        return response.read().decode(self.PIPELINE_ENCODING)



def main():
    with open(INPUT_DIR, encoding=PIPELINE_ENCODING) as input_file:
        text = input_file.read()
    
    print(text)
    print(API_TOKEN);
    print(DEFAULT_OUTPUT_DIR);
    print(API_URL);
    print(PIPELINE_ENCODING);
    print(INPUT_DIR);
    print(DEFAULT_TOOL);
    REQUEST_URL = API_URL+ DEFAULT_TOOL + "&input="+"MERHABAAAAAA"+"&token="+ API_TOKEN
    print(REQUEST_URL);

    start_time = time.time()

    caller = PipelineCaller(DEFAULT_TOOL, text, API_TOKEN, 'sentence')
    with open(DEFAULT_OUTPUT_DIR, 'w', encoding=PIPELINE_ENCODING) as output_file:
        output_file.write('{}\n'.format(caller.call()))

    process_time = time.time() - start_time

    print("[DONE] It took {0:.0f} seconds to process whole text.".format(process_time))

if __name__ == '__main__':
	main()