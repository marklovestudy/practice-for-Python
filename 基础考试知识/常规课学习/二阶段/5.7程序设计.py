'''
#创建列表
 list1=[1,2,3,'mark',[4,5,6,7]]
list1
[1, 2, 3, 'mark', [4, 5, 6, 7]]
list2=[]
list2
[]

#>>> list2.append('谢政洪')
#>>> list2
#['谢政洪']
#>>> list2.append('谢政江')
#>>> list2
#['谢政洪', '谢政江']
'''
from os import system                   #载入标准库os
def bc():           #break和continue的使用
    # for x in range(4):
    #     i=0
    #     while True:
    #         i+=1
    #         if i == 6:
    #             break           #打破，摧毁，破坏（跳出当前循环体）(for / while)
    #         else:
    #             print(i)
    #     print('ok')
    for i in range(5):
        if i == 3:
            continue           #继续          跳出当次循环
        else:
            print(i)
        print('ok')

def main():     #函数
    ls=[]   #1创建一个列表
    ls.append('谢政江')     #2在列表中添加四个人
    ls.append('谢政洪')
    ls.append('关浩华')
    ls.append('黄天乐')
    for name in ls:            #3遍历列表      for i in 序列：
        re=input('你好:%s，欢迎来到主控室，请您选择1/2/3'%name)       #4对玩家进行询问操作
        if re == '1':               #5不同选择程序作出不同的反应
            system('shutdown -s -t 60')                #关机
        elif re == '2':
            system('shutdown -a')                   #取消关机
        elif re == '3':
            system(r'C:\Users\Administrator\Desktop\57.sb3')                     #打开文件
        else:
            print('你输错了，you are stuiped')
if __name__ == '__main__':      #当运行当前文件时，执行下面程序
    #main()
    bc()