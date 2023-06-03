n=0
for i in range(1,19):
    for j in range(1,21):
        for k in range(1,7):
            n+=1
            if i+2*j+5*k == 50 and i + j + k == 25:
                print('一元%s张，二元%s张，五元%s张'%(i,j,k))
print(n)

#每张最少一张，最多23次   1最多18   32       2   30
#2块 最少一张  最多21    42       8        3   5
#5块 最少一张  最多6

# 如果一个自然数恰好等于它的真因子之和，这个数就是“完全数”。如6=1+2+3。设计一个算法求1000以内的完全数。
# 真因子：即除了自身以外的约数
# for n in range(6,1000):
#     for i in range(2,n):
#         if n%i==0:
#             #i是他的约数。存起来
#         #所有存起来的约数加起是不是等于n??
#24W   50W

for n in range(6,1000):         #枚举6-1000的数
    a=[]
    for i in range(1,n//2+1):

        if n%i==0:          #i是n的约数。
            a.append(i)
            #i是他的约数。存起来
        #所有存起来的约数加起是不是等于n??
    if sum(a)==n:
        print(n,'是完全数')

# 1枚举算法找出所有满足各位数字之和等于7的三位数
#
# 2找回密码：1密码是6位数字，前面两位是85；
#             2最后两位数字相同；
#             3能被13和33整除
#
# 3有一盒乒乓球，9个9个的数最后余下7个，5个5个的数最后余下2个，4个4个的数最后余下1个。问这盒乒乓球到少有多少个？
for i in range(850000,860000):
    b = i%100
    b1 = b//10
    b2 = b%10
    if b1 == b2 and i%13 == 0 and i%33 == 0:
        print('密码是%s'%i)