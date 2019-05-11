#!/bin/python

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
	pattern=re.compile('size="4">(.*?)</font>.*?width="820".*?#FFFFFF">(.*?)</p>',re.S)
	print(type(html))
	results=re.findall(pattern,html)
	for result in results:
		yield {
			'title':result[0].strip(),
			'content':result[1].strip(),
		}

def write_to_file(content):
	with open('jiuzhoupiaomiaolv.txt2','a') as f:
		f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main(offset):
	url='https://www.kanunu8.com/book/4493/'+str(offset)+'.html'        
	html=get_one_page(url)
	print(html)
	for result in parse_one_page(html):
		#print('正在爬取第',str(i-57832),'页',"《",result['title'],"》")
		print(result)
		write_to_file(result)

if __name__=='__main__':
	for i in range(57869,57979):
		main(i)
