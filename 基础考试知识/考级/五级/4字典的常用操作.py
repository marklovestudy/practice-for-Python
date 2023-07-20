'''
字典的概念：
类型名称： dict 定界符：{}
可变性：可变
有序性：无序
对元素类型与值的要求：键值对
元素可否重复：键不可重复，值可重复元素查找速度：非常快
增删元素速度：快

字典的概念：
    字典是包含若干“键：值”元素的无序可变序列，字典中的每个元素包含用冒号分隔开的键和值两部分，
    表示一种映射或对应关系。定义字典时，每个元素的键和值之间用冒号汾隔，不同元素之间用逗号分
    隔，所有的元素放在一对大括号中。字典中元素的键可以是 Python 中任意不可变数据，例如整数、
    实数、复数、字符串、元组等类型，但不能使用列表、集合、字典或其他可变类型作为字典的键。
    另外，字典的键不允许重复。值是可以重复的。

字典的常用操作：
#>>> d={}
#>>> type(d)
<class 'dict'>

dict函数创建字典
方法1：
#>>> book = dict(title='P',a = 'mark',p = 59)
#>>> book
{'title': 'P', 'a': 'mark', 'p': 59}
方法2：
#>>> e = dict([(1,2),(3,4)])
#>>> e
{1: 2, 3: 4}
方法3：
keys = ['mark','weiwei','dafei']
#>>> ee = dict.fromkeys(keys)
#>>> ee
{'mark': None, 'weiwei': None, 'dafei': None}

字典的常用操作：
通过 key()．而非位正偏移（下抓泰引）访间数据
可包含任对象的无序合
可变长度、异质、可任意嵌套
属"可变映射"分美
对象引用表（ Hash Table )

字典的声明：
{}空字典表
{key:value}
dict ( key = value )
dict [( key . value),(key , value))
dict.fromkeys([key1,key2,...])

字典的访问：
dict[key]

键的测试
key in dict     返回True or False
dict[key]       如果key不存在报错
dict.get(key,'错了')   如果key不存在，不报错会返回指定值'错了'

dict.keys()返回一个键的可迭代的对象。可用for遍历
dict.values()返回一个值的可迭代的对象。可用for遍历
dict.items()返回一个键值对的可迭代的对象。可用for遍历

字典的方法：
1、clear()清空
msg = {2: 'abc', 'mark': 38, True: 123, (11, 22): 12}
v = msg.clear()
print(msg)              #{}

2、copy()复制
msg = {2: 'abc', 'mark': 38, True: 123, (11, 22): 12}
v = msg.copy()
print(v)                #{2: 'abc', 'mark': 38, True: 123, (11, 22): 12}

3、fromkeys()#根据序列，创建字典，并指定统一的值
v = dict.fromkeys(["kk1",123,999],123)
print(v)            #{'kk1': 123, 123: 123, 999: 123}

4、get()#获取指定键的值，如果指定的键不存在，就返回指定值，默认返回NONE
msg = {2: 'abc', 'mark': 38, True: 123, (11, 22): 12}
v1 = msg.get(2)
v2 = msg.get("kk11",2222)
print(v1,v2)        #abc 2222

5、items()#将字典转换成dict_items
msg = {2: 'abc', 'mark': 38, True: 123, (11, 22): 12}
v1 = msg.items()
print(v1)      #输出：dict_items([(2, 'abc'), ('mark', 38), (True, 123), ((11, 22), 12)])

6、keys()#将字典转换成dict_keys
msg = {2: 'abc', 'mark': 38, True: 123, (11, 22): 12}
v1 = msg.keys()
print(v1)       #输出：dict_keys([2, 'mark', True, (11, 22)])

7、values()#将字典转换成dict_values
msg = {2: 'abc', 'mark': 38, True: 123, (11, 22): 12}
v1 = msg.values()
print(v1)       #输出：dict_values(['abc', 38, 123, 12])

8、pop()移除指定的键-值对，如果键不存在，返回指定的值
msg = {2: 'abc', 'mark': 38, True: 123, (11, 22): 12}
v1 = msg.pop(2,90)#2键不存在的话就会返回90
print(msg)      #{'mark': 38, True: 123, (11, 22): 12}
print(v1)       #abc

9、popitem()#删除最后一对键-值对，并返回给k,v
msg = {2: 'abc', 'mark': 38, True: 123, (11, 22): 12}
k,v = msg.popitem()
print(k,v)      #(11, 22) 12

10、setdefault("k1","123")
设置"k1","123"键-值对：如果键存在，不设置，且返回原字典的对应键的值；如果不存在，则把键-值对添加进原字典。返回当前键对应的值
msg = {2: 'abc', 'mark': 38, True: 123, (11, 22): 12}
v = msg.setdefault("k1","123")
print(msg,v)        #{2: 'abc', 'mark': 38, True: 123, (11, 22): 12, 'k1': '123'} 123

11、update()更新。把新内容替换老内容。
msg = {"k1":"v1","k2":"v2"}
v1 = msg.update({"k1":"11111","k3":123})
print(msg)      #{'k1': '11111', 'k2': 'v2', 'k3': 123}
v2 = msg.update(k1=6,k2=5,k3="mark",k4="feifei")
print(msg)      #{'k1': 6, 'k2': 5, 'k3': 'mark', 'k4': 'feifei'}

12 del dict[key]        #删除字典的键值对

def speak():
    print('hello world')

def hit():
    print('I hit you')
a = {'mark':'write','weiwei':speak}
a.get('weiwei',hit)()
a.get('weiwi',hit)()

快速创建字典与字典推导式
>>> a = ['mark','wei','dafei']
>>> b = dict.fromkeys(a,1)
>>> b
{'mark': 1, 'wei': 1, 'dafei': 1}
>>> c = {i:3 for i in range(1,4)}
>>> c
{1: 3, 2: 3, 3: 3}
>>>
>>> x = ['a','b','c']
>>> y = ['A','B','C']
>>> {i:j for i,j in zip(x,y)}
{'a': 'A', 'b': 'B', 'c': 'C'}
'''
