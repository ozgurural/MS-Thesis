import datetime
import os
import time
import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import sqlite3

driver = None

INFO = "[INFO]"
ERROR = "[ERROR]"

CHROME75 = "chromedriver76"
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
ADVANCED_SEARCH_PAGE_TOP = "https://twitter.com/search?q=((siber%20saldırı)%20OR%20hacklendi%20OR%20(fidye%20yazılımı)%20OR%20zafiyet%20OR%20ddos%20OR%20erişilemiyor%20OR%20(zararlı%20yazılım)%20OR%20malware%20OR%20virüs%20OR%20(casus%20yazılım)%20OR%20fidye%20OR%20yazılımı%20OR%20oltalama%20OR%20phising%20OR%20(güvenlik%20duvarı)%20OR%20firewall%20OR%20hacker%20OR%20(sistem%20açığı)%20OR%20cyberattack%20OR%20cyberwarfare%20OR%20hacking%20OR%20(kimlik%20avı)%20OR%20spear-phishing)%20lang%3Atr%20until%3A2015-12-15%20since%3A2015-12-14&src=typed_query"
ADVANCED_SEARCH_PAGE_LATEST = "https://twitter.com/search?f=tweets&vertical=default&q=since%3A2015-02-14%20until%3A2015-02-28&l=tr&src=typd"
SCROLL_PAUSE_TIME = 1


def init_print():
	print("    __                         __")
	print("   / /_  __  _______________  / /")
	print("  / __ \/ / / / ___/ ___/ _ \/ / ")
	print(" / /_/ / /_/ / /  / /__/  __/ /  ")
	print("/_.___/\__,_/_/   \___/\___/_/   ")
	print("                                 ")


# Get current time
def get_time():
	return str(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))


# Parse exception and return as string
def exception_parser(ex):
	exception_return_string = ""
	try:
		exception_return_string = ex.__class__.__name__ + ": " + str(ex)
	except Exception as e:
		exception_return_string = "Failed to parse exception with error: " + e.__class__.__name__ + ": " + str(e)
	finally:
		return exception_return_string


def disperse_login_popup():
	search_navigation_title = driver.find_element_by_class_name("SearchNavigation-titleText")
	search_navigation_title.click()


def work():
	global driver

	print(get_time(), INFO, "Commencing Chrome webdriver initialization..")

	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--incognito")
	# chrome_options.add_argument("--headless")
	chrome_options.add_argument("--log-level=3")
	chrome_options.add_argument("user-agent=%s" % USER_AGENT)
	chrome_options.add_argument('--blink-settings=imagesEnabled=false')  # Disable images

	chrome_driver_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), CHROME75)
	print(get_time(), INFO, "Chrome webdriver path:", chrome_driver_path)

	driver = webdriver.Chrome(chrome_driver_path, chrome_options=chrome_options)
	print(get_time(), INFO, "Chrome driver is started.")

	twitter_search_url = ADVANCED_SEARCH_PAGE_TOP.format("2015-02-14", "2015-02-28")
	print(get_time(), INFO, "Opening page:", twitter_search_url)

	driver.get(twitter_search_url)
	# driver.set_window_size(1024, 768)

	stream_items = driver.find_element_by_id("stream-items-id")

	disperse_login_popup()

	tweet_index = 1

	database = "nictr_attack_start_day_try2_securityEventsDataBase.sqlite"
	databaseTable = sqlite3.connect(database)

	im = databaseTable.cursor()
	im.execute("""CREATE TABLE IF NOT EXISTS databaseTable (Source, Date, UserName, Title, Text, Status)""")

	# Get scroll height
	last_height = driver.execute_script("return document.body.scrollHeight")
	while True:
		# Scroll down to bottom
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

		# Wait to load page
		time.sleep(SCROLL_PAUSE_TIME)

		# Calculate new scroll height and compare with last scroll height
		new_height = driver.execute_script("return document.body.scrollHeight")
		if new_height == last_height:
			break
		last_height = new_height

		tweets = stream_items.find_elements_by_css_selector('li.stream-item')
		tweet_count = len(tweets)
		for tweet in tweets:
			print("-- Tweet #%s --" % tweet_index)
			print(tweet.find_element_by_class_name("fullname").text)
			print(tweet.find_element_by_class_name("username").text)
			print(tweet.find_element_by_class_name("tweet-timestamp").get_attribute("href"))
			print(tweet.find_element_by_class_name("tweet-timestamp").find_element_by_class_name("_timestamp").get_attribute("data-time-ms"))
			print(tweet.find_element_by_class_name("tweet-text").text)
			tweet_index += 1

			insert = "INSERT INTO DataBaseTable VALUES (\"twitter\", ?, ?, \"--\", ?, \"0\")"
			query = (tweet.find_element_by_class_name("tweet-timestamp").find_element_by_class_name("_timestamp").get_attribute("data-time-ms"),
					 tweet.find_element_by_class_name("username").text, 
					 tweet.find_element_by_class_name("tweet-text").text)
			
			im.execute(insert, query)
			databaseTable.commit()
		
		

		# print("%s %s Tweet count: %s" % (get_time(), INFO, tweet_count), end="\r", flush=True)


def main():
	try:
		work()
	except Exception as e:
		print(get_time(), ERROR, exception_parser(e))
	finally:
		try:
			if driver is not None:
				driver.close()
		except Exception as e:
			print(get_time(), ERROR, exception_parser(e))


if __name__ == "__main__":
	main()
