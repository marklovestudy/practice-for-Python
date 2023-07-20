'''
一、字典的概念：
类型名称： dict 定界符：{}
可变性：可变
有序性：无序
对元素类型与值的要求：键值对
元素可否重复：键不可重复，值可重复元素查找速度：非常快
增删元素速度：快

字典的概念：
    字典是包含若干“键：值”元素的无序可变序列，字典中的每个元素包含用冒号分隔开的键和值两部分，
    表示一种映射或对应关系。定义字典时，每个元素的键和值之间用冒号分隔，不同元素之间用逗号分
    隔，所有的元素放在一对大括号中。字典中元素的键可以是 Python 中任意不可变数据，例如整数、
    实数、复数、字符串、元组等类型，但不能使用列表、集合、字典或其他可变类型作为字典的键。
    另外，字典的键不允许重复。值是可以重复的。

二、创建方式：
第一种方式：直接创建
dict1={'name':'mark','age':30}
第二种方式：dict创建
dict1=dict([('aa','bb'),('cc','dd')])
dict2=dict(key=value)
第三种方式：推导式  key value
{k:v for i in range(10)}
{i:j for i,j in zip(range(10),range(3,13))}
第四种方式：方法创建fromkeys()，
dict.fromkeys(["kk1",123,999],123)
zip的作用：1把二个序列组合到一起，变成一个序列，对应索引号不发生改变。
          2元素的数量以序列数少的为准

三、访问字典：
    msg = {2: 'abc', 'mark': 38, True: 123, (11, 22): 12}
    v1 = msg.get(2)         #get()方法访问
    print(msg[2])           #键访问
    msg[2]='ok'             #修改字典值

四、字典的方法：
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

import random as r
import time
monster = ['骷髅兵','僵尸','异形','精英骷髅兵','精英僵尸','精英异形','boss']            #怪物类型
creat_monster=(r.choice(monster) for i in range(100))
player_attribute={'name':'haha','f':10,'blood':100,'g':[5,10],'zb':'小刀'}
ck= {'小刀':0,'金币':0,'极品小红刀':0,'屠龙刀':0}
for i in range(100):
    v = creat_monster.__next__()
    if v in ['骷髅兵','僵尸','异形']:

        v_attribute = {'name':v,'f':5,'blood':100,'g':5,'zb':['小刀','金币100']}
        while v_attribute['blood'] > 0:
            print('%s攻击了%s'%(player_attribute['name'],v_attribute['name']))
            v_attribute['blood'] -= r.randint(player_attribute['g'][0],player_attribute['g'][1])
            print(v_attribute)
            time.sleep(0)
        zb = v_attribute['zb'][r.randint(0,1)]
        if zb == '小刀':
            ck['小刀']+=1
        elif zb == '金币100':
            ck['金币'] += 100
    elif v in ['精英骷髅兵','精英僵尸','精英异形']:
        v_attribute = {'name':v,'f':5,'blood':1000,'g':15,'zb':['极品小红刀','金币1000']}
        while v_attribute['blood'] > 0:
            print('%s攻击了%s'%(player_attribute['name'],v_attribute['name']))
            v_attribute['blood'] -= r.randint(player_attribute['g'][0],player_attribute['g'][1])
            print(v_attribute)
            time.sleep(0)
        zb = v_attribute['zb'][r.randint(0,1)]
        if zb == '极品小红刀':
            ck['极品小红刀']+=1
        elif zb == '金币1000':
            ck['金币'] += 1000
    else:
        v_attribute = {'name': v, 'f': 15, 'blood': 10000, 'g': 25, 'zb': ['屠龙刀', '金币10000']}
        while v_attribute['blood'] > 0:
            print('%s攻击了%s' % (player_attribute['name'], v_attribute['name']))
            v_attribute['blood'] -= r.randint(player_attribute['g'][0], player_attribute['g'][1])
            print(v_attribute)
            time.sleep(0)
        zb = v_attribute['zb'][r.randint(0, 1)]
        if zb == '屠龙刀':
            ck['屠龙刀'] += 1
        elif zb == '金币10000':
            ck['金币'] += 10000
    print(ck)
'''
import random as r
import time
monster = ['骷髅兵','僵尸','异形','精英骷髅兵','精英僵尸','精英异形']            #怪物类型
mob_list=[]
for i in range(10):
    name = r.choice(monster)
    if name in ['骷髅兵','僵尸','异形']:
        mob = {'gw': '骷髅', 'blood': 100}
        mob['gw']= name
        mob_list.append(mob)
    elif name in ['精英骷髅兵','精英僵尸','精英异形']:
        mob = {'gw': '骷髅', 'blood': 100}
        mob['gw'] = name
        mob['blood'] = 1000
        mob_list.append(mob)
while True:
    time.sleep(1)
    j=-1
    if len(mob_list) > 0:
        for i in range(len(mob_list)):
            print('当前怪物是：%s,当前怪物血量是：%s'%(mob_list[i]['gw'],mob_list[i]['blood']))
            s = r.randint(0,10)
            print('你攻击了%s怪，怪物失去生命%s'%(mob_list[i]['gw'],s))
            mob_list[i]['blood'] -= s
            if mob_list[i]['blood'] <= 0:
                j = i
        if j !=-1:
            mob_list.pop(j)
        print(mob_list)
    else:
        print('你已经杀完了所有的怪')
        break
