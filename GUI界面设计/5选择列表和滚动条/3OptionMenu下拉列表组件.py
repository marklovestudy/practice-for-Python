'''
OptionMenu为下拉列表组件，用户可以通过单击按钮展开下拉列表，并且选择其中的一项。
创建方法如下：
方法1
from tkinter import *
win=Tk()
val = StringVar()
val.set('a')
optionmenu=OptionMenu(win,val,'苹果','香蕉','梨','葡萄','圣女果','百香果','菠萝')      #(self, master, variable, value, *values, **kwargs)
optionmenu.pack()
win.mainloop()

方法2：
from tkinter import *
win=Tk()
val = StringVar()
fruits = ('苹果','香蕉','梨','葡萄','圣女果','百香果','菠萝')      #可通过元组或列表传值
optionmenu=OptionMenu(win,val,*fruits)      #(self, master, variable, value, *values, **kwargs)
optionmenu.pack()
win.mainloop()

实例1
在下拉列表组件中显示歌曲列表
from tkinter import *
win=Tk()
win.geometry('180x180')
val = StringVar()
Label(win,text='我的歌单').pack(side=TOP,fill=X)
list1 = ('逞强--刘洋洋','时间的过客--名诀','最爱--周慧敏','听闻远方有你--刘钧','一剪梅--费玉清','北方的夜里--大欢','暗里着迷--刘德华')
optionmenu=OptionMenu(win,val,*list1)      #(self, master, variable, value, *values, **kwargs)
optionmenu.pack(fill=X)
win.mainloop()

和OptionMenu配合的二个方法
    1.set()             设置下拉菜单默认被选中的值
    2.get()             设置下拉菜单当前被选中的值

实例：设置一个有四个答案的下拉列表，等用户选择答案后，判断用户的答案是否正确。
#OptionMenu的高级使用
from tkinter import *
def result():
    if v.get()==items[2]:
        re.config(text='答对了')
    else:
        re.config(text='答错了，小偷是%s'%items[2])
win=Tk()
win.title('逻辑推理谁是小偷')
win.configure(bg='yellow')
text = Text(win,width=50,height=13,bg='yellow',font=14,relief='flat')
ques="一位警察，抓获四个盗窃嫌疑犯，张三，李四，王二，麻子，而他们的供词如下：\n\n张三说：'不是我偷的'，\n\n李四说：'是张三偷的'。" \
     "\n\n王二说：'不是我',\n\n麻子说：'是李四偷的'。\n\n他们四人只有一个人说了真话，你知道谁是小偷吗？\n"
text.insert(END,ques)
text.grid(row=1,columnspan=4)
text.config(state='disabled')
items=('张三','李四','王二','麻子')
v = StringVar()
v.set(items[0])
optionmenu=OptionMenu(win,v,*items)      #(self, master, variable, value, *values, **kwargs)
optionmenu.grid(row=2,column=1)
button=Button(win,text='确定',command=result)
button.grid(row=2,column=2)
re = Label(win,padx=10,pady=10,width=60)
re.grid(row=3,columnspan=4)
win.mainloop()

ttk模块的OptionMenu组件与tkinter模块的OptionMenu组件样式差异比较大，
下面展示在窗口中添加ttk模块中的OptionMenu组件的代码以及表现样式。代码如下：
from tkinter import *
from tkinter.ttk import *
win=Tk()
val=StringVar(win)
fruits=('苹果','香蕉','梨','葡萄','圣女果','百香果','菠萝')
option=OptionMenu(win,val,*fruits)
option.pack()
win.mainloop()
'''
from tkinter import *
from tkinter.ttk import *
win=Tk()
def a(e):
    print(1)
val=StringVar(win)
fruits=('苹果','香蕉','梨','葡萄','圣女果','百香果','菠萝')
option=OptionMenu(win,val,*fruits,command=a)
option.pack()
v=option.keys()
print(v)
win.mainloop()