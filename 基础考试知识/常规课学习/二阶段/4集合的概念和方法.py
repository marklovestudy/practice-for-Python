'''
一、集合的概念：
类型名称：set
定界符:{}
可变行：可变
有序性：无序
对元素类型与值的要求：可哈希
元素是否重复：不可以
元素查找速度：非常快
增删元素速度：快

集合属于 Python 无序可变序列，使用一对大括号作为定界符，元素之间使用逗号分隔，
同一个集合内的每个元素都是唯一的，元素之间不允许重复。
集合中只能包含数字、字符串、元组等不可变类型（可哈希）的数据，而不能包含列表、
字典、集合等可变类型数据。可以使用 set 函数将列表、元组，字符串、range对象
等其他可迭代对象转换为集合。如果原来的数据中存在重复元素，则在转化为集时只留一个；
如果原序列和迭代对象中有不可哈希的值，无法转换成集合，抛出异常。

二、创建方法：
    第一种方式：直接创建
    set1={1,2,3,4}
    第二种方式，函数创建
    set2=set('hello')
    第三种：推到导式创建
    set3={i for i in range(5)}

三、通用操作：

四、操作方法
1、add()在集合里添加元表  clear()清空集合  copy()复制
s = set("hello")
print(s)   #输出：{'h', 'l', 'e', 'o'}
s.add("ss")
s.add(1)
print(s)   #输出：{'h', 1, 'o', 'l', 'e', 'ss'}

2、clear()清空集合
s = set("hello")
s.clear()
print(s)

3、copy()复制
s = set("hello")
v = s.copy()
print(s)
print(v)

4、difference()二个集合不同的元素，属于s集体不属于a集合的元素组成的集合S-A，并赋值给V，输出：{'e', 'h', 'l'}
s = set("hello")
a = set("work")
v = s.difference(a)
print(s)
print(v)

5、difference_update()从此集合中删除另一个集合存在的元素，如下：从S中删除A集合中存在的元素。S-A，并赋值给S
s = set("hello")
a = set("oe")
v = s.difference_update(a)
print(s)    #{'l', 'h'}
print(v)    #None

6、discard()指定删除，如果没有不会报错。
s = set("hello")
v = s.discard("a")
print(s)    #{'l', 'h', 'o', 'e'}
print(v)    #None

7、intersection()求二个集合的交集，赋值给v = {'e', 'o'}
s = set("hello")
a = set("oeak")
v = s.intersection(a)
print(s)    #{'l', 'e', 'o', 'h'}
print(v)    #{'e', 'o'}

8、intersection_update()在S集合中找到S、a集合的交集，并赋值给S
s = set("hello")
a = set("oeak")
v = s.intersection_update(a)
print(s)    #{'o', 'e'}
print(v)    #None

9、isdisjoint()   s、a有交集返回False,无交集返回True
s = set("hello")
a = set("oeak")
v = s.isdisjoint(a)
print(s)    #{'o', 'h', 'l', 'e'}
print(v)    #False

10、issubset()  判断集合s是不是属于a,s属于a返回True,否则返回False.
s = set("hello")
a = set("helkscsdsdsdsao")
v = s.issubset(a)
print(s)    #{'l', 'o', 'e', 'h'}
print(v)    #True

11、issuperset()判断s是不是包含a，如果包含则返回True,否则返回False     超类，父类
s = set("hello")            #超集  set('ak') in 'mark'
a = set("he")
v = s.issuperset(a)
print(s)    #{'l', 'o', 'e', 'h'}
print(v)    #True

12、pop()随机删除
s = set("hello")
v = s.pop()
print(s)
print(v)

13、remove()指定删除，如果没有会报错。
s = set("hello")        #{'h','e', 'l', 'o'}
v = s.remove("h")       #可变的序列基本改变的是序列本身，不可变的序列基本产生的都是返回值
print(s)    #{'e', 'l', 'o'}
print(v)    #None

14、symmetric_difference()  返回s交a的补集，并赋值给v
s = set("hello")
a = set("hegk")
v = s.symmetric_difference(a)
print(s)    #{'o', 'h', 'l', 'e'}
print(v)    #{'o', 'g', 'k', 'l'}

15、symmetric_difference_update()  返回s交a的补集，并赋值给s
s = set("hello")
a = set("hegk")
v = s.symmetric_difference_update(a)
print(s)    #{'l', 'o', 'k', 'g'}
print(v)    #None

16、union()   求  s和a的并集，并赋值给v = s 并 a
s = set("hello")
a = set("heak")
v = s.union(a)
print(s)    #{'h', 'l', 'o', 'e'}
print(v)    #{'h', 'a', 'k', 'e', 'l', 'o'}

17、update()   求 s和a的并集，并赋值给s = s 并 a,也可以是把集合a的元素添加到s中
s = set("hello")
a = set("heak")
v = s.update(a)
print(s)    #{'h', 'o', 'k', 'a', 'e', 'l'}
print(v)    #None



内置函数len()、max()、min()、sum()、sorted()、map()、filter()、
enumerate()等也适合于集合
支持数学意义上的交集
#&:交集符,|并集符，^交补集符,-差集符 > >= < <=包含符可用

# add()
# clear()
# copy()
# discard()指定删除，如果没有不会报错。
# pop()随机删除
# remove()指定删除，如果没有会报错。  A{1,2,3,4,5} B{3,4,5,6,7}
# 差集2个           1.V=A-B={1,2}    2A=A-B={1,2}
# 交集2个           1.V=A&B={3,4,5}  2A=A&B={3,4,5}
# 判断3  有无交集，>=   <=   1 A&B=True,False   2A>=B   3A<=B
# 补集2个          注：全集{1,2,3,4,5,6,7}   A的补集{6，7}  B的补集{1,2}  A&B的补集{1,2,6,7}   1V=A^B  2A=A^B
# 并集2个          并集{1,2,3,4,5,6,7}       1.V=A|B   2.A=A|B

'''
# set1 = set(['mark','hy','tlx','czk','ggh'])
# print(set1)
# #set1.pop()    单行注释
# set1.remove('mark')
# v = set1.discard('hy')
# print(set1,v)
# #1add(),2clear(),3copy(),4discard(),remove()指定,5pop()随机
# import random as r
# set1 = set('')
# for i in range(50):
#     set1.add(r.randint(0,100))
# print(set1)
# set2 = set('')
# for i in range(50):
#     set2.add(r.randint(0,100))
# print(set2)
# #查看二个班中间相同的分数
# v = set1.intersection(set2)
# print(v)
'''
任务1：请创建集合{'元素4', '元素2', '元素7', '元素5', '元素8', '元素9', '元素6', '元素10', '元素1', '元素3'}
任务2：请用方法remove()删除元素2和元素6
任务3：请用方法pop()随机删除一个元素。
任务4，请用方法clear()清空集合
'''
# set1 = set('')
# #1,添加不同的十个元素
# for i in range(1,11):
#     set1.add('元素'
#
#
#              +str(i))
# print(set1)
# #2复制元素
# set2 = set1.copy()
# print(set2)
# #3用discard()删除指定元素’元素2‘,remove()删除指定'元素6'
# set1.discard('元素2')
# set1.remove('元素6')
# print(set1)
# #4用pop()随机删除一个元素
# set1.pop()
# print(set1)
# #5清空集合
# set1.clear()
# print(set1)

class1 = set()                                  #创建空的集合
while len(class1) <= 9:                         #循环直到大于5
    name = input('your name?')                  #输入
    if name in class1:                          #如果name在1班级中
        print('你已经报过名啦，耐心等待开学吧')
    else:
        print('欢迎报名，新的学期要好好学习哦!!')
        class1.add(name)                        #添加学生名字到班级这个集合中
    print(class1)
print('班级已经报满。。。')
while len(class1) > 5:
    student1=input('哪个学生不够聪明，然后我们需要给他留一级。')
    if student1 not in class1:
        print('这个班没有这个学生')
    else:
        class1.remove(student1)
        print('这个学生已经调走了。。')
    print(class1)
print('这个班的学生还有：',class1,'  他们都很优秀。')