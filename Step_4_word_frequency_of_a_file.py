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

frequency = {}

document_text = open(config.STEP_4_INPUT_DIR, encoding="utf8")
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
    """with open('Step_3_output/frequency.txt', 'w', encoding='utf-8') as the_file:
        the_file.write(selected_strings, frequency[selected_strings])"""



trace1 = go.Bar(
    x=["siber", "tehdit", "casusluk"],
    y=[3,7,9],
    name='Keywords',
    marker=dict(
        color='rgb(55, 83, 109)'
    )
)
trace2 = go.Bar(
    x=["siber", "tehdit", "casusluk"],
    y=[ 4, 11, 8],
    name='Keywords-2',
    marker=dict(
        color='rgb(26, 118, 255)'
    )
)
data = [trace1, trace2]
layout = go.Layout(
    title='Cyber Attacks',
    xaxis=dict(
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    yaxis=dict(
        title='Frequency',
        titlefont=dict(
            size=16,
            color='rgb(107, 107, 107)'
        ),
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='style-bar')