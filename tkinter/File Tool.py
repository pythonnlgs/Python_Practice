from tkinter import *
from tkinter import messagebox

class filetool():
	def __init__(self):
		self.root = Tk()
		self.root.resizable(0,0)  
		self.root.geometry('200x100')
		self.root.title('filetool v1.0')
		self.label1 = Label(text = '后缀:')
		self.label1.place(x = 5, y = 10)
		self.in_ = Entry(self.root)
		self.in_.place(x = 45, y = 10)
	
	def b(self):
		try:
			with open('.' + self.in_.get(), 'w+') as f:
				messagebox.showinfo(title = '成功！', message = '已成功创建文件')
		except Exception as e:
			messagebox.showinfo(title = 'Error', message = '后缀不能为空！')

	def main(self):
		self.bu = Button(text = '创建', command = self.b)
		self.bu.place(x = 75, y = 60)
		self.root.mainloop()

if __name__ == '__main__':
	a = filetool()
	a.main()
