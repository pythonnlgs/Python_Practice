import base_composition as b
import os

page_dict = {}
page_list = []
#p = 0
def make_page_list(x, y):
	global page_list
	for i in range(x, y + 1):
		#p = i
		page_list.append(i)
		print(i)
		if i == 1:
			http = 'http://www.zuowen.com/yingyuzw/ksyingyu/zkyy/index.shtml'
		else:
			http = 'http://www.zuowen.com/yingyuzw/ksyingyu/zkyy/index_%d.shtml' % i
		#print(http)
		page_dict[i] = http
	return page_dict

def th(a, c):
	print(make_page_list(a, c))
	for page in page_list:
		name = ('第%d页' % page) + '\\'
		url = page_dict[page]
		try:
			b.get_text(url, name, 'zuowen')
			print(page, 'finished!')
		except:
			print('Error')

#th(41, 50)


def shi(url, name):
	#url = 'http://www.zuowen.com/shici/gushici/……/'
	b.get_text(url, '%s\\' % name, 'shici')

shi('http://www.zuowen.com/shici/wenyanwen/chuzhong/', '初中文言文')
