from turtle import *
import random
screensize(1000, 1000, 'black')
speed(0)

def get_color():
	rgb = []
	for i in range(3):
		rgb.append(random.random())
	rgb = tuple(rgb)
	return rgb

def drow(size, step):
	for i in range(step):
		pencolor(get_color())
		forward(size)
		right(360 / step)

def drow_ci(size, step, num):
	for i in range(num):
		drow(size, step)
		right(360 / num)
	done()

while True:
	size = int(input('请输入图形边长：'))
	step = int(input('请输入图形边数：'))
	num = int(input('请输入图形个数：'))
	drow_ci(size, step, num)