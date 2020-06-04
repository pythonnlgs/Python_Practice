import requests
from bs4 import BeautifulSoup as bsp
from threading import Thread
import os

class downloadppt_img(object):
	def __init__(self, page, yangshi, pth):
		self.page = page
		self.yangshi = yangshi
		self.pth = pth
		self.realpath = 'download\\' + self.pth
		try:
			os.mkdir(self.realpath)
		except OSError:
			print('mkdir faild.')

	def get_list(self, d):
		if d == 1:
			url = 'http://www.1ppt.com/beijing/%s/'\
			      % self.page
		else:
			url = 'http://www.1ppt.com/beijing/%s/%s%d.html'\
			      % (self.page, self.yangshi, d)
		response = requests.get(url = url)
		response.encoding = 'gbk'
		result = bsp(response.text, 'html.parser')\
		         .find_all('ul', class_ = 'tplist')[0]\
		         .find_all('li')
		lll = []
		for m in result:
			lll.append(['http://www.1ppt.com'\
				       + m.find_all('a')[0]['href'],\
				       m.find_all('a')[0].\
				       find_all('img')[0]['alt']])
		print(lll)
		return lll

	def writeimg(self, name, url):
		response = requests.get(url = url)
		with open(name, 'wb+') as f:
			f.write(response.content)

	def getimg(self, url):
		#url = 'http://www.1ppt.com/article/55041.html'
		response = requests.get(url = url)
		response.encoding = 'gbk'
		result = bsp(response.text, 'html.parser')\
		         .find_all('div', class_ = 'content')[0]\
		         .find_all('p')[0].find_all('img')
		#print(result)
		lll = []
		for x in result:
			lll.append([x['src'], '_' + str(result.index(x) + 1) + '.jpg'])
		#print(lll)
		return lll

	def mainth(self, d):
		thispath = self.realpath + 'p' + str(d) + '\\'
		try:
			os.mkdir(thispath)
		except OSError:
			print('mkdir faild.')
		for nn in self.get_list(d = d):
			try:
				print(nn[0])
				nnn = nn[1]
				for xx in self.getimg(nn[0]):
					name = thispath + nnn + xx[1]
					print(xx[0])
					self.writeimg(name = name, url = xx[0])
			except:
				pass

class downloadppt_img_run(object):
	def th1(self, a, b):
		down = downloadppt_img('xingkong', 'ppt_xingkong_', '星空\\')
		for p in range(a, b + 1):
			th = Thread(target = down.mainth, args = (p,))
			th.start()

	def th2(self, a, b):
		down = downloadppt_img('xiexie', 'ppt_xiexie_', '谢谢\\')
		for p in range(a, b + 1):
			th = Thread(target = down.mainth, args = (p,))
			th.start()

	def th3(self, a, b):
		down = downloadppt_img('zhongguofeng', 'ppt_zhongguofeng_', '中国风\\')
		for p in range(a, b + 1):
			th = Thread(target = down.mainth, args = (p,))
			th.start()

	def mainrun(self):
		th_1 = Thread(target = th1, args = (1, 4))
		th_2 = Thread(target = th2, args = (1, 3))
		th_3 = Thread(target = th3, args = (1, 9))
		pan = [th_1, th_2, th_3]
		for j in pan:
			j.start()

class downloadppt_moban