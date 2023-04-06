from tkinter import *
from tkinter.ttk import *
win=Tk()
tree = Treeview(win,columns=('hero','type','operate'),displaycolumns=(0,1,2))   #创建三列'hero','type','operate'
tree.heading('hero',text='ok')
tree.heading('type',text='male')
tree.heading('operate',text='fds')
sun=tree.insert('',0,values=['孙尚香','射手','5'])
liu=tree.insert('',1,values=['刘孙香','手','6'])
sun2=tree.insert(sun,0,text='孙城')
tree.insert(sun,1,text='孙埼')
tree.insert(sun,2,text='孙下载')
tree.insert(sun2,0,text='fdss')
tree.insert(sun2,1,text='iiihjh')
tree.pack()
win.mainloop()