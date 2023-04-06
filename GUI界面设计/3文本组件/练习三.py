from tkinter import *
import random as r
win=Tk()
images=['smile.png','ok.png','cry.png']
for i in range(3):
    exec('ima%s=PhotoImage(file=images[%d])'%(i,i))
for i in range(20):
    for j in range(40):
        Button(win,image=eval('ima%s'%r.randint(0,2))).grid(row=i,column=j)
win.mainloop()