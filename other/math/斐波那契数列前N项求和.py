a = 5 ** (1/2)
b_1, b_2 = 1 + a, 1 - a
c_1, c_2 = b_1 / 2, b_2 / 2

def F(num):
	d_1, d_2 = c_1 ** num, c_2 ** num
	e = d_1 - d_2
	r = e / a
	r = int(r)
	return r

def G(x):
	re_1 = F(x + 2)
	re_2 = re_1 - 1
	return re_2

print(F(10))
print(G(1472))