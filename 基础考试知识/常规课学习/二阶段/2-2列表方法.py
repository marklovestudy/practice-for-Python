"""
1、append()原来列表的最后添加元素                               8
li = [1,3,4,5]
v = li.append(6)  #把6添加到列表li的最后一项*
print(li)

2、clear()清空列表                                           6
li = [1,3,4,5]
v = li.clear()
print(li)

3、copy()浅拷贝                                             6
li = [1,3,4,5]
v = li.copy()
print(v)

4、count()计算元素的数量                                    8
li = [1,3,4,5]
v = li.count(3)
print(v)   #输出：1

5、extend()在列表后添加可迭代对象                           6
li = [1,3,4,5]
v = li.extend([66,"mark"])#extend里面加可迭代对象，用的是for循环添加
print(li)
注：
for i in [66,"mark"]
    li.append(i)
#[1, 3, 4, 5, 66, 'mark']

6、index()根据值找到值的位置index()，从左开始找，找到一个就不向后面找了。        6
li = [1,3,4,5,3]
v = li.index(3)
print(v)   #输出 1

7、 insert(2,66)在指定位置插入值。            8-10
li = [1,3,4,5,3]
v = li.insert(2,66)
print(li)

8、pop()默认删除最后一个元素的值，并获取删除的值，如果指定索引，将删除索引的值，并获得这个值。
li = [1,3,4,5,3]
v = li.pop()
print(li)
print(v)

9、remove()删除指定值，左边优先                6
li = [1,3,4,5,3]
v = li.remove(3)  #不获得值
print(li)    #[1, 4, 5, 3]
print(v)

10、reverse()将当前列表翻转             #3
li = [1,3,4,5,3]
v = li.reverse()
print(li)
print(v)

11、sort()排序，从小到大reverse = False    从大到小排reverse = True
li = [1,3,4,5,3]                        #6
v = li.sort(reverse=False)
print(li)   #[1, 3, 3, 4, 5]
print(v)
"""
##用while循环做披萨店点餐系统
# while False:     #为真(True)时执行，为假(False)时停止
#     print(1)
#     print(2)
#     print(3)
# print('ok')
#进店操作系统
#1创建一个新列表---用来存储顾客名字
#2询问顾客名字        input()
#3进行判断：1是会员，说欢迎。2不是会员，顾客成为新的会员。
#4做一个注销会员的系统：1输入名字：1在列表中，删除，2不在列表中。说输入错误
#5进店点餐系统

def join_system():     #定义函数，join_system是函数名字，()调用符     #进店操作
    print('这里网红披萨店：')
    name=input('您好，请输入名字：')       #询问顾客名字
    if name in comsters:                #判断顾客是否是会员
        print("欢迎您到光临。")
    else:
        comsters.append(name)           #把顾客名字添加到列表comsters中
    print(comsters)                     #打印列表信息

def delete_system():        #这个函数的作用是删除已有的会员的。
    name=input("请输入要注销的会员名字")
    #判断是否在列表中，在就删除，不在就说输入错误
    if name in comsters:            #判断名字是不是在列表中
        comsters.remove(name)       #通过值删除会员
    else:
        #while name not in comsters:
        print("输入错误")
    print(comsters)

def order_system(name):
    its=input('what do you want to eat?')       #用逗号隔开      西瓜，东瓜
    v=[name]
    print(v)
    print(its.split(','))
    v.extend(its.split(','))            #its.split(',')把用户输入的内容，以','为分割符，分割成一个列表。
    print(v)
    if name in comsters:
        #打骨折
        l=len(v)-1
        money=0.5*l*10
    else:
        #收2倍
        l = len(v) - 1
        money = 2 * l*10
    print('{}点了{}披萨，收取{}元。'.format(name,v[1:],money))
if __name__ == '__main__':
    # 进店操作系统
    comsters=[]     #存储顾客名字
    orders=[]       #用来存储顾客点的东西
    name = input("请输入您的名字：")
    re=input('请您选择业务类型，1注册和登陆会员，2注销会员，3点餐')
    if re == '1':
        join_system()
    elif re == '2':
        #注销会员的系统
        delete_system()
    elif re == '3':
        # # 进店点餐系统
        order_system(name)
    else:
        print('你的手像脚，输错了呢。')

# users = []
# while True:
#     name = input('请输入您的名字：')
#     if name in users:
#         print('欢迎再次光临',name)
#     else:
#         print('感谢您成为新会员')
#     users.append(name)
#     delname = input('你要删除的会员：')
#     if delname == '':
#         continue
#     users.remove(delname)       #删除已经存在的元素，如果不存在会报错
#     print(users)
