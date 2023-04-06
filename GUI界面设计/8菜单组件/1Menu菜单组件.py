'''
***
一、Menu组件的基本使用
    menu=Menu(win,option)

实例：为游戏窗口添加菜单项样式
    为窗口添加'游戏''帮助''退出'菜单项，具体代码如下：
from tkinter import *
win=Tk()
win2=Tk()
win.title('为游戏窗口添加菜单')
menu1=Menu(win)
menu1.add_command(label='游戏')
menu1.add_command(label='帮助')
menu1.add_command(label='退出')
menu2=Menu(win2)
menu2.add_command(label='戏')
menu2.add_command(label='助')
menu2.add_command(label='出')
win.config(menu=menu1)              #显示菜单
win2.config(menu=menu2)
win.mainloop()

实例：为游戏菜单添加功能
本实例通过一个眼力测试游戏，即在窗口中，众多的‘大’字中找到唯一一个‘女’字。单击菜单中的‘游戏’‘帮助’以及‘退出’选项分别
可以实现重新开始与结束游戏，获得提示以及退出游戏的功能。具体步骤如下：
n=84
def wrong():
    global n
    n-=1
    l.config(text='分数：'+str(n))

def rt():
    global n
    top=Toplevel(win)
    Label(top,text='恭喜，找到了，得会为：'+str(n),fg='red').grid(row=0,column=0,padx=10,pady=10)

def hp():
    showwarning('提醒','第4行')

def game():
    global n
    boo = askyesnocancel('暂停','是否停止本游戏，点击是，重新开始游戏，点击否暂停游戏')
    if boo == True:
        n=84
        l.config(text='分数：'+str(n))
    elif boo == False:
        l.config(text='分数：' + str(n))
from tkinter import *
from tkinter.messagebox import *
win=Tk()
win.title('为游戏窗口添加菜单')
menu1=Menu(win)
menu1.add_command(label='游戏',command=game)
menu1.add_command(label='帮助',command=hp)
menu1.add_command(label='退出',command=win.quit)
win.config(menu=menu1)              #显示菜单

for i in range(6):
    for j in range(14):
        Button(win,text='大',command=wrong).grid(row=i,column=j)
Button(win,text='女',command=rt).grid(row=3,column=6)
l=Label(win,font=14,fg='red',text='分数：84')
l.grid(row=8,column=0,columnspan=14)
win.mainloop()



***
二、制作二级下拉菜单
        方法                                          含义
    1.add_command(option)                   添加一个命令菜单项，相当于add('command',option)
    2.add_cascade(option)                   添加一个父菜单，相当于add('cascade',option)
    3.add_checkbutton(option)               添加一个菜单项，该菜单项为多选按钮，相当于add('checkbutton',option)
    4.add radiobutton(option)               添加一个菜单项，该菜单项为单选按钮，相当于add("radiobutton”,option)
    5.add separator(option)                 添加一条分割线，相当于add("separator",option)
    6.delete(index1,index2)                 删除index1~index2(含)的所有菜单项
    7.entrycget(index,option)               获得指定菜单项的某选项的值，index指定菜单项的索引值
    8.entryconfig(index,option)             设置指定菜单项的某选项的值，index指定菜单项的索引值
    9.index(index)                          返回index参数相对应的选项的序号
    10.insert(index,itemType,option)        插入指定类型的菜单项到index参数指定的位置
    11.insert_cascade(index,option)         在index参数指定的位置添加一个父菜单
    12.insert_checkbutton(index,option)     在index参数指定的位置添加一个复选框
    13.insert_radiobutton(index,option)     在index参数指定的位置添加一个单选按钮
    14.insertcommand(index,option)          在index参数指定的位置添加一个子菜单
    15.insert_separator(index,option)       在index参数指定的位置添加一个分割线
    16.invoke(index)                        调用index参数指定的菜单选项相关联的方法
    17.post(x,y)                            在指定位置显示弹出菜单
    18.type(index)                          获得index参数指定菜单项的类型，返回值为“command”“cascade”“checkbutton
                                            “radiobutton” “ separator”
    19.unpost()                             移除弹出菜单
    20.ypostion(index)                      返回index参数指定的菜单项的垂直偏移位置

以上方法中option参数及含义
    1.postcommand                       其属性值为一个方法，表示当菜单被打开时，调用该函数
    2.tearoff                           设置菜单能否从窗口中分离(默认值为True)
    3.cursor                            鼠标悬停Menu组件上时，鼠标的样式
    4.tearoffcommand                    当菜单被分离时，执行的方法
    5.background(bg)                    设置背景颜色
    6.selectcolor                       当菜单项选中为单选按钮或多选按钮时，选中标志的颜色
    7.activebackground                  当Menu组件处于active状态(通过state设置)的背景颜色
    8.activeborderwidth                 当Menu组件处于active状态(通过state设置)的边框宽度
    9.activeforeground                  当Menu组件处于active状态(通过state设置)的前景颜色
    10.bordewidth(bd)                   指定边框宽度
    11.disabledforeground               当Menu组件处于disabled状态时(通过state设置)的前景颜色
    12.font                             指定Menu组件中的文字样式
    13.foreground(fg)                   指定Menu组件的前景颜色
    14.relief                           指定边框样式
    15.title                            被分离的菜单的标题，默认标题为父菜单的名字

实例：为城市列表添加弹出式菜单
    通过二级菜单在窗口中展示城市列表，然后单击菜单中的‘修改’选项，即可弹出一个显示‘添加城市’和‘修改城市’的下拉菜单。
def pop1():
    menu2_2.post(win.winfo_x()+60,win.winfo_y()+120)    #win.winfo_x()、win.winfo_y()是获取win窗口的位置

def ad():
    v = input('你要添加的城市名字是：')
    menu2_1.add_command(label=v)

def rm():
    v = input('你要删除的城市名字是：')
    i = menu2_1.index(v)
    menu2_1.delete(i)
def st():
    v = input('你要修改的城市名字是：')
    i=menu2_1.index(v)
    menu2_1.delete(i)
    menu2_1.insert(i,'command')
    newv=input('你要修改的城市新名字是：')
    menu2_1.entryconfig(i,label=newv)
from tkinter import *
from tkinter.messagebox import *
win=Tk()
menu1=Menu(win)                                 #创建一级菜单
menu2_1=Menu(menu1,tearoff=False)               #设置菜单能否从窗口中分离(默认值为True)
menu1.add_cascade(label='城市',menu=menu2_1)     #给一级菜单中的‘城市’添加一个父菜单，menu2_1
menu2_1.add_command(label='北京')                 #给menu2_1添加命令菜单项
menu2_1.add_command(label='上海')                 #给menu2_1添加命令菜单项
menu2_1.add_command(label='重庆')
menu2_1.add_command(label='广州')
menu2_1.add_command(label='深圳')

menu1.add_command(label='修改',command=pop1)
menu2_2=Menu(menu1,tearoff=False)
menu2_2.add_command(label='添加城市',command=ad)
menu2_2.add_command(label='修改城市',command=st)
menu2_2.add_command(label='删除城市',command=rm)
menu1.add_command(label='退出',command=win.quit)
win.config(menu=menu1)

win.mainloop()

实例：为菜单添加快捷键，主要通过accelerator实现。
    注：accelerator只能在菜单中显示快捷键提示信息，而不能实现单击快捷键时，菜单项响应事件，
    若要实现单击快捷键响应对应的功能，还需要bind()方法绑定键盘事件
为窗口添加菜单，并且通过菜单设置窗口大小和文字样式。具体如下：
1引入ttk模块，然后新建窗口，在窗口中添加工具栏，并且为工具栏中的‘最大化’，‘中等窗口’添加快捷键。
def max_win(event):
    win.geometry('600x400')

def normal_win(event):
    win.geometry('300x200')


def txt():
    global val,font_size,top
    top=Toplevel(win)
    val=StringVar()
    val.set('宋体')
    font_family=('宋体','黑体','方正舒体','楷体','隶书','方正姚体')
    family = Combobox(top,textvariable=val,values=font_family)
    family.grid(row=0,column=0)
    font_size=Spinbox(top,from_=12,to=30,increment=2,width=10)
    font_size.grid(row=0,column=1)
    btn1=Button(top,text='确定',command=font_set)
    btn1.grid(row=1,column=1)

def font_set():
    font1=(val.get(),font_size.get())
    label.config(font=font1)
from tkinter import *
from tkinter.ttk import *
win=Tk()
win.geometry('300x200')
menu1=Menu(win)                                 #创建一级菜单
menu2_1=Menu(menu1,tearoff=False)               #设置菜单能否从窗口中分离(默认值为True)
menu1.add_cascade(label='窗体',menu=menu2_1)     #给一级菜单中的‘城市’添加一个父菜单，menu2_1
menu2_1.add_command(label='最大化',accelerator='Ctrl+UP',command=lambda :max_win(''))
menu2_1.add_command(label='中等窗口',accelerator='Ctrl+DOWN',command=lambda :normal_win(''))             #给menu2_1添加命令菜单项
menu2_1.add_command(label='最小化',command=win.iconify)
menu2_1.add_separator()                         #添加分割线
menu2_1.add_command(label='关闭',command=win.quit)

menu2_2=Menu(menu1,tearoff=False)
menu1.add_cascade(label='自定义',menu=menu2_2)
menu2_2.add_command(label='文字设置',command=txt)
win.config(menu=menu1)

label=Label(win,text='这是一个窗口')
label.grid(row=0,column=0)
win.bind_all('<Control-Up>',max_win)
win.bind_all('<Control-Down>',normal_win)
win.mainloop()

实例：制作工具栏
根据含义猜成语游戏，游戏中可以通过快捷键或者单击工具栏中的菜单实现下一关，重新游戏，退出游戏，
还可以设置窗口和文字样式及窗口大小。
具体步骤如下：
num=0
idiom =["别出心裁","白云苍狗","暴虎冯河","鞭长莫及","并行不悖","安土重迁","不耻下问", "不胫而走","安步当车","爱莫能助","白驹过隙"]
idiom_means = ["独出巧思，不同流俗","比喻世事变幻无常","比喻有勇无谋，鲁莽冒险","本意为马鞭虽长，但打不到马肚子上，比喻虽有力，力量也打不到",
              "彼此同时进行，不相妨碍","留恋故土,不肯轻易迁移","比喻谦虚好学，不介意向学识或地位不及自己的人请教","消息传的很快",
              "从容的步行，就当乘车一般","心里愿意帮助，但是力量做不到","形容时间过得很快，像白马在细小的缝隙前一闪而过"]
def next1(event):
    global num
    num+=1
    panduan()

def restart(event):
    global num
    num=0
    panduan()

def show1():
    showinfo('游戏规则','根据成语的含义猜成语，正确则自动跳转到下一关')

def tip():
    str1=idiom[num][0]
    entry.delete(0,END)
    entry.insert(0,str1)

def panduan():
    global num
    a = entry.get()
    if a == idiom[num]:
        num += 1
    if (num >= len(idiom)):
        boo = askyesno('成功过关','恭喜！已过完所有关卡，是否重新过关？')
        if boo == True:
            num=0
            panduan()
        else:
            win.quit()
    entry.delete(0,END)
    means.config(text=idiom_means[num])
    level.config(text='第'+str(num+1)+'关')
from tkinter import *
from tkinter.messagebox import *
win=Tk()
win.geometry('250x200')
win.title('成语猜猜猜')

menu1=Menu(win)                                 #创建一级菜单
menu2_1=Menu(menu1,tearoff=False)               #设置菜单能否从窗口中分离(默认值为True)
menu1.add_cascade(label='游戏',menu=menu2_1)     #给一级菜单中的‘城市’添加一个父菜单，menu2_1
menu2_1.add_command(label='下一关',accelerator='Ctrl+N',command=lambda :next1(''))
menu2_1.add_command(label='重新开始',accelerator='Ctrl+R',command=lambda :restart(''))             #给menu2_1添加命令菜单项
menu2_1.add_separator()                         #添加分割线
menu2_1.add_command(label='退出',command=win.quit)

menu2_2=Menu(menu1,tearoff=False)
menu1.add_cascade(label='帮助',menu=menu2_2)
menu2_2.add_command(label='游戏规则',command=show1)
menu2_2.add_command(label='提示',command=tip)
win.config(menu=menu1)

level=Label(win,text='第一关',font=14)
level.grid(row=0,column=0,columnspan=4,sticky=E)

means=Label(win,text=idiom_means[0],font=14,width=30,bg='#D8F3F0',height=3,wraplength=200)
means.grid(row=1,column=0,pady=10,columnspan=4)

entry=Entry(win,font=14)
entry.grid(row=2,column=1,sticky=E)
btn=Button(win,text='确定',command=panduan)
btn.grid(row=2,column=2)

win.bind_all('<Control-n>',next1)
win.bind_all('<Control-r>',restart)
win.mainloop()
'''
num=0
idiom =["别出心裁","白云苍狗","暴虎冯河","鞭长莫及","并行不悖","安土重迁","不耻下问", "不胫而走","安步当车","爱莫能助","白驹过隙"]
idiom_means = ["独出巧思，不同流俗","比喻世事变幻无常","比喻有勇无谋，鲁莽冒险","本意为马鞭虽长，但打不到马肚子上，比喻虽有力，力量也打不到",
              "彼此同时进行，不相妨碍","留恋故土,不肯轻易迁移","比喻谦虚好学，不介意向学识或地位不及自己的人请教","消息传的很快",
              "从容的步行，就当乘车一般","心里愿意帮助，但是力量做不到","形容时间过得很快，像白马在细小的缝隙前一闪而过"]
