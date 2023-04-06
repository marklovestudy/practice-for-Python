def pp(n):
    print(n)
from tkinter import *
win=Tk()
list1=[]
for i in range(5):
    list1.append(lambda :pp(i))
    Button(win, text='OK', command=list1[i]).pack()


win.mainloop()