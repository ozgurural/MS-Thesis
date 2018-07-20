# -*- coding: utf-8 -*-

import json
import re

def main():

	#Reading Tweets
	print('Reading Tweets\n')
	tweets_data_path = 'Step_1_output/stream_ddos__siber__hacklendi.json'

	tweets_data = []
	notParsed = []
	tweets_file = open(tweets_data_path, "r")
	for line in tweets_file:
		if line.strip():   
			try:
				tweet = json.loads(line)
				tweets_data.append(tweet)
			except:
				notParsed.append(line)
				continue

	print(len(tweets_data))
	print('Could not parse: ', len(notParsed))

	#Structuring Tweets
	print('Structuring Tweets\n')
	print(type(tweets_data))
	tweets = {}

	tweets['text'] = [tweet['text'] for tweet in tweets_data]
	print('end')

	with open('Step_2_output/extractedlines.txt', 'w', encoding='utf-8') as the_file:
		for send in tweets['text']:
			print(send)
			the_file.write(send)

if __name__ == '__main__':
	main()