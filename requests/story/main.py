import requests
from bs4 import BeautifulSoup
import time
import os
import sys

#path_ = ''

def write_txt(name, code, msg):
	#global path_
	path_ = 'D:\\Sublime_Text_output\\py\\requests\\故事\\download\\'
	real_path = path_ + name + '.txt'
	file_open = open(real_path, 'w+', encoding = code, errors = 'ignore')
	file_open.write(msg)
	file_open.close()

def get_text(url):
	global code
	response = requests.get(url = url, timeout = 30000)
	response.encoding = response.apparent_encoding
	code = response.apparent_encoding
	html = BeautifulSoup(response.text, 'html.parser')
	result = html.find_all('dd')[0].find_all('p')[0].text
	#print(result[0].find_all('p')[0].text)
	return result

def get_list_url_and_write(x, y, type_, num):
	#global path_
	https = []
	for count in range(x, y + 1):
		url = 'http://www.xigushi.com/%s/list_%d_%d.html' % (type_, num, count)
		https.append(url)
	#url = 'http://www.xigushi.com/thgs/list_2_1.html'
	for url in https:
		page = https.index(url) + x
		os.mkdir('D:\\Sublime_Text_output\\py\\requests\\故事\\download\\第%d页\\' % page)
		list_d = []
		list_n = []
		response = requests.get(url = url, timeout = 30000)
		response.encoding = response.apparent_encoding
		html = BeautifulSoup(response.text, 'html.parser')
		a = html.find_all('ul', class_ = '')[1].find_all('a')
		for name in a:
			list_n.append(name.string)
			list_d.append('http://www.xigushi.com' + name['href'])
		#url = 'http://www.xigushi.com/thgs/13857.html'
		for name in list_n:
			count_name = list_n.index(name)
			text = get_text(list_d[count_name])
			if name.find(':') >= 1:
				name = name.replace(':', '')
			if name.find('?') >= 1:
				name = name.replace('?', '')
			if name.find('"') >= 1:
				name = name.replace('"', '')
			try:
				write_txt(msg = text, code = code, name = ('第%d页' % page + '\\' + name))
				print(name + '   Done')
				#sys.stdout.write('已下载:%.3f%%' % (float(count_name / len(range(x, y + 1))) * 100) + '\r')
			except:
				print('error')

get_list_url_and_write(1, 31, 'yqgs', 1)
