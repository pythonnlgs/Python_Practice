import os

def mingming(dir_):
	os.chdir(dir_)
	print(os.getcwd())
	li = os.listdir(os.getcwd())
	for img in li:
		print(img)
		if '.mp4' in img:
			os.rename(img, str(li.index(img) + 1) + '.mp4')
		elif '.png' in img:
			os.rename(img, str(li.index(img) + 1) + '.jpg')
		elif '.jpg' in img:
			os.rename(img, str(li.index(img) + 1) + '.jpg')
		elif '.JPG' in img:
			os.rename(img, str(li.index(img) + 1) + '.jpg')
		elif '.jpeg' in img:
			os.rename(img, str(li.index(img) + 1) + '.jpg')

for i in range(20):
	print('rename already!')

if __name__ == '__main__':
	mingming(r'F:\照片\杂货照片\other')