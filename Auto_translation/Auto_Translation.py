#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:20161047012  阳小兰


import tkinter
import os
import urllib.request
import urllib.parse
import json
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import time
import random

class YouDaoFanyi(object):
    def __init__(self):
        pass
    def crawl(self,word):
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/'
        data = {}
        head={}
        head['User-Agent']='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        data['type'] = 'AUTO'
        data['i'] = word
        data['doctype'] = 'json'
        data['Version'] = '2.1'
        data['keyfrom'] = 'fanyi.web'
        data['ue'] = 'UTF-8'
        data['action'] = 'FY_BY_CLICKBUTTON'
        data['typoResult'] = 'true'

        data = urllib.parse.urlencode(data).encode('utf-8')
        req =urllib.request.Request(url,data,head)
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        target = json.loads(html)
        result = target['translateResult'][0][0]['tgt']
        return result

class Login(object):

    
    def __init__(self):
        
        self.fanyi = YouDaoFanyi()
    
        # 创建主窗口,用于容纳其它组件 
        self.root = tkinter.Tk()
        self.root.title("在线翻译_有道")
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        w = 500
        h = 253
        x = (ws/2) - (w/2) 
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y-100))
        self.root.resizable(width=False, height=False)
        #设置背景
        self.photo=tkinter.PhotoImage(file=r"welcome.gif")
        self.label=tkinter.Label(self.root,image=self.photo)  #图片
        self.label.pack()
        
        #设置下拉列表
        self.comvalue=tkinter.StringVar()#窗体自带的文本，新建一个值
        self.comboxlist=ttk.Combobox(self.root,textvariable=self.comvalue) #初始化
        self.comboxlist["values"]=("自动检测语言")
        self.comboxlist.current(0)  #选择第一个
        self.comboxlist.bind("<<ComboboxSelected>>")  #绑定事件,(下拉列表框被选中时，绑定go()函数)
        self.comboxlist.place(x = 20,y = 40,width = 100,height = 20)
        
        #创建一个文本框
        self.result_text1 = Text(self.root,background = '#FFFFCE')
        self.result_text1.place(x = 20,y = 120,width = 220,height = 80)
        self.result_text1.bind("<Key-Return>",self.submit)

        #创建两个按钮
        #为按钮添加事件
        self.submit_btn = Button(self.root,text=u'翻译',bg='#FF0000',fg='white',activeforeground='white',activebackground='#CE0000',command=self.submit)
        self.submit_btn.place(x=320,y=215,width=70,height=25)
        self.submit_btn2 = Button(self.root,text=u'清空',bg='#FF0000',fg='white',activeforeground='white',activebackground='#CE0000',command = self.clean)
        self.submit_btn2.place(x=410,y=215,width=70,height=25)


        #翻译内容标题
        self.title_label = Label(self.root,text=u'翻译内容:',bg='#FFFFCE')
        self.title_label.place(x=20,y=85)
        #翻译结果标题
        self.title_label = Label(self.root,text=u'翻译结果:',bg='#FFFFCE')
        self.title_label.place(x=260,y=85)
        
        #设置一个文本框
        self.result_text = Text(self.root,background = '#FFFFCE')
        self.result_text.place(x = 260,y = 120,width = 220,height = 80)
    #开始翻译
    def submit(self,*event):
            #从输入框获取用户输入的值
            content = self.result_text1.get(0.0,END).strip().replace("\n"," ")
            #把这个值传送给服务器进行翻译
            result = self.fanyi.crawl(content)
            #将结果显示在窗口中的文本框中
            self.result_text.delete(0.0,END)
            self.result_text.insert(END,result)
            
    #清空文本域中的内容
    def clean(self):
        self.result_text1.delete(0.0,END)
        self.result_text.delete(0.0,END)


def main():   
    L = Login()  
    tkinter.mainloop()
    
if __name__=='__main__':
    main()
    
