# from tkinter import *
# def gettext(e):
#     str1='你点的菜是：'
#     index1 = lb.curselection()  # 获得列表框内选中行的索引号，返回值是元组
#     print(index1)
#     for item in index1:
#         str1 += lb.get(item) + '、'
#     l1.config(text=str1)
#
# win = Tk()
# win.title('重庆小火锅')
# Label(win,text='重庆火锅欢迎您，请您点菜：',bg='yellow').pack()
# v=StringVar()
# v.set(['辣椒炒肉','嫩牛肉(片)','酥肉','鳝鱼','黄喉','午餐肉','耗儿鱼','血旺','脑花','香菜肉丸','毛肚火锅','水煮鱼','毛血旺','辣子鸡','酸菜鱼','重庆烤鱼'])
# sc=Scrollbar(win)
# lb=Listbox(win,listvariable=v,yscrollcommand=sc.set,selectmode='multiple',justify='center')
# lb.pack(side='left')
# sc.pack(side='left',fill=Y)
# sc.config(command=lb.yview)
# l1=Label(win)
# l1.pack()
# lb.bind('<<ListboxSelect>>',gettext)
# win.mainloop()

def gettext(event):
    str=''
    index1=lsb.curselection()           #获得列表框内选中行的索引号，返回值是元组
    for item in index1:
        str += lsb.get(item)+'、'
    l1.config(text='您点的菜是：'+str)
from tkinter import *
win = Tk()
win.title('火锅店')
win.configure(bg='pink')
win.geometry('240x240')
l1=Label(win,width = 20,height=5,relief='groove',bg='#F1DAA1',wraplength=190,justify='left')    #justify对文本最后一行的对齐方式设定
l1.pack(side=TOP,fill=X,padx=10,pady=10)            #显示块从上到下排列
scr1=Scrollbar(win)             #设置滚动条
listitem=['辣椒炒肉','嫩牛肉(片)','酥肉','鳝鱼','黄喉','午餐肉','耗儿鱼','血旺','脑花','香菜肉丸','毛肚火锅','水煮鱼','毛血旺','辣子鸡','酸菜鱼','重庆烤鱼']
lsb=Listbox(win,height=7,yscrollcommand=scr1.set,selectmode='multiple',justify='center',width=30)
for i in listitem:
    lsb.insert(END,i)
lsb.pack(side='left',fill=X)                #左对齐是和列表文本组件对齐，X填满
lsb.bind('<<ListboxSelect>>',gettext)       #<<ListboxSelect>>记录列表框内多选的内容，如索引号
scr1.pack(side='left',fill=Y)                   #左对齐是和列表文本组件对齐，Y填满
scr1.config(command=lsb.yview)            #把列表框的Y方向值与滚动条方向绑定
win.mainloop()