#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import ssl

FROM_ADDRESS = '********@*****'
MY_PASSWORD = 'SMTPサーバーのパスワード'
BCC = ''


def create_message(from_addr, to_addr, bcc_addrs, subject, body):
	msg = MIMEText(body)
	msg['Subject'] = subject
	msg['From'] = from_addr
	msg['To'] = to_addr
	msg['Bcc'] = bcc_addrs
	msg['Date'] = formatdate()
	return msg


def send(from_addr, to_addrs, msg):
	smtpobj = smtplib.SMTP_SSL('smtp.***.***', 465, timeout=10)
	smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
	smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
	smtpobj.close()

def mail(to_addr='', subject='', body=''):
	msg = create_message(FROM_ADDRESS, to_addr, BCC, subject, body)
	send(FROM_ADDRESS, to_addr, msg)

def main():
	TO_ADDRESS = '*******@****'
	SUBJECT = '（件名）'
	BODY = '（本文）'

	to_addr = TO_ADDRESS
	subject = SUBJECT
	body = BODY

	mail(to_addr, subject, body)

if __name__ == '__main__':
	main()
