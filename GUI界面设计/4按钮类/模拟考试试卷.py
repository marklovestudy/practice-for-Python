from tkinter import *
win=Tk()
def pd():
    scroe=0
    for i in range(len(list2)):
        if list2[i] == list3[i].get()[0]:
            scroe+=1
    l1.config(text='最后得分是：'+str(scroe))
list1=[
    ['世界上最大的国家是：','A美国','B俄罗斯','C中国','D加拿大'],
    ['世界上最大的动物是：','A蓝鲸','B恐龙','C飞龙','D海马'],
    ['黑色是怎么形成的：','A无色','B白色和灰色','C蓝色和灰色','D无光']
]
list2=['B','A','D']
list3=[]
for i in list1:
    v=StringVar()
    v.set(' ')
    l=Label(win,text=i[0])
    l.pack()
    r1=Radiobutton(win,variable=v,value=i[1],text=i[1]).pack(anchor='w')
    r2=Radiobutton(win,variable=v,value=i[2],text=i[2]).pack(anchor='w')
    r3=Radiobutton(win,variable=v,value=i[3],text=i[3]).pack(anchor='w')
    r4=Radiobutton(win,variable=v,value=i[4],text=i[4]).pack(anchor='w')
    list3.append(v)
Button(win,text='确定',command=pd).pack()
l1=Label(win,text='')
l1.pack()
win.mainloop()