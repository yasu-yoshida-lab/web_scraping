#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import datetime
from bs4 import BeautifulSoup
TOP = "https://www.nikkei.com"


def scraper(URL):
	dict_title = {}
	
	url = requests.get(URL)
	soup = BeautifulSoup(url.content, "html.parser")

	elems = soup.find_all("div", class_='m-miM09')
	for elem in elems:
		try:
			title = elem.find('span', class_='m-miM09_titleL').text
			dict_title[TOP + elem.find('a').get('href')] = title
		except:
			pass

	return dict_title

def get_news():
	dict_news = {}

	print("日本経済新聞--ビジネス/スタートアップ--")
	URL = TOP + "/business/startups/"
	dict_tmp = scraper(URL)
	dict_news["startups"] = dict_tmp

	print("日本経済新聞--テクノロジー/最新技術--")
	URL = TOP + "/technology/leading-edge/"
	dict_tmp = scraper(URL)
	dict_news["leading"] = dict_tmp

	print("日本経済新聞--テクノロジー/AI--")
	URL = TOP + "/technology/ai/"
	dict_tmp = scraper(URL)
	dict_news["ai"] = dict_tmp

	print("日本経済新聞--テクノロジー/IoT--")
	URL = TOP + "/technology/iot/"
	dict_tmp = scraper(URL)
	dict_news["iot"] = dict_tmp

	return dict_news

def main():
	dict_news = get_news()
	print(dict_news)

if __name__=='__main__':
	main()
