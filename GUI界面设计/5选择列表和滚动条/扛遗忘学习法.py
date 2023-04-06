
def p():
    global v
    str1=''
    str2=''
    str3 = '知识库：'
    for k,vl in v.items():              #遍历字典
        time_long=time.time()-vl
        if time_long<3600*24:
            str1 += k + '  '
            l1.config(text=str1)
        if time_long<3600*48 or \
                (3600*24*3<time_long and time_long<3600*24*4) \
                or (3600*24*7<time_long and time_long<3600*24*8) or \
                (3600*24*15<time_long and time_long<3600*24*16) or \
                (3600*24*30<time_long and time_long<3600*24*31):
            str2 += k + '  '
            l2.config(text=str2,wraplength=300)
        str3 += k + '  '
        l3.config(text=str3, wraplength=300)

def write_in():
    global v
    with open('study.json','r',encoding='utf-8') as f:
        v = json.load(f)
        print(v)
    print(e1.get())
    if e1.get() not in v.keys():
        v[e1.get()] = time.time()
    if e1.get() in v.keys():
        l1.config(text='已存在')
        time.sleep(1)
    with open('study.json','w',encoding='utf-8') as f:
        json.dump(v,f)
    p()

def write_out():
    global v
    with open('study.json', 'r', encoding='utf-8') as f:
        v = json.load(f)
    if e1.get() in v.keys():
        v.pop(e1.get())
    with open('study.json','w',encoding='utf-8') as f:
        json.dump(v,f)
    p()

from tkinter import *
import time
import json
v = dict()

win=Tk()
win.title('扛遗忘学习法')
e1=Entry(win,width=10)
e1.grid(row=0,column=0,columnspan=3,sticky=W+E,padx=10,pady=10)
b1=Button(win,text='存入',command=write_in)
b1.grid(row=0,column=3,sticky=W+E,padx=10,pady=10)
b2=Button(win,text='删除',command=write_out)
b2.grid(row=0,column=4,sticky=W+E,padx=10,pady=10)
Label(win,text='今天新学内容：').grid(row=1,column=0,columnspan=5,sticky=W+E,padx=10,pady=10)
l1=Label(win,width=40,height=2,bg='pink')
l1.grid(row=2,column=0,columnspan=5,sticky=W+E,padx=10,pady=10)
Label(win,text='今天需要温习的内容：').grid(row=3,column=0,columnspan=5,sticky=W+E,padx=10,pady=10)
l2=Label(win,width=40,height=5,bg='pink')
l2.grid(row=4,column=0,columnspan=5,sticky=W+E,padx=10,pady=10)
l3=Label(win,text='知识库：',width=40,height=5,bg='pink')
l3.grid(row=5,column=0,columnspan=5,sticky=W+E,padx=10,pady=10)
win.mainloop()