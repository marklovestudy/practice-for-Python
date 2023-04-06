# win.title('text文本学习')
# text1=Text(win,bg='pink')
# text1.pack()
# text1.insert('end','mark牵城量堿')      #给text文本组件添加内容
# text1.delete(1.0,1.3)          #删除从第一行的0号索引---第一行的3号索引，包头不包尾
# v=text1.get(1.0,'end')          #获取所有的内容起始位置，结束位置
def buy():
    print(s1.get(),s2.get())
    text1.insert('end','你购买了%s，购买数为：%s.\n'%(s2.get(),s1.get()))
from tkinter import *
win = Tk()
s1=Spinbox(win,from_=1,to=31)
s1.pack()
v=['包子','鞋子','衣服','书包']
s2=Spinbox(win,values=v)
s2.pack()
Button(win,text='buy',command=buy).pack()
text1=Text(win,bg='pink')
text1.pack()
win.mainloop()