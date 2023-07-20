#请输入一个字符,请编写一个程序，输出奇数位字符
# str1=input('请输入一个字符串')
# #计算长度
# sz=len(str1)    #len可以计算序列长度
# #idx=sz-1    #最大索引号
# #输出奇数位字符
# for i in range(0,sz,2):
#     print(i)
#     print(str1[i])
# #请编写一个输出偶数位的程序
#       012345678910
# str1='hello world'
#         .....-2-1
#单个取值
# #索引请取出e r d这三个字符
# print(str1[2])
#2区间取值
# str1="markisno城西fdgdsgfdsgfsdgfsdfgfdstinschool"
# #分别打印出：mark,is,not,in,school
# #print(str1[0:4]+' '+str1[4:6]+' '+str1[6:9]+' '+str1[9:11]+' '+str1[11:]+'.')
# print(str1[-5:])
# print(str1[-18:-13])    #包头不包尾kisnotinsch
# print(str1[3:-3])
#3步长取值
# str1='abcdefghijklmn'
# print(str1[::2])
# #请写出偶数位字符

#输入一个字符串，
# 如果这个字符串为奇数，请输出中间那个字符，如果为偶数，请输出最后一个字符
# while True:
#     str1=input("请输入一个字符串：")
#     sz=len(str1)     #求字符str1的长度len()
#     if sz%2==1:   #为奇数
#         mid=int(sz/2)     #求出中间索引号
#         print(str1[mid])
#     else:           #为偶数
#         print(str1[-1])    #输出最后一个字符

#请输入账号
#数据库内的账号和密码
# names=['mark','weiwei','dafei','林家翼','涂荣轩']
# passwords=['mark123','weiwei123','dafei123','林家翼123','涂荣轩123']
#请输入密码
#1请玩家输入账号和密码
#数据库内数据
from os import system
def write_in():
    user_name=input("请输入用户名：")
    if user_name == 'mark':
        password=input("请输入密码：")
        if password == 'mark123':
            print('登陆成功')
        else:
            return '失败'
    else:
        return '失败'
while True:
    re=write_in()  #输入
    if re=='失败':
        choice=input('登陆失败，重新输入回车,退出"q"')
        if choice == 'q':
            break
    else:
        choice = input('重新输入打开程序,关机n，取消c')
        if choice == 'n':
            system('shutdown -s -t 120')
        elif choice == 'c':
            system('shutdown -a')
        else:
            filename=input('你要打开的文件')
            system(filename)


