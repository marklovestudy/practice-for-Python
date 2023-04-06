'''
一，Treeview组件的基本使用
    Treeview组件是ttk模块的组件之一，它集树状态结构和表格于一体，用户可以使用该组件设计表格
    或者树形菜单，并且设置树形菜单时，可以折叠或展开子菜单。语法如下：
    tree = Treeview(win,option)
Treeview的参数如下：
    1.columns               其值为列表，列表的每一个元素代表一个列表标识符的名称，列表的长度为列的长度
    2.displaycolumns        设置列表是否显示以及显示顺序，也可以使用‘#all’表示全部显示
    3.height                表格的高度(表格中可以显示几行数据)
    4.padding               标题栏内容距离组件边缘的间距
    5.selectmode            定义选择行的方式，'extended'可以通Ctrl+鼠标选择多行(默认值);'browse'只能选择一行；'none'表示不能改变选择
    6.show                  表示显示哪些列，其值有'tree headings(显示所有列)''tree(显示第一列(图标栏))''headings(显示除第一列以外的其他列)'

实例：统计王者荣耀各英雄的类型以及操作难易程度。
from tkinter import *
from tkinter.ttk import *
win=Tk()
tree = Treeview(win,columns=('hero','type','operate'),show='headings',displaycolumns=(0,1,2))   #创建三列'hero','type','operate'
tree.heading('hero',text='英雄',anchor='center')          #给'hero'列写上文本
tree.heading('type',text='类型',anchor='center')
tree.heading('operate',text='操作难易程度',anchor='center')

tree.insert('',END,values=['孙尚香','射手','5'])
tree.insert('',END,values=('孙策','战士','3'))
tree.insert('',END,values=('大乔','辅助','3'))
tree.insert('',END,values=('小乔','法师','3'))
tree.pack()
win.mainloop()

二、为树形菜单添加图标
实例：
添加树形菜单后，需要通过insert()方法添加菜单的子项目item，其语法如下：
tree.insert(父对象，插入位置，ID，option)
其中，第一项是指定该菜单的父菜单的ID，，第二项是插入位置，可以是索引或者END等，ID是程序员为该项菜单设置的ID若省略，
则由Treeview自动分配，option是可选参数，一共有5个，分别是：
    1.text              属性菜单中子项目显示的名称
    2.image             子项目前面的图标
    3.values            子项目一行的值，未赋值的列是空列，超过列的长度会被截断
    4.open              子菜单展开或关闭
    5.tags              与item关联的标记

from tkinter import *
from tkinter.ttk import *
win=Tk()
tree = Treeview(win,columns=('date','temperature'),height=8)
tree.heading('#0',text='天气')
tree.heading('date',text='日期')
tree.heading('temperature',text='气温')

rain=PhotoImage(file='head.png')
storm=PhotoImage(file='jin.png')
sunny=PhotoImage(file='ku.png')
tree.insert('',END,values=('4月1日','-3~5'),image=rain,text='中到暴雨')
tree.insert('',END,values=('4月2日','-3~7'),image=sunny,text='睛')
tree.insert('',END,values=('4月3日','0~8'),image=storm,text='雷阵雨')
tree.insert('',END,values=('4月4日','1~10'),image=sunny,text='睛')
tree.insert('',END,values=('4月5日','2~10'),image=sunny,text='睛')
tree.insert('',END,values=('4月6日','2~12'),image=sunny,text='睛')
tree.insert('',END,values=('4月7日','2~10'),image=rain,text='睛')
tree.pack()
win.mainloop()

三，为树添加子菜单
使用Treeview组件添加子菜单时，需要通过ID绑定父元素，这个ID可以通过程序员手动分配，如
果程序员省略了子菜单的ID，则由Treeview组件自动分配。首先通过一段代码来看如何设置和分配的：
from tkinter import *
from tkinter.ttk import *
win=Tk()
tree = Treeview(win)
tree.heading('#0',text='皇帝')

tree.insert('',0,'wei',text='魏')
shu=tree.insert('',1,text='蜀')
wu=tree.insert('',2,text='吴')

tree.insert('wei',0,text='曹操')
tree.insert('wei',1,text='曹丕')

tree.insert(shu,0,text='刘备')
tree.insert(shu,1,text='刘禅')

tree.insert(wu,0,text='孙坚')
tree.insert(wu,1,text='孙权')

tree.pack()
win.mainloop()

实例：统计运动竞赛各组成员的得分情况
from tkinter import *
from tkinter.ttk import *
win=Tk()
tree = Treeview(win,columns='score')
tree.heading('#0',text='小组')
tree.heading('score',text='得分')

score1={'R001':'20','R002':'19','R003':'19','R004':'16'}
score2={'B001':'17','B002':'19','B003':'18','B004':'14'}
score3={'G001':'17','G002':'15','G003':'16','G004':'16'}

red=tree.insert('',0,text='红队')
blue=tree.insert('',1,text='蓝队')
green=tree.insert('',2,text='绿队')

for k,v in score1.items():
    tree.insert(red,END,text=k,values=v)

for k,v in score2.items():
    tree.insert(blue,END,text=k,values=(v))

for k,v in score3.items():
    tree.insert(green,END,text=k,values=(v))

tree.pack()
win.mainloop()

四，菜单项的获取与编辑
Treeview组件提供了一些虚拟事件和方法，首先介绍虚拟事件，三个虚拟事件如下：
    1.<<TreeviewSelect>>        当选项发生变化时，触发某事件
    2.<<TreeviewOpen>>          当菜单项items的open=True时，触发某事件
    3.<<TreeviewClose>>         当菜单项items的open=False时，触发某事件

Treeview常用方法和含义如下：
    1.bbox(item,column=None)            返回一个item的范围，如果column指定了列，则返回元素的范围，如果item不可使，则返回空值
    2.get_children(item=None)           返回item的所有子item的列表，如果item没有指定，则返回根目录的item
    3.set_children(item,*newchildren)   设置item的新的子items，这里的设置指的是 全部替换
    4.column(column,option=none,**kw)   设置或返回各列的属性。column是列标识符，option若不设置，则返回所有属性的字典
    5.delete(*item)                     删除item及其子item
    6.detach(*item)                     取消item和子item的链接，可以在另一个点重新输入，但不会显示。根item的链接无法取消
    7.exists(item)                      判断item是否在Treeview组件中，若返回True，则在Treeview中
    8.focus(item=None)                  设置或返回获得焦点的item，若不指定item且无item获得焦点，则返回空值
    9.heading(column,option=None,**kw)  查询或修改指定列的标题选项，column为列标识符，option若不设置则返回所有属性的字典，若设置，则返回该属性的属性值
    10.insert(parent,index,iid=none,**kw)   创建新的item并返回新创建item的项标识符
    11.item(item,option=None,**kw)      查询或修改指定item的选项
    12.selection()                      返回所有选中的items的列表
    13.selection_set(*item)             设置项目为新的选择
    14.selection_add(*item)             从选择项中添加项
    15.selection_remove(*item)          从选择项中删除项
    16.selection_toggle(*item)          切换项目中每个项目的选择状态
    17.set(item,column=None,value=None) 指定item，如果不设定column和value，则返回他们的字典，若设置了
                                        column，则返回对应的value，若value也设定了，则作相应的修改

实例：统计个人出行纪录
在菜单中统计并且修改个人出行记录。具体步骤如下：
#3编写setdat()方法，该方法实现选择月份后，日期选择列表显示对应天数的功能。
def setdat(event):
    temp=monsel.get()
    if temp == 2:
        dat['value']=tuple(range(1,29))
    elif temp in [4,6,9,11]:
        dat['value'] = tuple(range(1, 31))
    else:
        dat['value'] = tuple(range(1, 32))

#4编写get1()方法，实现向树形菜单中添加内容的功能，当单击'确定'按钮时，首先判断目的地是否为空，若不为空，则将时间，日期以及目的地存储为元组，
#以便于向树形菜单中添加新的菜单项，然后判断当前属性菜单中，是否有菜单基被选中，若有，则在该菜单项的位置处添加新的菜单项（即修改当前选中的表格
# 内容），并删除原菜单基，否则，在菜单末尾添加新的菜单项。在步骤3后面添加如下代码。
def get1():
    if len(entry.get())==0:
        return False        #print('请输入目的地')
    else:
        #将时间格式化为两位数
        h = str(horsel.get()) if horsel.get() > 10 else '0' + str(horsel.get())
        m = str(minsel.get()) if minsel.get() > 10 else '0' + str(minsel.get())
        item1 = (str(monsel.get())+'月'+str(datsel.get())+'日',h+':'+m,entry.get())
        if not tree.focus() == '':          #判断是否有菜单被选中
            #在获取焦点的菜单项的位置添加新的菜单，并且删除原来的菜单项
            tree.insert('',tree.index(tree.focus()),values=item1)
            del1()
        else:
            tree.insert('',END,values=item1)
        reset1()

#5编写dell()方法，实现单击'删除'按钮，删除当前被选中的菜单项的功能，在步骤4后面添加如下代码：
def del1():
    #单击删除按钮时，删除获取焦点的菜单
    if tree.focus() == '':
        return False
    else:
        tree.delete(tree.focus())       #focus(item=None)设置或返回获得焦点的item，若不指定item且无item获得焦点，则返回空值

#6编写edt()方法，实现双击菜单中某行，修改该行中的内容的功能。接步骤5后，如下：
def edt(event):
    temp = tree.set(tree.focus())       #指定item，如果不设定column和value，则返回他们的字典，若设置了column，则返回对应的value，若value也设定了，则作相应的修改
    print(temp,tree.focus())            #打印出来供观察
    d = temp['date'].split('月')         #时间以'月'分割
    t = temp['time'].split(':')         #时间以':'分割
    monsel.set(int(d[0]))               #获取列表的第一项，并取整，即获取月份赋值到月份选择列表中
    datsel.set(int(d[1].split('日')[0]))     #获取日期赋值到日期选择列表中
    horsel.set(int(t[0]))               #获取小时赋值到时间的第一个选择列表中
    minsel.set(int(t[1]))               #获取分钟赋值到时间的第二个选择列表中
    entry.delete(0,END)
    entry.insert(INSERT,temp['depart'])

#7由于修改和删除菜单项后，都需要重置文本组件里的值，为了避免重复代码，编写reset1()方法，该方法中依次
#重置了各列表框和文本框的值。在步骤6后。如下：
def reset1():
    monsel.set(1)
    datsel.set(1)
    horsel.set(0)
    minsel.set(0)
    entry.delete(0,END)
#1首先创建窗口，在窗口中添加输入时间、日期的选择框以及出发地的文本类型组件，具体代码如下：
from tkinter import *
from tkinter.ttk import *
win=Tk()
#输入内容
frame=Frame()
frame.grid()
Label(frame,text='日期：').grid(row=0,column=0)
monsel=IntVar()
monsel.set(1)
mon=Combobox(frame,value=tuple(range(1,13)),textvariable=monsel,width=5)    #月
mon.grid(row=0,column=1)
mon.bind('<<ComboboxSelected>>',setdat)         #月份变化时，对应日期也变化
Label(frame,text='-').grid(row=0,column=2)
datsel=IntVar()
datsel.set(1)
dat=Combobox(frame,value=tuple(range(1,32)),textvariable=datsel,width=5)    #日
dat.grid(row=0,column=3)
Label(frame,text='时间：').grid(row=0,column=4,columnspan=2,sticky=S+E)
horsel=IntVar()                                 #绑定时间选项
horsel.set(0)
hor=Spinbox(frame,from_=0,to=24,width=5,textvariable=horsel)    #时
hor.grid(row=0,column=6)
Label(frame,text=':').grid(row=0,column=7)
minsel=IntVar()
minsel.set(0)                                   #绑定分钟选项
min=Spinbox(frame,from_=0,to=59,width=5,textvariable=minsel)    #分
min.grid(row=0,column=8)
Label(frame,text='出发地:').grid(row=0,column=9)
entry=Entry(frame)
entry.grid(row=0,column=10)
Button(frame,text='确定',command=get1).grid(row=0,column=11)
Button(frame,text='删除',command=del1).grid(row=0,column=12)
#2在下方添加表格以及表格绑定虚拟事件<<TreeviewSelect>>，作用是当选中某菜单项时，立即获取该菜单的内容，便于修改或删除等。如下：
tree = Treeview(win,columns=('date','time','depart'),show='headings')
tree.heading('date',text='日期')                  #设置每列的标题
tree.heading('time',text='时间')
tree.heading('depart',text='出发地')
tree.grid(row=1,column=0)
tree.bind('<<TreeviewSelect>>',edt)             #当选项发生变化时，调用edt()函数
win.mainloop()
'''
#3编写setdat()方法，该方法实现选择月份后，日期选择列表显示对应天数的功能。
def setdat(event):
    temp=monsel.get()
    if temp == 2:
        dat['value']=tuple(range(1,29))
    elif temp in [4,6,9,11]:
        dat['value'] = tuple(range(1, 31))
    else:
        dat['value'] = tuple(range(1, 32))

