import requests
from bs4 import BeautifulSoup
import time
import os
import sys

class poem(object):
	def __init__(self):
		'''
		初始化
		'''
		self.list_d = []
		self.dict_n = {}

	def write_txt(self, name, code, msg):
		'''
		写入文件
		'''
		#global path_
		path_ = 'D:\\Sublime_Text_output\\py\\requests\\poem\\download\\'
		real_path = path_ + name + '.txt'
		file_open = open(real_path, 'w+', encoding = code, errors = 'ignore')
		file_open.write(msg)
		file_open.close()

	def get_list(self, url):
		'''
		获取当前URL下所有链接
		'''
		#url = 'https://www.gushimi.org/gushi/index.html'
		global code
		response = requests.get(url = url)
		response.encoding = response.apparent_encoding
		code = response.apparent_encoding
		html = BeautifulSoup(response.text, 'html.parser')
		result = html.find_all('div', class_ = 'news_title')
		for k in result:
			href = 'https://www.gushimi.org' + k.find_all('a')[0]['href']
			self.list_d.append(href)
			self.dict_n[href] = k.string
		#print(dict_n)
	
	def get_text(self, url):
		'''
		获取当前URL下文字正文
		'''
		#url = 'https://www.gushimi.org/gushi/384861.html'
		global code
		response = requests.get(url = url)
		response.encoding = response.apparent_encoding
		code = response.apparent_encoding
		html = BeautifulSoup(response.text, 'html.parser')
		result = html.find_all('div', class_ = 'newstext')[0].text
		print(result)
		return result

	def main(self, x, y):
		'''
		主函数
		'''
		https = []
		for i in range(x, y + 1):
			if i == 1:
				html = 'https://www.gushimi.org/gushi/index.html'
			else:
				html = 'https://www.gushimi.org/gushi/index_%d.html' % i
			https.append(html)
		#count = 0
		for links in https:
			#count += 1
			page = https.index(links) + x
			os.mkdir('D:\\Sublime_Text_output\\py\\requests\\poem\\download\\第%d页\\' % page)
			poem.get_list(self, url = links)
			for k in self.list_d:
				name = '第' + str(page) + '页\\' + self.dict_n[k]
				poem.write_txt(self, code = code, msg = poem.get_text(self, k), name = name)
				time.sleep(0.5)
			self.list_d = []
			self.dict_n = {}


p = poem()
p.main(1, 20)