'''
三子棋
'''
#主循环
from tkinter import *
arr=[]
who=['*','#']
dex=0
def aa(x,y,win):
    global arr,dex
    print(dex)
    arr[x][y].set(who[dex])
    vv = StringVar()
    vv.set('玩家下')
    # 生成棋格
    l = Label(win, textvariable=vv)
    l.grid(row=10, columnspan=10)


def gc(win):
    global arr,dex
    for i in range(10):
        lj=[]
        for j in range(10):
            v=StringVar()
            b = str('{}_{}'.format(i,j))
            lj.append(v)
            exec('b%s=Button(win,font=14,width=3,height=1,textvariable=v,command=lambda :aa(%d,%d,%s))'%(b,i,j,win))
            eval('b%s'%b).grid(row=i,column=j)
        arr.append(lj)

def game(w):
    global dex
    w.destroy()
    win = Tk()
    vv = StringVar()
    vv.set('玩家下')
    #生成棋格
    gc(win)
    l = Label(win, textvariable=vv)
    l.grid(row=10, columnspan=10)
    win.mainloop()

def out(w):
    w.destroy()

def choice():
    win=Tk()
    #选择开始游戏
    Button(win,text='开始游戏',command=lambda : game(win)).pack(side='left')
    #选择结束游戏
    Button(win, text='退出游戏',command=lambda : out(win)).pack(side='left')
    win.mainloop()

def main():
    global arr
    print('游戏开始。')
    #选择游戏是否开始
    choice()
if __name__ == '__main__':
    main()