#4编写get1()方法，实现向树形菜单中添加内容的功能，当单击'确定'按钮时，首先判断目的地是否为空，若不为空，则将时间，日期以及目的地存储为元组，
#以便于向树形菜单中添加新的菜单项，然后判断当前属性菜单中，是否有菜单基被选中，若有，则在该菜单项的位置处添加新的菜单项（即修改当前选中的表格
# 内容），并删除原菜单基，否则，在菜单末尾添加新的菜单项。在步骤3后面添加如下代码。
def get1():
    if len(entry.get())==0:
        return False        #print('请输入目的地')
    else:
        #将时间格式化为两位数
        h = str(horsel.get()) if horsel.get() > 10 else '0' + str(horsel.get())
        m = str(minsel.get()) if minsel.get() > 10 else '0' + str(minsel.get())
        item1 = (str(monsel.get())+'月'+str(datsel.get())+'日',h+':'+m,entry.get())
        if not tree.focus() == '':          #判断是否有菜单被选中
            #在获取焦点的菜单项的位置添加新的菜单，并且删除原来的菜单项
            tree.insert('',tree.index(tree.focus()),values=item1)
            del1()
        else:
            tree.insert('',END,values=item1)
        reset1()

#5编写dell()方法，实现单击'删除'按钮，删除当前被选中的菜单项的功能，在步骤4后面添加如下代码：
def del1():
    #单击删除按钮时，删除获取焦点的菜单
    if tree.focus() == '':
        return False
    else:
        tree.delete(tree.focus())       #focus(item=None)设置或返回获得焦点的item，若不指定item且无item获得焦点，则返回空值

