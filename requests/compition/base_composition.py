import requests
from bs4 import BeautifulSoup
import time
import os
import sys

def setting():
	list_d = []
	list_n = []
	code = ''

def get_http(list_url):
	setting()
	global list_n, list_d, code
	url = list_url
	response = requests.get(url = url, timeout = 300000)
	response.encoding = response.apparent_encoding
	#code = response.apparent_encoding
	r = response.text
	re = BeautifulSoup(r, 'html.parser')
	#resul = re.find_all('div', class_ = 'artbox_1')
	res = re.find_all('div', class_ = 'wrapper clearfix')
	ro = res[1].find_all('div', class_ = 'artlist')
	resu = ro[0].find_all('a', target = '_blank')
	#print(resu)
	li_re = resu[1: 21]
	list_d = []
	list_n = []
	for k in li_re:
		#print(k['title'], k['href'])
		list_d.append(k['href'])
		list_n.append(k['title'])


def write_txt(name, msg, code, path):
	file = open(('D:\\Sublime_Text_output\\py\\requests\\作文\\download\\' + path + name + '.txt'), 'w+', encoding = code, errors = 'ignore')
	file.write(msg)
	file.close()
	#print(name, 'Finished!')

def get_http_shi(url):
	setting()
	global list_n, list_d, code
	response = requests.get(url = url, timeout = 300000)
	response.encoding = response.apparent_encoding
	code = response.apparent_encoding
	r = response.text
	re = BeautifulSoup(r, 'html.parser')
	result = re.find_all('div', class_ = 'wrapper clearfix')[0].find_all('ul')[0].find_all('a')
	#print(result)
	list_d = []
	list_n = []
	for m in result:
		list_d.append(m['href'])
		list_n.append(m.string)

def get_text(list_url, path, type_):
	path_d = 'D:\\Sublime_Text_output\\py\\requests\\作文\\download\\'
	os.mkdir(path_d + path)
	global code
	str1 = ''
	if type_ == 'zuowen':
		get_http(list_url)
	else:
		get_http_shi(list_url)
	count = 0
	for j in list_d:
		url = j
		response = requests.get(url = url, timeout = 300000)
		response.encoding = response.apparent_encoding
		code = response.apparent_encoding
		#print(code)
		r = response.text
		re = BeautifulSoup(r, 'html.parser')
		res = re.find_all('div', class_ = 'con_content')
		result = res[0].text.replace('　　', '\n')
		#print(result)
		wz = list_d.index(j)
		name = list_n[wz]
		if name.find(':') >= 1:
			name = name.replace(':', ' ')
		if name.find('?') >= 1:
			name = name.replace('?', '')
		if name.find('"') >= 1:
			name = name.replace('"', '')
		write_txt(name, result, code, path)
		count += 1
		sys.stdout.write("  已下载:%.3f%%" % (float(count / len(list_d)) * 100) + '\r')
		time.sleep(0.6)
