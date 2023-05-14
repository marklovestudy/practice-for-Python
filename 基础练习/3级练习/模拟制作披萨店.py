'''
#披萨服务系统
1来了一个顾客
2询问顾客干点什么事呢。：
    1点餐。：1制作顾客要求披萨。
           2吃披萨
           3结账
    2会员服务
'''
import time

def pay_money():
    name=input("请输入会员名字：不是会员请输入0")
    with open('comters.txt', 'r', encoding='utf-8') as f:
        str1=f.read()
        if name in str1:
            print('给您打完拆后是23元。')
        else:
            print('您不是会员，你的花费为50元。')
    print('欢迎下次光临。')

def order():
    #1制作顾客要求披萨。
    menu=input('你要吃什么口味的披萨（输入格式“西瓜,草莓”）。')       #输入格式'西瓜,草莓'
    # or_ls=menu.split(',')                 #你点的水果PIZZA列表
    for i in range(51):
        print('制作中，制作进度{}%'.format(2*i))
        time.sleep(1)
    print('你的{}味PIZZA做好了，用餐愉快'.format(menu))
    print('用餐中')
    time.sleep(10)
    pay_money()

def vip():
    re=input('请选择：0退出，1为注册会员，2注销会员')
    with open('comters.txt','r+',encoding='utf-8') as f:
        str1=f.read()
        if re == '0':
            print('用户退出')
            return
        elif re == '1':
            name = input('请输入名字：')
            if name in str1:
                print('用户已经注册，请重新输入')
                vip()
            else:
                f.write(','+name)
                print('{}已经为您注册好了'.format(name))
        elif re == '2':
            name = input('请输入名字：')
            if name in str1:
                with open('comters.txt', 'w', encoding='utf-8') as fo:
                    ls=str1.split(',')
                    ls.remove(name)
                    str2=','.join(ls)
                    fo.write(str2)
                    print('用户已经删除。')
            else:
                print('此用户不是会员')
    pizza_system()

def pd(re):
    if re == '1':
        order()         #点餐
    elif re == '2':
        vip()           #会员服务
    else:
        print('输入错误，请重新输入')
        pizza_system()

def weclome():
    print('************************************')
    print('***      1:点餐   2：会员服务      ***')
    print('************************************')
    re=input('请选择：')
    return re

def pizza_system():
    re=weclome()       #选择的是1，点餐，2表示会员服务
    pd(re)             #用来判断用户口的选择结果

if __name__ == '__main__':
    pizza_system()          #这是一个函数。PIZZA店的服务系统