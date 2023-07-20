#monster = ['骷髅兵','僵尸','异形','Boss','精英骷髅兵','精英僵尸','精英异形']
#1创建一个生成器        推导式创建
#2由生成器生成一个怪物（生成器.__next__(),next(生成器)）。精英怪血量为1000，普通怪血量为100.
#3打印攻击怪物的过程：
#当前异形：血量100，防御：6，攻击：6
# 当前异形： 血量94，防御：6，攻击：6
# 当前异形： 血量85，防御：6，攻击：6
# 当前异形： 。。。。。。
# 当前异形： 。。。。。。
# 当前异形： 血量3，防御：6，攻击：6
# 当前异形： 阵亡。。
# import random as r
# import time
# monster = ['骷髅兵','僵尸','异形','Boss','精英骷髅兵','精英僵尸','精英异形']
# #创建一个生成器，推导式创建元组
# t1=(monster[r.randint(0,6)] for i in range(100))      #(元素 个数)
# for i in range(100):
#     name_monster=t1.__next__()      #生成了一个怪物,同时创建怪物属性
#     if name_monster in ['骷髅兵','僵尸','异形']:
#         xl=100;fy=6;gj=6
#     elif name_monster in ['精英骷髅兵','精英僵尸','精英异形']:
#         xl=1000;fy=16;gj=16
#     else:
#         xl = 3000;fy = 26;gj = 26
#     while xl>0:
#         print("当前怪物为{},血量：{}，防御：{}，攻击：{}".format(name_monster,xl,fy,gj))
#         xl-=r.randint(15,35)         #每次循环掉15到35滴血
#         time.sleep(0.5)
#     print("当前怪物为{}已阵亡。。。".format(name_monster))
#     time.sleep(0.5)

#请输入一个八进制数，输出10进制的数
#如：输入77，输出63
# num=input('输入0-7的八进制数')  #'777'
# #num=int(num,8)     #方法1
# #方法2
# n1=0
# for i in num:       #'7'  eval('7')   7
#     n1=eval(i)+n1*8
# print(n1)

