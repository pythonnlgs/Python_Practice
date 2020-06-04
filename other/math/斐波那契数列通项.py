a = 5 ** (1/2)
b_1, b_2 = 1 + a, 1 - a
c_1, c_2 = b_1 / 2, b_2 / 2

def F(num):
	d_1, d_2 = c_1 ** num, c_2 ** num
	e = d_1 - d_2
	r = e / a
	r = int(r)
	return r

print(F(1474))