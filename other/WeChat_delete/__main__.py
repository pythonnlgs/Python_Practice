import time
import os
import delete
import get_all
import json

dir1 = 'D:\\WeChatDownload\\WeChat Files\\vincentilove\\FileStorage\\Image'
dir2 = 'D:\\WeChatDownload\\WeChat Files\\vincentilove\\FileStorage\\File'
dir3 = 'D:\\WeChatDownload\\WeChat Files\\vincentilove\\FileStorage\\CustomEmotion'
dir4 = 'D:\\WeChatDownload\\WeChat Files\\vincentilove\\FileStorage\\Video'
dir5 = 'D:\\WeChatDownload\\WeChat Files\\vincentilove\\FileStorage\\Cache'

'''
def write_json(msg, name):
	with open('D:\\Sublime_Text_output\\py\\WeChat\\data\\' + name + '.json', 'w+') as file:
		file.write(msg)
		file.close()
	return ('D:\\Sublime_Text_output\\py\\WeChat\\data\\' + name + '.json')
'''

def judge(li1, li2):
	'''
	li1->big
	li2->small
	'''
	result_ = []
	for l1 in li1:
		if not l1 in li2:
			result_.append(l1)
	return result_


def __clear__(dir_, name):
	result1 = []
	get_all.listDir(dir_, result1)
	#str_json = json.dumps(result, indent = 4)
	#file1 = write_json(str_json, name + '_a')
	delete.delete(dir_)
	result2 = []
	get_all.listDir(dir_, result2)
	#str_json = json.dumps(result, indent = 4)
	#file2 = write_json(str_json, name + '_b')
	print(len(judge(result1, result2)))
	return len(judge(result1, result2))

def main():
	len1 = __clear__(dir1, 'Image')
	len2 = __clear__(dir2, 'File')
	len3 = __clear__(dir3, 'CustomEmotion')
	len4 = __clear__(dir4, 'Video')
	len5 = __clear__(dir5, 'Cache')
	len_h = len1 + len2 + len3 + len4 + len5
	print('共%d个文件' % len_h)
	return len_h

if __name__ == '__main__':
	count = 0
	con_h = 0
	while True:
		try:
			con_h += main()
			count += 1
			print('已删除%d次' % count)
			print('累计删除%d个文件' % con_h)
			time.sleep(30)
		except:
			print('Error')