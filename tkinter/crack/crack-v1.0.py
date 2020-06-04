try:
	import os
	from tkinter import *
	from tkinter import messagebox
	import time
except:
	pass

class crack(object):
	def __init__(self):
		self.root = Tk()
		self.root.resizable(0,0)  
		self.root.geometry('300x200')
		self.root.title('Crack Tool v1.0')
		self.label = Label(text = '程序名：')
		self.label.place(x = 0, y = 10)
		self.in_exe = Entry(self.root)
		self.in_exe.place(x = 60, y = 10)
		self.name = ''
		self.type_messagebox = False
		self.type_crack = False

	def bool(self, ty):
		if ty:
			return 'True'
		elif not(ty):
			return 'False'
		else:
			return None

	def flush_f(self):
		self.name = self.in_exe.get()
		print(self.name)

	def on_messagebox(self):
		self.type_messagebox = True

	def off_messagebox(self):
		self.type_messagebox = False

	def on_crack(self):
		self.type_crack = True
		while self.type_crack:
			command = 'taskkill /f /im %s' % self.name
			os.system(command)
			if self.type_messagebox:
				messagebox.showinfo(title = 'Already crack!', message = self.name)
				time.sleep(1)
			else:
				time.sleep(1)

	def off_crack(self):
		self.type_crack = False

	def test(self):
		str_ = 'name:' + self.name + '\n' + 'type_messagebox:' + \
		       self.bool(self.type_messagebox) + '\n' + \
		       'type_crack:' + self.bool(self.type_crack)
		messagebox.showinfo(title = 'mgr', message = str_)

	def main(self):	
		self.turn_on_messagebox = Button(text = '开启破解通知', command = self.on_messagebox)
		self.turn_on_messagebox.place(x = 0, y = 170)
		self.turn_off_messagebox = Button(text = '关闭破解通知', command = self.off_messagebox)
		self.turn_off_messagebox.place(x = 100, y = 170)
		self.turn_on_messagebox = Button(text = '开启无限关闭', command = self.on_crack)
		self.turn_on_messagebox.place(x = 0, y = 140)
		self.turn_off_messagebox = Button(text = '关闭无限关闭', command = self.off_crack)
		self.turn_off_messagebox.place(x = 100, y = 140)
		self.flush_ = Button(text = '确定', command = self.flush_f)
		self.flush_.place(x = 230, y = 5)
		self.test_b = Button(text = 'mgr', command = self.test)
		self.test_b.place(x = 265, y = 170)
		self.root.mainloop()

if __name__ == '__main__':
	a = crack()
	a.main()