#6编写edt()方法，实现双击菜单中某行，修改该行中的内容的功能。接步骤5后，如下：
def edt(event):
    temp = tree.set(tree.focus())       #指定item，如果不设定column和value，则返回他们的字典，若设置了column，则返回对应的value，若value也设定了，则作相应的修改
    print(temp,tree.focus())            #打印出来供观察
    d = temp['date'].split('月')         #时间以'月'分割
    t = temp['time'].split(':')         #时间以':'分割
    monsel.set(int(d[0]))               #获取列表的第一项，并取整，即获取月份赋值到月份选择列表中
    datsel.set(int(d[1].split('日')[0]))     #获取日期赋值到日期选择列表中
    horsel.set(int(t[0]))               #获取小时赋值到时间的第一个选择列表中
    minsel.set(int(t[1]))               #获取分钟赋值到时间的第二个选择列表中
    entry.delete(0,END)
    entry.insert(INSERT,temp['depart'])

#7由于修改和删除菜单项后，都需要重置文本组件里的值，为了避免重复代码，编写reset1()方法，该方法中依次
#重置了各列表框和文本框的值。在步骤6后。如下：
def reset1():
    monsel.set(1)
    datsel.set(1)
    horsel.set(0)
    minsel.set(0)
    entry.delete(0,END)
