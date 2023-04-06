from tkinter import *           #标准库 turtle,tkinter      pygame   第三方库
from tkinter.messagebox import *
from webbrowser import open
def aa():
    mesb=askyesnocancel('消息','是否查询')
    if mesb:
        win2=Tk()
        def bb():
            wd = e1.get()
            open('https://www.baidu.com/s?wd=%s'%wd)
            return
        e1=Entry(win2)
        e1.pack()
        Button(win2,text='确定',command=bb).pack()

        win2.mainloop()
win1 = Tk()             #创建一个屏幕
pic1=PhotoImage(file='1.png')       #创建一个文件对象
Button(win1,text='ok',command=aa,image=pic1).pack()
win1.mainloop()

#修改图片大小
# from PIL import Image,ImageTk       #pillow
# pic1=Image.open('1.png')
# pic1=pic1.resize((100,100),Image.LANCZOS)
# pic1=ImageTk.PhotoImage(pic1)