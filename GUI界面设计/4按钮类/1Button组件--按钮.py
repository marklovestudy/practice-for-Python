'''
Button组件的基本使用
    Button(win,text='确定'，command=hit)

1,添加图片：
from tkinter import *
win=Tk()
def aa():
    Label(win,image=ima1).pack()
ima1 = PhotoImage(file='1.gif')
Button(win,text='确定',image=ima1,compound='center',font=50,command=aa).pack()
win.mainloop()

2,Button组件的相关属性
    1，activebackground                  按钮激活时的背景颜色
    2.activeforeground                  按钮激活时的前景颜色
    3.bd                                边框的宽度，默认为2像素
    4.command                           单击按钮时，执行的方法
    5.image                             在按钮上添加的图片
    6.state                             设置按钮的状态，可选的值有NORMAL(默认值)、ACTIVE、DISABLED
    7.wraplength                        限制按钮每行显示的字符的数量，按像素单位
    8.text                              按钮的文本内容
    9.underline                         设置哪个文字带下划线，例如取值为0，表示第一个，值为1，表示第二个，默认值为-1

实例：实现简易密码输入器
from tkinter import *
def num(a):
    psw.insert('end',a)
def back():
    v = psw.get()
    psw.delete(len(v)-1,'end')
def enter():
    v = psw.get()
    win2=Toplevel()         #重新打开一个新的窗口，该窗口在根窗口的上方
    if v=='123456789':
        Label(win2,text='\n\n密码正确，请等待\n\n').pack()
    else:
        Label(win2, text='\n\n密码不正确，请重新输入\n\n').pack()
win=Tk()
win.title('密码输入器')
psw = Entry(win,relief = 'solid',justify='center')
b1=Button(win,text='1',command=lambda :num('1'))
b2=Button(win,text='2',command=lambda :num('2'))
b3=Button(win,text='3',command=lambda :num('3'))
b4=Button(win,text='4',command=lambda :num('4'))
b5=Button(win,text='5',command=lambda :num('5'))
b6=Button(win,text='6',command=lambda :num('6'))
b7=Button(win,text='7',command=lambda :num('7'))
b8=Button(win,text='8',command=lambda :num('8'))
b9=Button(win,text='9',command=lambda :num('9'))
bx=Button(win,text='X',command=back)
b0=Button(win,text='0',command=lambda :num('0'))
be=Button(win,text='et',command=enter)
psw.grid(row=0,columnspan=3)
b1.grid(row=1,column=0,sticky=W+E)
b2.grid(row=1,column=1,sticky=W+E)
b3.grid(row=1,column=2,sticky=W+E)
b4.grid(row=2,column=0,sticky=W+E)
b5.grid(row=2,column=1,sticky=W+E)
b6.grid(row=2,column=2,sticky=W+E)
b7.grid(row=3,column=0,sticky=W+E)
b8.grid(row=3,column=1,sticky=W+E)
b9.grid(row=3,column=2,sticky=W+E)
bx.grid(row=4,column=0,sticky=W+E)
b0.grid(row=4,column=1,sticky=W+E)
be.grid(row=4,column=2,sticky=W+E)
win.mainloop()




注：
    在Python中，经常会用到各种函数。这些函数有系统中已定义的函数，还有根据自己的需求自定义函数。
    和其他语言一样，在定义自定义函数时，首先要对函数名进行宣言，接着再具体对函数做具体的性质或者操作，
    计算的定义，定义完成后即可以调用已此函数。除此以外，Python语言还有提供了另外的一种简便的无需对
    函数名宣言，即可在代码中使用的自定义函数，就是本文将要说明的lambda函数，也称为无名函数。

    lambda函数
    什么是lambda函数？简单的说就是没有函数名的自定义函数。也称为无名函数。
    在代码编写过程中，有时候需要只使用1次的函数调用，此时即可考虑使用lambda函数。

lambda函数定义
lambda函数用法：

lambda(参数)：（返回值）
参数：lambda函数所用到的变量名称。例如，需要计算1+2时，首先将1和2赋予变量num1,num2。则此时lambda参数为num1,num2。
返回值：需要得到的计算过程。例如，需要变量num1+num2时，返回值就等于num1+num2.
补充说明：当不需要返回计算值时，返回值可以省略，此时lambda函数返回参数值。例如(lambda:'hello')(),会返回文字列hello。

lambda函数代码实例及说明
以下，通过具体的代码示例来说明lambda函数的动作结果。
goukei = lambda num1, num2 ：num1 + num2
print('计算结果：', goukei(1, 2))
运行结果为：
计算结果：3
说明
    第一行的goukei = lambda num1, num2 :num1 + num2，表示将lambda函数的计算结果赋予变量goukei。
    而lambda函数中的计算式，表示将变量num1和变量num2相加。
    第二行中的goukei(1,2)，表示将数值1，2分别赋予lambda函数中的变量num1以及num2,
    并计算结果。而print('计算结果：'……)表示打印输出固定文字列"计算结果："

总结：
在Python中提供一种不需对函数宣言的自定义函数，即为lambda函数。通过自定义函数中的变量以及计算式，
得到满足需求的返回结果。并且，此函数可以直接在主程序中直接定义并使用，所以，可以一定程度提高代码的可读性以及简洁性。
以上，即为Lambda函数在Python中的使用方法说明。
'''
from tkinter import *
def num(a):
    psw.insert('end',a)
def back():
    v = psw.get()
    psw.delete(len(v)-1,'end')
def enter():
    v = psw.get()
    win2=Toplevel()         #重新打开一个新的窗口，该窗口在根窗口的上方

    def ex():
        win2.destroy()
    if v=='123456789':
        Label(win2,text='\n\n密码正确，请等待\n\n').pack()
        Button(win2,text='退出',command=ex).pack()
    else:
        Label(win2, text='\n\n密码不正确，请重新输入\n\n').pack()


win=Tk()
win.title('密码输入器')
psw = Entry(win,relief = 'solid',justify='center')
b1=Button(win,text='1',command=lambda :num('1'))
b2=Button(win,text='2',command=lambda :num('2'))
b3=Button(win,text='3',command=lambda :num('3'))
b4=Button(win,text='4',command=lambda :num('4'))
b5=Button(win,text='5',command=lambda :num('5'))
b6=Button(win,text='6',command=lambda :num('6'))
b7=Button(win,text='7',command=lambda :num('7'))
b8=Button(win,text='8',command=lambda :num('8'))
b9=Button(win,text='9',command=lambda :num('9'))
bx=Button(win,text='X',command=back)
b0=Button(win,text='0',command=lambda :num('0'))
be=Button(win,text='et',command=enter)
psw.grid(row=0,columnspan=3)
b1.grid(row=1,column=0,sticky=W+E)
b2.grid(row=1,column=1,sticky=W+E)
b3.grid(row=1,column=2,sticky=W+E)
b4.grid(row=2,column=0,sticky=W+E)
b5.grid(row=2,column=1,sticky=W+E)
b6.grid(row=2,column=2,sticky=W+E)
b7.grid(row=3,column=0,sticky=W+E)
b8.grid(row=3,column=1,sticky=W+E)
b9.grid(row=3,column=2,sticky=W+E)
bx.grid(row=4,column=0,sticky=W+E)
b0.grid(row=4,column=1,sticky=W+E)
be.grid(row=4,column=2,sticky=W+E)
win.mainloop()