#1首先创建窗口，在窗口中添加输入时间、日期的选择框以及出发地的文本类型组件，具体代码如下：
from tkinter import *
from tkinter.ttk import *
win=Tk()
#输入内容
frame=Frame()
frame.grid()
Label(frame,text='日期：').grid(row=0,column=0)
monsel=IntVar()
monsel.set(1)
mon=Combobox(frame,value=tuple(range(1,13)),textvariable=monsel,width=5)    #月
mon.grid(row=0,column=1)
mon.bind('<<ComboboxSelected>>',setdat)         #月份变化时，对应日期也变化
Label(frame,text='-').grid(row=0,column=2)
datsel=IntVar()
datsel.set(1)
dat=Combobox(frame,value=tuple(range(1,32)),textvariable=datsel,width=5)    #日
dat.grid(row=0,column=3)
Label(frame,text='时间：').grid(row=0,column=4,columnspan=2,sticky=S+E)
horsel=IntVar()                                 #绑定时间选项
horsel.set(0)
hor=Spinbox(frame,from_=0,to=24,width=5,textvariable=horsel)    #时
hor.grid(row=0,column=6)
Label(frame,text=':').grid(row=0,column=7)
minsel=IntVar()
minsel.set(0)                                   #绑定分钟选项
min=Spinbox(frame,from_=0,to=59,width=5,textvariable=minsel)    #分
min.grid(row=0,column=8)
Label(frame,text='出发地:').grid(row=0,column=9)
entry=Entry(frame)
entry.grid(row=0,column=10)
Button(frame,text='确定',command=get1).grid(row=0,column=11)
Button(frame,text='删除',command=del1).grid(row=0,column=12)
#2在下方添加表格以及表格绑定虚拟事件<<TreeviewSelect>>，作用是当选中某菜单项时，立即获取该菜单的内容，便于修改或删除等。如下：
tree = Treeview(win,columns=('date','time','depart'),show='headings')
tree.heading('date',text='日期')                  #设置每列的标题
tree.heading('time',text='时间')
tree.heading('depart',text='出发地')
tree.grid(row=1,column=0)
tree.bind('<<TreeviewSelect>>',edt)             #当选项发生变化时，调用edt()函数
win.mainloop()