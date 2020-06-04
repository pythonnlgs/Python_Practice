def fibo(n):
	a, b = 0, 1
	for i in range(n):
		a,b = b, a + b
		print(a,end='\t')
#n = eval(input("请输入一个整数："))
print('斐波那契前n项'.center(20,'-'))
fibo(6)