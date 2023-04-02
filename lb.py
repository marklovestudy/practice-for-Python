from tkinter import *
import random as r

def pm(l):
    global n
    if n == 0:
        d={}
        for i in l[1:]:
            name=i
            s=eval('+'.join(i.strip().split()[1:]))
            d[name]=s
        lt=list(d.items())
        lt.sort(key=lambda x:x[1],reverse=True)
        for i in range(1,len(l)):
            l[i]=lt[i-1][0]+'{:^6}'.format(lt[i-1][1])
        l[0]='{:^6}{:^4}{:^4}{:^4}{:^4}'.format('姓名','语文','英语','数学','总分')
        listbox.delete(0,len(l))
        v.set(l)
        n=1
n=0
win = Tk()
class_mates=['{:^6}{:^6}{:^6}{:^6}'.format('同学%s'%i,r.randint(0,100),r.randint(0,100),r.randint(0,100)) for i in range(1,31)]
class_mates.insert(0,'{:^6}{:^4}{:^4}{:^4}'.format('姓名','语文','英语','数学'))
v=StringVar()
v.set(class_mates)
listbox=Listbox(win,listvariable=v,width =25,height=31)
listbox.pack()
lb=Label(win)
lb.pack()
Button(win,text='一键排名',command=lambda :pm(class_mates)).pack()
win.mainloop()
