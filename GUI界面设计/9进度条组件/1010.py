def rego():
    pro.stop()
    pro.step(amount=5)
    pro.start()
from tkinter import *
from tkinter.ttk import *
win=Tk()
win.title('灵魂画师')
ima1=PhotoImage(file='draw.png')
l=Label(win,image=ima1,text='灵魂画师',compound=BOTTOM,font=('华文新魏',18),foreground='red')
l.grid(row=0,column=1,padx=20,pady=10)
v1=IntVar()
val=0
v1.set(val)
pro=Progressbar(win,value=0,max=100,mode='determinate',length=200)
pro.grid(row=1,columnspan=3,pady=10)
Button(win,text='进入游戏',command=pro.start).grid(row=2,column=0,pady=10)
Button(win,text='游戏加速',command=rego).grid(row=2,column=1,pady=10)
Button(win,text='停止游戏',command=pro.stop).grid(row=2,column=2,pady=10)
win.mainloop()