#!/bin/python3
#author='guanming'

import requests
import re
import json

def get_one_page(url):
	r=requests.get(url)
	if r.status_code==200:
		return r.content.decode('gbk')
	return None

def parse_one_page(html):
	pattern=re.compile('id="BookCon.*?<h1>(.*?)</h1>.*?BookText">(.*?)</div>',re.S)
	results=re.findall(pattern,html)
	for result in results:
		yield {
		'章节':result[0].strip(),
		'正文':result[1].strip().replace('&nbsp;','')
	}

def write_to_file(content):
	with open('wuxingshan.txt','w') as f:
		f.write(json.dumps(content,ensure_ascii=False)+'\n')

if __name__=='__main__':
	for i in range(7851802,7852304):
		print("开始爬取第",str(i-7851801),"章")
		url='https://www.quanben.net/14/14877/'+str(i)+'.html'
		html=get_one_page(url)
		results=parse_one_page(html)
		for result in results:
#			print(result)
			write_to_file(result)
