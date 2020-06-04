from tkinter import *
from tkinter import messagebox
import downloadtool
import time

class _downloadtool():
	def __init__(self):
		self.root = Tk()
		self.root.resizable(0,0) 
		self.root.geometry('250x150')
		self.root.title('download tool v1.0')
		self.label1 = Label(text = '目标网站链接：')
		self.label1.place(x = 0, y = 10)
		self.label2 = Label(text = '线程数：')
		self.label2.place(x = 0, y = 40)
		self.label3 = Label(text = '文件名：')
		self.label3.place(x = 0, y = 70)
		self.in_url = Entry(self.root)
		self.in_url.place(x = 100, y = 10)
		self.in_th = Entry(self.root)
		self.in_th.place(x = 100, y = 40)
		self.in_name = Entry(self.root)
		self.in_name.place(x = 100, y = 70)
		#self.root.mainloop()

	def begin(self):
		try:
			st = time.time()
			down = downloadtool.downloader(url = self.in_url.get(), name = self.in_name.get(), num = int(self.in_th.get()))
			down.run()
			en = time.time()
			t = en - st
			messagebox.showinfo(title = 'success',message = '下载成功！\n文件大小:%d\n耗时%d秒\n平均速度：%d' % (down.total, t, (down.total / t)))
		except TypeError:
			messagebox.showinfo(title = 'Error', message = '请输入合法整数!')
	
	def main(self):
		self.bu = Button(text = '开始下载', command = self.begin)
		self.bu.place(x = 80, y = 120)
		self.root.mainloop()

if __name__ == '__main__':
	a = _downloadtool()
	a.main()