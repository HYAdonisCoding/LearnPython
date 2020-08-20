#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        # self.createWidgets()
        # self.createWidgetsByInput()
        self.createWidgetByList()
        
    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello , world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

    def createWidgetsByInput(self):
        self.nameInput = Entry(self, bd=5)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Coming', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)


    def createWidgetByList(self):
        self.init_window_name.title("文本处理工具_v1.2")
        root = Tk()
        li = ['C', 'python', 'php', 'html', 'SQL', 'java']
        movie = ['CSS', 'jQuery', 'Bootstrap']
        listb = Listbox(root)  # 创建两个列表组件
        listb2 = Listbox(root)
        for item in li:  # 第一个小部件插入数据
            listb.insert(0, item)

        for item in movie:  # 第二个小部件插入数据
            listb2.insert(0, item)

        listb.pack()
        listb2.pack()

app = Application()

# 设置窗口标题
app.master.title('World Window')
# 主消息循环
app.mainloop()