def next1(event):
    global num
    num+=1
    panduan()

def restart(event):
    global num
    num=0
    panduan()

def show1():
    showinfo('游戏规则','根据成语的含义猜成语，正确则自动跳转到下一关')

def tip():
    str1=idiom[num][0]
    entry.delete(0,END)
    entry.insert(0,str1)

def panduan():
    global num
    a = entry.get()
    if a == idiom[num]:
        num += 1
    if (num >= len(idiom)):
        boo = askyesno('成功过关','恭喜！已过完所有关卡，是否重新过关？')
        if boo == True:
            num=0
            panduan()
        else:
            win.quit()
    entry.delete(0,END)
    means.config(text=idiom_means[num])
    level.config(text='第'+str(num+1)+'关')
from tkinter import *
from tkinter.messagebox import *
win=Tk()
win.geometry('250x200')
win.title('成语猜猜猜')

menu1=Menu(win)                                 #创建一级菜单
menu2_1=Menu(menu1,tearoff=False)               #设置菜单能否从窗口中分离(默认值为True)
menu1.add_cascade(label='游戏',menu=menu2_1)     #给一级菜单中的‘城市’添加一个父菜单，menu2_1
menu2_1.add_command(label='下一关',accelerator='Ctrl+N',command=lambda :next1(''))
menu2_1.add_command(label='重新开始',accelerator='Ctrl+R',command=lambda :restart(''))             #给menu2_1添加命令菜单项
menu2_1.add_separator()                         #添加分割线
menu2_1.add_command(label='退出',command=win.quit)

menu2_2=Menu(menu1,tearoff=False)
menu1.add_cascade(label='帮助',menu=menu2_2)
menu2_2.add_command(label='游戏规则',command=show1)
menu2_2.add_command(label='提示',command=tip)
win.config(menu=menu1)

level=Label(win,text='第一关',font=14)
level.grid(row=0,column=0,columnspan=4,sticky=E)

means=Label(win,text=idiom_means[0],font=14,width=30,bg='#D8F3F0',height=3,wraplength=200)
means.grid(row=1,column=0,pady=10,columnspan=4)

entry=Entry(win,font=14)
entry.grid(row=2,column=1,sticky=E)
btn=Button(win,text='确定',command=panduan)
btn.grid(row=2,column=2)

win.bind_all('<Control-n>',next1)
win.bind_all('<Control-r>',restart)
win.mainloop()