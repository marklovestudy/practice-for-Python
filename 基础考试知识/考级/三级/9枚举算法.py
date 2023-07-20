'''
枚举算法的概念
    枚举，就是将问题的可能解一个个地列举，逐一判断，即使中途找到符合的解也要继续找下去，将所有可能都找完才结束。
    枚举算法又叫穷举算法，其基本思想是把问题所有的解一一地罗列出来，并对每一个可能解进行判断，以确定这个可能解
    是否是问题的真正解。若是，就采纳这个解，否则就抛弃它。

枚举算法的程序实现
    1列举与检验过程既不重复也不遗漏；
    2尽可能地使可能解的罗列范围最小，以提高解决问题的效率；
    3用循环语句(for)在一定范围内列举所有可能的解；
    4用选择语句(if)判断和选择真正的解。

枚举算法的一般格式
循环结构：
    循环结构：
例1：用50元钱兑换为1，2，5元共25张，每种不少于1张，有多少种方案
for i in range(1,26):
    for j in range(1,26):
        for k in range(1,10):
            if i+2*j+5*k == 50 and i + j + k == 25:
                print('一元%s张，二元%s张，五元%s张'%(i,j,k))
#分析算法和不分析算法的效率差得不是一点半点
#已知条件：每张最少1张，最多为23张，总钱为50元，5元钱最多6张
#算法：枚举算法可实现
#设1元i张，2元j张，5元k张
n = 0
for i in range(1,24):
    for j in range(1,25-i):
        for k in range(1,7):
            if i+2*j+5*k==50 and i+j+k==25:
                print('一元%s张，二元%s张，五元%s张'%(i,j,k))
            n+=1
print(n)
n = 0
for i in range(1,26):
    for j in range(1,26):
        for k in range(1,10):
            if i+2*j+5*k == 50 and i + j + k == 25:
                print('一元%s张，二元%s张，五元%s张'%(i,j,k))
            n+=1
print(n)

例2:如果一个自然数恰好等于它的真因子之和，这个数就是“完全数”。如6=1+2+3。设计一个算法求1000以内的完全数。
真因子：即除了自身以外的约数
for i in range(1000):
    a = set()
    for j in range(1,i):
        if i%j == 0:
            a.add(j)
    a = list(a)
    a.sort(reverse=False)
    if i == sum(a):
        print('%s是全完数'%i,a)

#全面分析问题：因子：能被这个数整除的数叫因子，所有真因子之和等于这个数本身
#所有大于1的整数都能被1整除，所以1是所有数的真因子，循环不用1和本身，如果这个数大于2，本身不能被比较本身小于1的数整除，
#任何一个数不能除大于自已一半的数。
#用枚举算法编程
n=0
for i in range(5,1000):
    a=[]
    for j in range(2,int(i/2)+1):
        if i%j == 0:
            a.append(j)
        n+=1
    v = sum(a)+1
    if v == i:
        print(i,'是完全数。。')
print(n)

n=0
for i in range(1000):
    a = []
    for j in range(1,i):
        if i%j == 0:
            a.append(j)
        n+=1
    if i == sum(a):
        print('%s是全完数'%i,a)
print(n)

例3：查找100以内能被2和3整除的数
for i in range(100):
    if i%2 == 0 and i%3 == 0:
        print('%s能被2和3同时整除'%i)#全面分析问题：能被2整除的数是偶数，能被3整除的数必需是位数和为3的倍数
n=0
for i in range(0,100,6):
    if i%2==0 and i%3==0:
        print(i,'能同时被2和3整除')
    n+=1
print(n)

n=0
for i in range(100):
    if i%2 == 0 and i%3 == 0:
        print('%s能被2和3同时整除'%i)
    n+=1
print(n)

例4：用枚举算法找出所有满足各位数字之和等于7的三位数
for i in range(106,701):
    a = i//100
    b = (i - a*100)//10
    c = i%10
    if a + b + c == 7:
        print('%s这个三位数各位数字之和为7'%i)

例5：
    找回密码：1密码是6位数字，前面两位是85；
            2最后两位数字相同；
            3能被13和33整除
for i in range(850000,860000):
    b = i%100
    b1 = b//10
    b2 = b%10
    if b1 == b2 and i%13 == 0 and i%33 == 0:
        print('密码是%s'%i)


例6：10000以内
有一盒乒乓球，9个9个的数最后余下7个，5个5个的数最后余下2个，4个4个的数最后余下1个。问这盒乒乓球到少有多少个？
方法1：





for i in range(1,10000):
    a_9 = i%9
    a_5 = i%5
    a_4 = i%4
    if a_9 == 7 and a_5 == 2 and a_4 == 1:
        print('这盒乒乓球最少有%s个'%i)
        break

方法2：
n = 1
while True:
    if n%9==7 and n%5==2 and n%4==1:
        print('这盒乒乓球最少有%s个'%n)
        break
    n += 4

方法3：
n = 16
while True:
    if n%5==2:
        break
    n += 9
while True:
    if n%4==1:
        break
    n += 45
print('这盒乒乓球最少有%s个'%n)
'''
s1 = []
for i in range(1,10000):
    a = 0
    for j in range(1,i+1):
        a += j
    if a >= 1000000:
        break
    s1.append(a)

s2 = []
for i in range(1,10000):
    a = i ** 2
    if a >= 1000000:
        break
    s2.append(a)

for i in s1:
    if i in s2:
        print('A和B相同的数有%s'%i)

a = 8
n = 1
while n <= a:
    for x in range(1,1000000000):
        for y in range(1,1000000000):
            if x*(x+1)/2 == y**2:
                print('第%s数是%s'%(n,y**2))
                n += 1
            if y**2 > x*(x+1)/2:
                break
