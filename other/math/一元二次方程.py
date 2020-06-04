print('ax^2+bx+c=0')

def func_1_2(a, b, c):
	un = a * 2
	up_1 = b * (-1)
	up_2_a = b ** 2
	up_2_b = 4 * a * c
	up_2_c = up_2_a - up_2_b
	if up_2_c < 0:
		return('错误！！！')
	else:
		up_2_d = up_2_c ** (1/2)
		x = up_1 + up_2_d
		y = up_1 - up_2_d
		result_1 = x / un
		result_2 = y / un
		return result_1, result_2

print(func_1_2(2, -1, -1))