def zhishu(num):
	for i in range(2,num):
		if num % i == 0:
			return True  #合数
	else:
		return False  #质数

def add(x):
	nump = x
	zs = []
	while x > 1:
		if not zhishu(x):
			zs.append(x)
		x -= 1
	zs = sorted(zs)
	str1 = ''
	for i in range(len(zs)):
		if i == 0:
			str1 = str1 + str(zs[i])
		else:
			str1 = str1 + ' ' + str(zs[i])
	result = '小于%d的质数有：%s  共%d个' % (nump, str1, len(zs))
	return result

print(add(100))