import random
import re

class RandRe(object):
	def __init__(self):
		self._BIG = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
		             'l', 'i', 'j', 'k', 'l', 'm', 'n',
		             'o', 'p', 'q', 'r', 's', 't', 'u',
		             'v', 'w', 'x', 'y', 'z']

		self._SMALL = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
		               'L', 'I', 'J', 'K', 'L', 'M', 'N',
		               'O', 'P', 'Q', 'R', 'S', 'T', 'U',
		               'V', 'W', 'X', 'Y', 'Z']

		self._ZHUANYI = [r'[\!]', r'[\@]', r'[\#]', r'[\$]',
		               r'[\%]', r'[\^]', r'[\&]', r'[\*]',
		               r'[\(]', r'[\)]', r'[\-]', r'[\_]',
		               r'[\=]', r'[\+]', r'[\{]', r'[\}]',
		               r'[\[]', r'[\]]', r'[\|]', r'[\:]',
		               r'[\;]', r'[\"]', r'[\']', r'[\<]',
		               r'[\>]', r'[\,]', r'[\.]', r'[\?]',
		               r'[\/]', r'[\~]', r'[\`]']

		self._NUM = ['0-1', '0-2', '0-3', '0-4', '0-5',
		             '0-6', '0-7', '0-8', '0-9', '1-2',
		             '1-3', '1-4', '1-5', '1-6', '1-7',
		             '1-8', '1-9', '2-3', '2-4', '2-5',
		             '2-6', '2-7', '2-8', '2-9', '3-4',
		             '3-5', '3-6', '3-7', '3-8', '3-9',
		             '4-5', '4-6', '4-7', '4-8', '4-9',
		             '5-6', '5-7', '5-8', '5-9', '6-7',
		             '6-8', '6-9', '7-8', '7-9', '8-9']

		self._LETTERS = ['a-b', 'a-c', 'a-d', 'a-e', 'a-f', 'a-g',
		                'a-h', 'a-i', 'a-j', 'a-k', 'a-l', 'a-m',
		                'a-n', 'a-o', 'a-p', 'a-q', 'a-r', 'a-s',
		                'a-t', 'a-u', 'a-v', 'a-w', 'a-x', 'a-y',
		                'a-z', 'b-c', 'b-d', 'b-e', 'b-f', 'b-g',
		                'b-h', 'b-i', 'b-j', 'b-k', 'b-l', 'b-m',
		                'b-n', 'b-o', 'b-p', 'b-q', 'b-r', 'b-s',
		                'b-t', 'b-u', 'b-v', 'b-w', 'b-x', 'b-y',
		                'b-z', 'c-d', 'c-e', 'c-f', 'c-g', 'c-h',
		                'c-i', 'c-j', 'c-k', 'c-l', 'c-m', 'c-n',
		                'c-o', 'c-p', 'c-q', 'c-r', 'c-s', 'c-t',
		                'c-u', 'c-v', 'c-w', 'c-x', 'c-y', 'c-z',
		                'd-e', 'd-f', 'd-g', 'd-h', 'd-i', 'd-j',
		                'd-k', 'd-l', 'd-m', 'd-n', 'd-o', 'd-p',
		                'd-q', 'd-r', 'd-s', 'd-t', 'd-u', 'd-v',
		                'd-w', 'd-x', 'd-y', 'd-z', 'e-f', 'e-g',
		                'e-h', 'e-i', 'e-j', 'e-k', 'e-l', 'e-m',
		                'e-n', 'e-o', 'e-p', 'e-q', 'e-r', 'e-s',
		                'e-t', 'e-u', 'e-v', 'e-w', 'e-x', 'e-y',
		                'e-z', 'f-g', 'f-h', 'f-i', 'f-j', 'f-k',
		                'f-l', 'f-m', 'f-n', 'f-o', 'f-p', 'f-q',
		                'f-r', 'f-s', 'f-t', 'f-u', 'f-v', 'f-w',
		                'f-x', 'f-y', 'f-z', 'g-h', 'g-i', 'g-j',
		                'g-k', 'g-l', 'g-m', 'g-n', 'g-o', 'g-p',
		                'g-q', 'g-r', 'g-s', 'g-t', 'g-u', 'g-v',
		                'g-w', 'g-x', 'g-y', 'g-z', 'h-i', 'h-j',
		                'h-k', 'h-l', 'h-m', 'h-n', 'h-o', 'h-p',
		                'h-q', 'h-r', 'h-s', 'h-t', 'h-u', 'h-v',
		                'h-w', 'h-x', 'h-y', 'h-z', 'i-j', 'i-k',
		                'i-l', 'i-m', 'i-n', 'i-o', 'i-p', 'i-q',
		                'i-r', 'i-s', 'i-t', 'i-u', 'i-v', 'i-w',
		                'i-x', 'i-y', 'i-z', 'j-k', 'j-l', 'j-m',
		                'j-n', 'j-o', 'j-p', 'j-q', 'j-r', 'j-s',
		                'j-t', 'j-u', 'j-v', 'j-w', 'j-x', 'j-y',
		                'j-z', 'k-l', 'k-m', 'k-n', 'k-o', 'k-p',
		                'k-q', 'k-r', 'k-s', 'k-t', 'k-u', 'k-v',
		                'k-w', 'k-x', 'k-y', 'k-z', 'l-m', 'l-n',
		                'l-o', 'l-p', 'l-q', 'l-r', 'l-s', 'l-t',
		                'l-u', 'l-v', 'l-w', 'l-x', 'l-y', 'l-z',
		                'm-n', 'm-o', 'm-p', 'm-q', 'm-r', 'm-s',
		                'm-t', 'm-u', 'm-v', 'm-w', 'm-x', 'm-y',
		                'm-z', 'n-o', 'n-p', 'n-q', 'n-r', 'n-s',
		                'n-t', 'n-u', 'n-v', 'n-w', 'n-x', 'n-y',
		                'n-z', 'o-p', 'o-q', 'o-r', 'o-s', 'o-t',
		                'o-u', 'o-v', 'o-w', 'o-x', 'o-y', 'o-z',
		                'p-q', 'p-r', 'p-s', 'p-t', 'p-u', 'p-v',
		                'p-w', 'p-x', 'p-y', 'p-z', 'q-r', 'q-s',
		                'q-t', 'q-u', 'q-v', 'q-w', 'q-x', 'q-y',
		                'q-z', 'r-s', 'r-t', 'r-u', 'r-v', 'r-w',
		                'r-x', 'r-y', 'r-z', 's-t', 's-u', 's-v',
		                's-w', 's-x', 's-y', 's-z', 't-u', 't-v',
		                't-w', 't-x', 't-y', 't-z', 'u-v', 'u-w',
		                'u-x', 'u-y', 'u-z', 'v-w', 'v-x', 'v-y',
		                'v-z', 'w-x', 'w-y', 'w-z', 'x-y', 'x-z',
		                'y-z']

		self._BASE = [r'\w', r'\d', r'\s',
		              r'\W', r'\D', r'\S', r'.']

		self._bools = [True, False]

	def _make_range(self):
		num = random.randint(1, 100)
		if num <= 30:
			b = random.randint(1, 4)
			e = random.randint(b, 4)
			return '{%d,%d}' % (b - 1, e)
		elif num <= 50:
			return r'+'
		elif num <= 60:
			return r'?'
		elif num <= 80:
			return r'*'
		else:
			return '{%d}' % random.randint(1, 3)

	def _make_other(self):
		_bool = random.choice(self._bools)
		if _bool:
		    return random.choice(self._BIG + self._SMALL + self._BASE)
		else:
			b_2 = random.randint(1, 6)
			if b_2 == 1:
				return '[%s]' % random.choice(self._LETTERS)
			elif b_2 == 2:
				return '[%s]' % random.choice(self._NUM)
			elif b_2 == 3:
				return '[%s%s]' % (random.choice(self._LETTERS), random.choice(self._NUM))
			elif b_2 == 4:
				return '%s' % random.choice(self._ZHUANYI)
			else:
				return random.choice(self._BASE)

	def ReKey(self, lenth):
		body = ''
		while len(body) <= lenth:
			x = random.choice(self._bools)
			if x:
				ls = self._make_other() + self._make_range()
				body += ls
			else:
				body += random.choice(self._BIG + self._SMALL + self._ZHUANYI)
				if random.choice(self._bools):
					body += self._make_range()
		return body
