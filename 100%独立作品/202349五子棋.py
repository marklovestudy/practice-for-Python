'''
五子棋
'''
#主循环
from tkinter import *
from tkinter.messagebox import *
arr=[]          #创建全局数组，记录20x20的数据
who=['*','#']   #玩家*和玩家#
dex=0           #索引，主要取谁在下的值
def pd(x,y):    #判断每下一步是谁赢了
    global arr
    #判断是否格子下满了
    re=1
    for i in arr[5:15]:             #棋盘是20*20，但是棋手只能下在5-15中，而0，1，2，3，4和15，16，17，18，19是隐藏的
        for j in i[5:15]:
            if j.get() == '':
                re=0
                break
        print(re)
        if re == 0:
            break
    if re == 1:
        return 'c'      #如果格子下满，平局
    #坚向相同  返回相同的棋子
    for z in range(-4,1):
        ret=[]
        for i in range(x+z,x+z+5):
            if arr[i][y].get() != '':
                ret.append(arr[i][y].get())
        if len(ret) == 5 and len(set(ret)) == 1:
            return ret[0]
    #横向
    for z in range(-4,1):
        ret=[]
        for i in range(y+z,y+z+5):
            if arr[x][i].get() != '':
                ret.append(arr[x][i].get())
        if len(ret) == 5 and len(set(ret)) == 1:
            return ret[0]
    #斜线1
    for z in range(-4,1):
        ret=[]
        for i,j in zip(range(x+z,x+z+5),range(y+z,y+z+5)):
            if arr[i][j].get() != '':
                ret.append(arr[i][j].get())
        if len(ret) == 5 and len(set(ret)) == 1:
            return ret[0]
    #斜线2
    for z in range(-4,1):
        ret=[]
        for i,j in zip(range(x+z,x+z+5),range(y-z,y-z-5,-1)):
            if arr[i][j].get() != '':
                ret.append(arr[i][j].get())
        if len(ret) == 5 and len(set(ret)) == 1:
            return ret[0]

def aa(x,y,win):            #把棋手*和#下的位置记录在arr5-15中
    global arr,dex
    re1=22
    if arr[x+5][y+5].get() == '':       #如果棋盘格子上是 ''可以落棋
        arr[x+5][y+5].set(who[dex])
    else:
        return 0                        #否则无效
    re=pd(x+5,y+5)                      #每下一步进行判断：平局？   *赢   #赢
    if re == '*':
        re1=askyesno('ok', '*赢了')
    elif re == '#':
        re1=askyesno('ok', '#赢了')
    elif re == 'c':
        re1=askyesno('ok', '平局')
    if re1 == True:                     #选择是重新开始
        game(win)
    elif re1 == False:                  #选择否退出
        win.quit()
    vv = StringVar()
    vv.set('玩家下')
    l = Label(win, textvariable=vv)
    l.grid(row=10, columnspan=10)
    if dex == 0:                #通过索引取值，把玩家*#下的棋正确配对
        dex = 1
        vv.set('玩家#下')
    else:
        dex =0
        vv.set('玩家*下')

def md(i,j,win,v):          #设置按键用来做为棋位
    Button(win, font=14, width=3, height=1, textvariable=v, command=lambda : aa(i, j, win)).grid(row=i, column=j)

def gc(win):                #生成棋盘，10*10的格子。
    global arr,dex
    for i in range(-5,15):
        lj=[]
        for j in range(-5,15):
            v=StringVar()
            lj.append(v)
            if 0<=i<=9 and 0<=j<=9:
                md(i,j,win,v)
        arr.append(lj)          #arr是20*20，只用中间的5-15，5-15，来存棋手的棋子数据

def game(w):        #启动游戏
    global arr,dex
    w.destroy()
    arr=[]      #初始化，因为后面可能要重玩
    win = Tk()
    #生成棋格
    gc(win)
    win.mainloop()

def out(w):
    w.destroy()

def choice():
    win=Tk()
    win.geometry('110x140')
    #选择开始游戏
    Button(win,text='开始游戏',command=lambda : game(win)).grid(row=1,column=0)
    #选择结束游戏
    Button(win, text='退出游戏',command=lambda : out(win)).grid(row=1,column=1)
    Label(win,text='五子棋',bg='pink').grid(row=0,columnspan=2)
    win.mainloop()

def main():
    global arr
    print('游戏开始。')
    #选择游戏是否开始
    choice()
if __name__ == '__main__':
    main()