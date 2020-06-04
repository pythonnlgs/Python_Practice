import turtle
import random

class MyTurtle(turtle.Turtle):
	def draw_square(self, x):
		self.setheading(x)
		for i in range(4):
			self.forward(x)
			self.left(90)
		return
#随机获取rgb模式下的颜色的三个参数
	def get_color(self):
		rgb = []
		for i in range(3):
			rgb.append(random.randint(0, 255))
		return rgb
#设置画笔的颜色    
	def set_pen_color(self):
		self.screen.colormode(255)
		self.pencolor(self.get_color())

t = MyTurtle()

t.screen.bgcolor("black")
t.speed(0)

# 遍历1~1000°内的所有角度，随着初始角度增大，正方形的边长也增大
x = 1
while x < 1000:
	t.set_pen_color()
	t.draw_square(x)
	x = x + 1

t.screen.mainloop()