from tkinter import *
from tkinter.messagebox import *
def pp():
    v=showerror('中毒了','你的胆子是真的大')
    if v=='ok':
       pp()
win=Tk()        #创建容器对象
ima=PhotoImage(file='1.png')    #创建图片对象
Button(win,image=ima,text='点我试试',compound='center',
       font=('黑体 20 bold'),fg='red',command=pp).pack()
x=100
y=100
x_v=0.1
y_v=0.05
while True:
       win.geometry('100x100+%d+%d'%(x,y))
       x+=x_v
       y+=y_v
       if x<0 or x>1200:
              x_v=-x_v
       if y<0 or y>600:
              y_v=-y_v
       win.update()