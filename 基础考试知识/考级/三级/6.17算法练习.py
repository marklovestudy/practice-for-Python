# 1练习冒泡算法。
# 1第一个for循环确定轮数
# 2第二个for循环确定范围

import random as r

def maopao(l):
    sz = len(l)
    for i in range(sz - 1):
        for j in range(sz - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]


def selectsort(l):
    sz = len(l)
    for i in range(sz - 1):
        for j in range(i + 1, sz):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]


def fun(n):
    ans = 0  # 转成的十进制数，也就是用来存储目标数的变量
    i = 1
    while n:
        t = n % 10  # 取余
        ans = ans + t * i
        i *= 8
        n //= 10  # 取整
    return ans


def fun1(n):  # 输入一个数123，输出一个321
    ans = 0
    while n:
        t = n % 10  # 取余
        ans = ans*10 + t
        n //= 10  # 取整
    return ans


if __name__ == '__main__':
    # ls=[r.randint(0,100) for i in range(25)]
    # print(ls)
    # maopao(ls)
    # selectsort(ls)
    # print(ls)
    # 输入一个字符串：数字0-7的八进制，然后十进数字输出
    # 如“707”，输出：455
    # while True:
    #     num=eval(input("请输入一个0-7的数字："))
    #     re=fun(num)
    #     print("八进制：{}转成十进制数：{}".format(num,re))

    # 输入一个数123，输出一个321
    while True:
        num = eval(input("请输入一个数字："))
        re = fun1(num)
        print("数字{}反向排序后{}".format(num, re))
