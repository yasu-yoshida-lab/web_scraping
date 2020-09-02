#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
from web_scraping import get_news
from send_mail import mail


TO_ADDRESS = '********@*****'

def trans_body(dict_news):
	list_text = []
	list_ref = []

	for str_first in dict_news.keys():
		list_text += [dict_news[str_first][str_second] for str_second in dict_news[str_first].keys()]
		list_ref += [str_second for str_second in dict_news[str_first].keys()]
	
	list_body = [fist + ' ' + second for (fist, second) in zip(list_text, list_ref)]
	str_body = '\n'.join(list_body)

	return str_body


def news_mail(dict_news):
	now = datetime.datetime.now()
	
	subject = '(%4d/%2d/%2d)日経新聞スクレイピング'%(now.year, now.month, now.day)
	body = trans_body(dict_news)
	mail(TO_ADDRESS, subject, body)

if __name__=='__main__':
	dict_news = get_news()
	news_mail(dict_news)

