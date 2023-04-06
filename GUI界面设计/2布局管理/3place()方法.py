'''
place()方法中的参数：
    1,x,y                       设置组件水平和重直距离
    2,width,height              设置组件宽度和高度
    3,relx,rely                 设置组件距离容器左侧和距离顶部的相对距离。数值范围(0~1)
    4,relwidth,relheight        组件相对父容器的宽度和高度。数值范围(0~1)

实例：华容道用x,y,width,height布局华容道
from tkinter import *
win = Tk()
win.title('华容道')
win.geometry('240x300')
l1 = Label(win,text='赵云',bg='pink',relief='groove',font=14)
l2 = Label(win,text='曹操',bg='pink',relief='groove',font=14)
l3 = Label(win,text='黄忠',bg='pink',relief='groove',font=14)
l4 = Label(win,text='张飞',bg='pink',relief='groove',font=14)
l5 = Label(win,text='关羽',bg='pink',relief='groove',font=14)
l6 = Label(win,text='马超',bg='pink',relief='groove',font=14)
l7 = Label(win,text='卒',bg='pink',relief='groove',font=14)
l8 = Label(win,text='卒',bg='pink',relief='groove',font=14)
l9 = Label(win,text='卒',bg='pink',relief='groove',font=14)
l0 = Label(win,text='卒',bg='pink',relief='groove',font=14)

l1.place(width=60,height=120,x=0,y=0)
l2.place(width=120,height=120,x=60,y=0)
l3.place(width=60,height=120,x=180,y=0)
l4.place(width=60,height=120,x=0,y=120)
l5.place(width=120,height=60,x=60,y=120)
l6.place(width=60,height=120,x=180,y=120)
l7.place(width=60,height=60,x=60,y=180)
l8.place(width=60,height=60,x=120,y=180)
l9.place(width=60,height=60,x=0,y=240)
l0.place(width=60,height=60,x=180,y=240)

win.mainloop()

实例：：华容道用relx,rely,relwidth,relheight布局华容道
from tkinter import *
win = Tk()
win.title('华容道')
win.geometry('240x300')
l1 = Label(win,text='赵云',bg='pink',relief='groove',font=14)
l2 = Label(win,text='曹操',bg='pink',relief='groove',font=14)
l3 = Label(win,text='黄忠',bg='pink',relief='groove',font=14)
l4 = Label(win,text='张飞',bg='pink',relief='groove',font=14)
l5 = Label(win,text='关羽',bg='pink',relief='groove',font=14)
l6 = Label(win,text='马超',bg='pink',relief='groove',font=14)
l7 = Label(win,text='卒',bg='pink',relief='groove',font=14)
l8 = Label(win,text='卒',bg='pink',relief='groove',font=14)
l9 = Label(win,text='卒',bg='pink',relief='groove',font=14)
l0 = Label(win,text='卒',bg='pink',relief='groove',font=14)

l1.place(relwidth=0.25,relheight=0.4,relx=0,rely=0)
l2.place(relwidth=0.5,relheight=0.4,relx=0.25,rely=0)
l3.place(relwidth=0.25,relheight=0.4,relx=0.75,rely=0)
l4.place(relwidth=0.25,relheight=0.4,relx=0,rely=0.4)
l5.place(relwidth=0.5,relheight=0.2,relx=0.25,rely=0.4)
l6.place(relwidth=0.25,relheight=0.4,relx=0.75,rely=0.4)
l7.place(relwidth=0.25,relheight=0.2,relx=0.25,rely=0.6)
l8.place(relwidth=0.25,relheight=0.2,relx=0.5,rely=0.6)
l9.place(relwidth=0.25,relheight=0.2,relx=0,rely=0.8)
l0.place(relwidth=0.25,relheight=0.2,relx=0.75,rely=0.8)

win.mainloop()
'''
from tkinter import *
win = Tk()
win.title('华容道')
win.geometry('240x300')
l1 = Label(win,text='赵云',bg='pink',relief='groove',font=14)
l2 = Label(win,text='曹操',bg='pink',relief='groove',font=14)
l3 = Label(win,text='黄忠',bg='pink',relief='groove',font=14)
l4 = Label(win,text='张飞',bg='pink',relief='groove',font=14)
l5 = Label(win,text='关羽',bg='pink',relief='groove',font=14)
l6 = Label(win,text='马超',bg='pink',relief='groove',font=14)
l7 = Label(win,text='卒',bg='pink',relief='groove',font=14)
l8 = Label(win,text='卒',bg='pink',relief='groove',font=14)
l9 = Label(win,text='卒',bg='pink',relief='groove',font=14)
l0 = Label(win,text='卒',bg='pink',relief='groove',font=14)
l1.place(width=60,height=120,x=0,y=0)
l2.place(width=120,height=120,x=60,y=0)
l3.place(width=60,height=120,x=180,y=0)
l4.place(width=60,height=120,x=0,y=120)
l5.place(width=120,height=60,x=60,y=120)
l6.place(width=60,height=120,x=180,y=120)
l7.place(width=60,height=60,x=60,y=180)
l8.place(width=60,height=60,x=120,y=180)
l9.place(width=60,height=60,x=0,y=240)
l0.place(width=60,height=60,x=180,y=240)

win.mainloop()

from tkinter import *
win = Tk()
win.title('华容道')
win.geometry('240x300')
a=['卒','赵云','曹操','黄忠','张飞','关羽','马超','卒','卒','卒']
b=[]
for i in range(10):
    exec("l%s=Label(win,text='%s',bg='pink',relief='groove',font=14)"%(i,a[i]))     #循环创建变量
    b.append('l'+str(i))
for i in range(10):
    eval(b[i]).place(width=80,height=30,x=i*80,y=0)
win.mainloop()

# #你们班的同学名字是
# students=['student1', 'student2', 'student3', 'student4', 'student5', 'student6', 'student7', 'student8']
# names=['黄烨','杨轶凯','涂荣轩','陈择凯','张三','李四','王五','赵六']
# #请用循环把同学的名字赋值给变量student1-8。如student1='黄烨',student2='杨轶凯'
# for i in range(8):
#     exec("student%s='%s'"%(i+1,names[i]))
# for i in students:
#     print(eval(i))