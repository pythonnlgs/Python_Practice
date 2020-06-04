def zhishu(num):
	for i in range(2,num):
		if num % i == 0:
			return True  #合数
	else:
		return False  #质数

def add(x):
	zs = []
	count = 2
	while not len(zs) == x:
		if not zhishu(count):
			zs.append(count)
		count += 1
	str1 = ''
	for i in range(len(zs)):
		if i == 0:
			str1 = str1 + str(zs[i])
		else:
			str1 = str1 + ' ' + str(zs[i])
	result = '前%d个质数分别是:%s' % (x, str1)
	return result

print(add(25))