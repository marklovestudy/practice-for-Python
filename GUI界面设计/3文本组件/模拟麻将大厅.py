from tkinter import *
from PIL import Image,ImageTk      #pip install pillow
#1制作窗口
win = Tk()
win.title('麻将馆')
win.configure(bg='yellow')          #背景颜色
#2显示模块
def remade(image,w,h):          #修改图片的大小
    ima = Image.open(image)                 #创建图片对象
    ima = ima.resize((w,h),Image.LANCZOS)   #修改大小
    ima = ImageTk.PhotoImage(ima)           #转成TK图片
    return ima
ima1=remade('desk.png',100,100)             #修改桌子的大小
ima2=remade('chair.png',30,30)              #修改椅子的大小
#加载桌子，#加载椅子
for i in range(1,10,3):
    for j in range(1,13,3):
        Label(win,image=ima1).grid(row=i,column=j)
        Button(win,image=ima2).grid(row=i-1,column=j)
        Button(win, image=ima2).grid(row=i+1, column=j)
        Button(win, image=ima2).grid(row=i, column=j-1)
        Button(win, image=ima2).grid(row=i, column=j+1)
win.mainloop()      #内置循环
