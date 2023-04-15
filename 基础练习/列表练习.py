'''
关机程序：
询问：七个人
选择关机
选择取消关机
'''
#打印消息：询问玩家是否开始游戏游戏
# while True:
#     print("************************")
#     print("**** 1play  0exit ******")
#     print("************************")
#     re=input("您的选择是：")
#     #判断是否开始游戏
#     if re == '1':
#         print('游戏开始')
#         #打印棋盘
#         print('   |   |   ')
#         print('-----------')
#         print('   |   |   ')
#         print('-----------')
#         print('   |   |   ')
#         #初始化数据
#         list1=[['','',''],['','',''],['','','']]
#         #玩家下        '*'
#         x,y=eval(input('x?,y?'))
#         if 1<=x<=3 and 1<=y<=3:
#             list1[x-1][y-1]='*'
#             print(list1)
#         #刷新棋盘
#         print(' {} | {} | {} '.format(list1[0][0], list1[0][1], list1[0][2]))
#         print('-----------')
#         print(' {} | {} | {} '.format(list1[1][0], list1[1][1], list1[1][2]))
#         print('-----------')
#         print(' {} | {} | {} '.format(list1[2][0], list1[2][1], list1[2][2]))
#         #玩家赢了吗
#         #横向
#         if list1[0][0]==list1[0][1] and list1[0][1]==list1[0][2] and list1[0][0] != '':
#             print("{}赢啦",list1[0][0])
#         #电脑下        #
#         #电脑赢了吗
#         break
#
#
#     elif re=='0':
#         print('退出游戏')
#         break       #跳出当前循环体
#     else:
#         print('请重新输入')

from os import system
for i in range(3):
    re=input('你要关机吗?')
    if re == '1':
        print('关机')
        system('shutdown -s -t 119')
    elif re == '0':
        print('取消关机')
        system('shutdown -a')
    else:
        print('打开文件')
        system('C:/Users/Administrator/Desktop/413森林求生.sb3')