from tkinter import *
win = Tk()
win.title('位置设置')
win.configure(bg='#a7ea90')
winw=300
winh=220
scrw=win.winfo_screenwidth()        #获取屏幕宽度
scrh=win.winfo_screenheight()       #获取屏幕高度
x=(scrw-winw)/2
y=(scrh-winh)/2
win.geometry('%dx%d+%d+%d'%(winw,winh,x,y))
str="\n\n程序员鄙视链\n\n一等码农搞算法，吃香喝辣调调参\n\n二等码农搞架构，高并低延能吹牛\n\n三等码农搞工程，怼天怼地怼PM\n\n四等码农搞前端，浮层像素老黄牛"
txt=Label(win,text=str,bg='#a7ea90',font='华文新魏 12 bold').pack()
win.mainloop()