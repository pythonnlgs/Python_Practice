import math
def C(m, n):
	up = math.factorial(m)
	un = math.factorial(m - n) * math.factorial(n)
	result = up / un
	result = int(result)
	r = '%s = %d' % ('c' + str(m) + ' ' + str(n), result)
	return r

def A(m, n):
	up = math.factorial(m)
	un = math.factorial(m - n)
	result = up / un
	result = int(result)
	r = '%s = %d' % ('A' + str(m) + ' ' + str(n), result)
	return r

print(C(6, 5))
print(A(6, 5))