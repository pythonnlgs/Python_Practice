import requests
from bs4 import BeautifulSoup as bsp
import os
from threading import Thread
import json

class download_poem(object):
	def __init__(self, page, _path, httptype):
		self.page = 'https://so.gushiwen.org/%s.aspx' % page
		print(self.page)
		self.realpath = 'download\\%s\\' % _path
		self.httptype = httptype
		try:
			os.mkdir(self.realpath)
		except:
			print('mkdir faild.')

	def get_list(self):
		#url = 'https://so.gushiwen.org/gushi/xiaoxue.aspx'
		response = requests.get(url = self.page)
		response.encoding = response.apparent_encoding
		result = bsp(response.text, 'html.parser').\
		         find_all('div', class_ = 'typecont')
		#print(result)

		lll = []
		for p in result:
			_dict = {}
			try:
				_dict['group'] = p.find_all('strong')[0].text
			except IndexError:
				_dict['group'] = 'None'
			dd = p.find_all('span')
			hh = []
			for m in dd:
				#print(m)
				try:
					if not self.httptype:
						hh.append({'name': m.text,
							       'link': m.find_all('a')[0]['href']})
					else:
						hh.append({'name': m.text,
							       'link': 'https://so.gushiwen.org' +\
							       m.find_all('a')[0]['href']})	
				except:
					pass
			_dict['links'] = hh
			lll.append(_dict)
		#print(lll[1])
		return lll

	def get_and_write_cont(self):
		def _write(pn, msg):
			try:
				with open(pn, 'w+', encoding = 'utf8') as f:
					f.write(msg)
			except:
				print('write file faild.')

		def _getcont(url):
			#url = 'http://so.gushiwen.org/shiwenv_1585dd289ef9.aspx'
			response = requests.get(url = url)
			response.encoding = 'utf8'
			#print(response.encoding)
			html = bsp(response.text, 'html.parser')
			result = html.find_all('div', class_ = 'contson')\
			         [0].text.replace('\n', '')
			#print(result)
			return result

		def _prosess(_dict):
			hhh = self.realpath + _dict['group'] + '\\'
			try:
				os.mkdir(hhh)
			except:
				print('mkproupdir faild.')
			for q in _dict['links']:
				pn = hhh + q['name'] + '.txt'
				_cont = _getcont(q['link'])
				_write(pn = pn, msg = _cont)
				#time.sleep(0.6)
				print('%s:\n%sfinished!' % (pn, _cont))

		def mainth():
			pbl = []
			for k in self.get_list():
				ttt = Thread(target = _prosess, args = (k,))
				ttt.start()

		mainth()


class PackageError(Exception):
	def __init__(self, s):
		pass


def main(file):
	try:
		f = open(file, 'r', encoding = 'utf-8')
		try:
			_list = json.load(f)
			for b in _list:
				pp = download_poem(b['page'], b['path'], b['httptype'])
				thh = Thread(target = pp.get_and_write_cont, args = ())
				thh.start()
		except:
			raise PackageError('System can not load "%s", please check your config.' % file)
		finally:
			f.close()
	except FileNotFoundError:
		raise PackageError('System can not found "%s", please check your config.' % file)

if __name__ == '__main__':
	main('config.json')