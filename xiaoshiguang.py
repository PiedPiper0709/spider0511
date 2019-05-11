#!/bin/python3

import requests
import re
import json

def get_one_page(url):
	r=requests.get(url)
	if r.status_code==200:
		return r.content.decode('gbk')
	return None

def parse_one_page(html):
	pattern=re.compile('<h1>(.*?)</br>.*?</a></p>(.*?)</p>',re.S)
	results=re.findall(pattern,html)
	for item in results:
		yield {
			'title':item[0],
			'content':item[1]
		}

def write_to_file(content):
	with open('xiaoshiguang.txt','a') as f:
		f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main(offset):
	url='https://www.kanunu8.com/book2/10944/'+str(offset)+'.html'
	html=get_one_page(url)
	results=parse_one_page(html)
	print("正在爬取第",str(offset-195306),"页")
	for result in results:
		print(result)
		write_to_file(result)

if __name__=='__main__':
	for i in range(195307,195383):
		main(i)
