'''
Checkbutton组件的基本使用,
val1 = IntVar() StringVar()
#1绑定了变量
#2动态变化的值
#3选中代表1，不选中代表0

#1每个Checkbutton绑定的是不同的变量，
#2每个Checkbutton所绑定的变量选中代表1，没被选中代表0
#逻辑1
from tkinter import *
win=Tk()
def p():
    bb=[]
    for i in aa:                #遍历aa序列
        bb.append(i.get())      #把aa中的每个元素获得的值添加到bb中
    print(bb)                   #打印列表
aa=[]                           #创建列表
for i in range(10):
    v = IntVar()                   #创建变量
    aa.append(v)             #把变量加入到列表末尾
    Checkbutton(win,variable=v,text=str(i+1)+'号',command=p).pack()    #创建复选框
win.mainloop()
逻辑2
from tkinter import *
win=Tk()
val1 = IntVar()
ckbox1=Checkbutton(win,variable=val1,text='苹果').pack()
val2 = IntVar()
ckbox2=Checkbutton(win,variable=val2,text='香蕉').pack()
win.mainloop()

实例多选
from tkinter import *
win=Tk()
fruits=['苹果','香蕉','百香果','草霉','牛油果']
val1 = IntVar()
def a():
    print(val1)

for i in fruits:
    val1 = IntVar()             #如果这一行的IntVar()的值放在列表的下面，那么将会使所有的Checkbutton绑定同一个变量，变量是从PY_VAR0，PY_VAR1，依次增加，每一次创建都会增加1，所以每次绑定的数不一样
    print(val1)
    ckbox1=Checkbutton(win,variable=val1,text=i).pack(side='left')      #组件被选中时val1的值为1，否则为0

win.mainloop()

实例：调查问卷
def result1():
    sel=''
    for i in range(len(str1)):
        print(check[i].get())
        if (check[i].get()==1):
            sel = sel+str1[i]+' '
    re.config(text=sel)
from tkinter import *
win=Tk()
win.title('调查问卷')
str1=['旅游','追剧上网','和新友聚聚','户外健身']
text = Label(win,text='适当的放松 友谊身心健康，请在下方选出自己最喜欢的方式',font=14).grid(row=0,column=0,columnspan=6)
check=[]
for i in range(len(str1)):
    v = IntVar()
    ckbox1=Checkbutton(win,variable=v,text=str1[i],font=12,selectcolor='pink').grid(row=1,column=i)
    check.append(v)
button = Button(win,text='提交',bg='pink',command=result1).grid(row=2,column=0,pady=6,columnspan=6)
re = Label(win,font=12,height=5,width=50,bg='gray')
re.grid(row=4,columnspan=6)
win.mainloop()
'''
from tkinter import *
win=Tk()
fruits=['苹果','香蕉','百香果','草霉','牛油果']

def a():
    print(val1.get())
    bb=[]
    for i in range(len(aa)):
        bb.append(aa[i].get())
    print(bb)
aa=[]
for i in fruits:
    val1 = IntVar()             #如果这一行的IntVar()的值放在列表的下面，那么将会使所有的Checkbutton绑定同一个变量，变量是从PY_VAR0，PY_VAR1，依次增加，每一次创建都会增加1，所以每次绑定的数不一样
    ckbox1=Checkbutton(win,variable=val1,text=i,offvalue=3, onvalue=4,command=a).pack(side='left')
    aa.append(val1)
win.mainloop()