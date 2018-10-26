# To run this code, first edit config.py with your configuration
#

#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import string

import config

frequency = {}

document_text = open('Step_3_output/output.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
totalcount = 0
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
    totalcount = totalcount + 1
     
frequency_list = frequency.keys()
 
for words in frequency_list:
    print(words, frequency[words])

for selected_strings in config.STRING_VECTOR:
    print("results=>>>>>>>>>>>>>>>")
    print(selected_strings, frequency[selected_strings])
    print("frequecy of "+ selected_strings + ":", frequency[selected_strings]/totalcount)