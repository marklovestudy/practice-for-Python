from tkinter import *
def gm():                                           #创建gm函数
    global v                                        #申明全局变量
    price=eval(s1.get())                            #提供字符里的数字
    thing=v.index(s2.get())+1                       #查找您选择的元素的索引号+1
    money=thing*price*100000                        #计算一共要花多少钱
    l1.config(text="你总共要花费%s元"%money)           #设置显示模块上的显示内容
win=Tk()                                            #创建Tk窗口
s1=Spinbox(win,from_=0,to=20)                       #创建Spinbox对象s1，用来选择货物    传数字用from_最小值   to最大值
s1.pack()                                           #打包s1
v=['手机','电脑','汽车','枪','飞机','火车','油船']       #创建货物列表
s2=Spinbox(win,values=v)     #物品                    #创建Spinbox对象s2，用来选择数量  传字符串可用序列传值
s2.pack()                                           #打包s1
Button(win,text='购买',comman=gm).pack()              #创建按钮模块          text指文本，comman指调用命令
l1=Label(win)                                       #创建显示模块l1
l1.pack()                                           #打包
win.mainloop()                                      #内置主循环

