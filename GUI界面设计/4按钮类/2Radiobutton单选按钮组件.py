'''
Radiobutton组件的基本使用
    Radiobutton组件可以实现单选，相关参数
    1.image             指定Radiobutton显示图片
    2.text              指定Radiobutton显示文本
    3.compound          设置图像和文本的排版方式，具体值可参照Label组件中compound属性
    4.cursor            当鼠标悬停在Radiobutton上时的样式
    5.indicatoron       指定是否绘制指定Radiobutton前面的小圆圈
    6.selectcolor       选择框的颜色
    7.selecteimage      当Radiobutton被选中时显示的状态
    8.state             指定Radiobutton的状态
    9.value             指定Radiobutton的值
    10.variable         获取或设置当前选中的单选按钮

from tkinter import *
win=Tk()
vali=IntVar()
vali.set('male')
r1=Radiobutton(win,variable=vali,value='male',text='男').pack()
r2=Radiobutton(win,variable=vali,value='female',text='女').pack()
r3=Radiobutton(win,variable=vali,value='gay',text='人妖').pack()
Label(win,textvariable = vali).pack()
win.mainloop()

实例：
在窗口中显示一则脑筋急转弯的游戏
from tkinter import *

def result1():
    if v.get()==1:
        l1.config(text='答错了，答案是小狗，因为旺旺仙贝（汪汪先背）')
    elif v.get() == 0:
        l1.config(text='请选择一个答案')
    else:
        l1.config(text='答对了，因为旺旺仙贝（汪汪先背）')

win=Tk()
win.title('脑筋急转弯')
win.geometry('300x150')
text = Label(win,text='老师让小猫和小狗去背书，请问谁先背书呢',font=14).pack(anchor=W)
v=IntVar()
v.set(0)
r1=Radiobutton(win,variable=v,value=1,text='小猫').pack(anchor=W)
r2=Radiobutton(win,variable=v,value=2,text='小狗').pack(anchor=W)
b = Button(win,text='提交',command=result1,font=14,relief='groove').pack()
l1=Label(win)
l1.pack()
win.mainloop()


实例心理测试功能
'''
from tkinter import *

def result1():
    if v.get() == 0:
        l1.config(text='\n你太直接了，这样对你的个人不太好，经常上当，也会被别人报复，好自为之。')
    elif v.get() == 1:
        l1.config(text='\n说明你是一个比较不容易克制自己的人，容易得罪人，小心被报复')
    elif v.get() == 2:
        l1.config(text='\n说明你是一个比较容易克制自己的人，一般不会犯错，但也会有小机会被情绪左右，你很优秀了。')
    else:
        l1.config(text='\n只能说明你太利害了，自我控制能力太强，干啥事都很有决心，但是城府有点深，难交到知心朋友。')

win=Tk()
win.title('心理测试')
str1 = ['一定会','很可能会','偶尔会','绝不会']
Label(win,text='测试你的性格有几面').pack(anchor=W)                              #1
Label(win,text='当你看不惯别人的某些行为时，你会直接指出来吗？').pack(anchor=W)        #2
v=IntVar()
for i in range(len(str1)):  #len(str1)=4        #3,4,5,6
    Radiobutton(win,variable=v,value=i,text = str1[i],indicatoron=0,selectcolor='blue').pack(side=TOP,fill=X,padx=10)
b = Button(win,text='提交',bg='blue',command=result1,font=14,relief='groove').pack(side=TOP,fill=X,padx=30) #7
l1=Label(win,font=14,width=40,height=10,justify='left',wraplength=320)  #8
l1.pack()
win.mainloop()
