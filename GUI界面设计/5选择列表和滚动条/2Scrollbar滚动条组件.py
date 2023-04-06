'''
def gettext(event):
    str=''
    index1=fruites.curselection()           #获得列表框内选中行的索引号，返回值是元组
    print(index1)
    for item in index1:
        str += fruites.get(item)+'、'
    l1.config(text='你选择了'+str)

from tkinter import *
win = Tk()
win.configure(bg='pink')
win.geometry('240x240')

l1=Label(win,width = 20,height=5,relief='groove',bg='#F1DAA1',wraplength=190,justify='left')    #justify对文本最后一行的对齐方式设定
l1.pack(side=TOP,fill=X,padx=10,pady=10)            #显示块从上到下排列

scr1=Scrollbar(win)             #设置滚动条
listitem=['苹果','香蕉','梨','葡萄','圣女果','百香果','菠萝','西瓜','香瓜','草莓','水桃','油桃','蜜枣','柠檬','牛柚果','冰糖柚','桔子','橙子','巴西桔','枣子']
fruites=Listbox(win,height=7,yscrollcommand=scr1.set,selectmode='multiple',justify='center',width=30)
for i in listitem:
    fruites.insert(END,i)
fruites.pack(side='left',fill=X)                #左对齐是和列表文本组件对齐，X填满
fruites.bind('<<ListboxSelect>>',gettext)       #<<ListboxSelect>>记录列表框内多选的内容，如索引号
scr1.pack(side='left',fill=Y)                   #左对齐是和列表文本组件对齐，Y填满
scr1.config(command=fruites.yview)            #把列表框的Y方向值与滚动条方向绑定
win.mainloop()

'''


def gettext(event):
    str=''
    index1=fruites.curselection()           #获得列表框内选中行的索引号，返回值是元组
    print(index1)
    for item in index1:
        str += fruites.get(item)+'、'
    l1.config(text='你选择了'+str)

from tkinter import *
win = Tk()
win.configure(bg='pink')
win.geometry('240x240')

l1=Label(win,width = 20,height=5,relief='groove',bg='#F1DAA1',wraplength=190,justify='left')    #justify对文本最后一行的对齐方式设定
l1.pack(side=TOP,fill=X,padx=10,pady=10)            #显示块从上到下排列

scr1=Scrollbar(win)             #设置滚动条
listitem=['苹果','香蕉','梨','葡萄','圣女果','百香果','菠萝','西瓜','香瓜','草莓','水桃','油桃','蜜枣','柠檬','牛柚果','冰糖柚','桔子','橙子','巴西桔','枣子']
fruites=Listbox(win,height=7,yscrollcommand=scr1.set,selectmode='multiple',justify='center',width=30)
for i in listitem:
    fruites.insert(END,i)
fruites.pack(side='left',fill=X)                #左对齐是和列表文本组件对齐，X填满
fruites.bind('<<ListboxSelect>>',gettext)       #<<ListboxSelect>>记录列表框内多选的内容，如索引号
scr1.pack(side='left',fill=Y)                   #左对齐是和列表文本组件对齐，Y填满
scr1.config(command=fruites.yview)            #把列表框的Y方向值与滚动条方向绑定
win.mainloop()
