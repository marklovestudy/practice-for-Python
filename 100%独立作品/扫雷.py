from tkinter import *
from tkinter.messagebox import *
import random as r

def pd(win,mine_arr,x,y,vs):        #判断当前格子是否是雷。
    print(x,y)
    if 0<=x<=10 and 0<=y<=10 and vs[x][y].get() == '':
        if mine_arr[x+1][y+1]=='*':
            vs[x][y].set('*')
            re=askyesno('输了','你挂了，请选择')
            if re == True:
                game(win)
            else:
                ex(win)
        else:
            ret=str(mine_arr[x][y])+str(mine_arr[x+1][y])+str(mine_arr[x+2][y])+str(mine_arr[x][y+1])+str(mine_arr[x+2][y+1])+str(mine_arr[x][y+2])+str(mine_arr[x+1][y+2])+str(mine_arr[x + 2][y+2])
            ret=ret.count('*')
            vs[x][y].set(ret)
            if ret == 0:            #算法：递归扫除无雷时周围的格子
                pd(win, mine_arr,  x-1, y-1,vs)
                pd(win, mine_arr,  x, y - 1,vs)
                pd(win, mine_arr,  x+1, y - 1,vs)
                pd(win, mine_arr,  x - 1, y,vs)
                pd(win, mine_arr,  x + 1, y,vs)
                pd(win, mine_arr,  x - 1, y + 1,vs)
                pd(win, mine_arr,  x, y + 1,vs)
                pd(win, mine_arr,  x + 1, y + 1,vs)
    else:
        return

def c_b(win,mine_arr,i,j,vs):
    Button(win, textvariable=vs[i][j], font=14, width=3, command=lambda: pd(win, mine_arr,i, j,vs)).grid(row=i, column=j)


def init_mine_bt(win,mine_arr,x,y):         #初始化雷数据v(stringvar)变量
    vs=[]
    for i in range(x):
        vs1=[]
        for j in range(y):
            v=StringVar()
            v.set('')
            vs1.append(v)
        vs.append(vs1)
    for i in range(x):
        for j in range(y):
            c_b(win, mine_arr, i, j,vs)
    return vs

def set_mine(mine_arr,num):     #设置地雷
    while num>0:
        x=r.randint(1,10000)%10+1
        y = r.randint(1,10000)%10+1
        if mine_arr[x][y] == 0:
            mine_arr[x][y] = '*'
            num -=1
        print(num)

def init_mine_data(x,y):        #创建雷数据，设置为比显示区域大2格
    ls=[]
    for i in range(x):
        ls1=[]
        for j in range(y):
            ls1.append(0)
        ls.append(ls1)
    return ls

def game(win):
    win.destroy()
    win=Tk()
    #初始化数据
    #显示棋盘
    i,j=10,10
    #初始化雷的数据
    mine_arr=init_mine_data(i+2,j+2)
    #布雷
    num=10
    set_mine(mine_arr,num)
    #初始化格子
    vs=init_mine_bt(win,mine_arr,i,j)
    win.mainloop()

def ex(w):      #选择退出游戏后关闭窗口
    w.destroy()

def pp():       #显示首页选择页面
    win = Tk()
    win.title('扫雷')
    Label(win, text='欢迎您！！扫雷游戏，请选择').grid(row=0, columnspan=2)
    Button(win, text='开始游戏',command=lambda :game(win)).grid(row=1, column=0)
    Button(win, text='退出游戏',command=lambda :ex(win)).grid(row=1, column=1)
    win.mainloop()

def main():
    pp()

if __name__ == '__main__':
    main()