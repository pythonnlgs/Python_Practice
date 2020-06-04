import os
import shutil
'''
dir1 = 'D:\\WeChatDownload\\WeChat Files\\vincentilove\\FileStorage\\Image\\2020-02'
dir2 = 'D:\\WeChatDownload\\WeChat Files\\vincentilove\\FileStorage\\Image\\Thumb\\2020-02'
'''
def delete(dir_):
	files1 = os.listdir(dir_)
	for listfile1 in files1:
		filepath1 = os.path.join(dir_,listfile1)
		try:
			os.remove(filepath1)
		except PermissionError:
			shutil.rmtree(filepath1)