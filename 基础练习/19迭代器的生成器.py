'''
1迭代器，只要遵守迭代协议就是可迭代对象。对象必须提供一个next方法，执行方法要么返回迭代中的下一项，要么就引起一个
Stoplterration异常，以终止迭代，只能往后走，不能往前走。
2可迭代对象：实现了迭代协议的对象（如何实现：对象内部定义一个__iter__(方法)）
3协议是一和约定，可迭代对象实现了迭代协议，python的内部工具（如FOR循环，sum,min,max函数等）使用迭代器协议访问对象
p = [1,2,3,4,5,6]
iter_1 = p.__iter__()       生成的结果就是一个迭代器
iter_1.__next__()       #next(iter_1)

生成器：可以理解为一种数据类型，这种数据类型自动实现了迭代器协议(其他的数据类型需要调用自己内置的__iter__方法)，
所以生成器就是可迭代对象。
1.生成器函数：常规函数定义，但是，使用yield语句而不是return语句返回结果。yield语句一次返回一个结果，在每个结果
中间，挂起函数的状态，以便下次从它离开的地方继续执行。
2.生成器表达式：类似于列表推导，但是生成器返回按需产生结果的一个对象，再不是一次构建一个结果列表

为何使用生成器对延迟操作提供了支持。所谓延迟操作，是指在需要的时候才产生结果，而不是产即产生结果。这也是生成器的主要好处。

生成器小结：
1，是可迭代对象
2.实现了延迟计算，省内存
3.生成器本质和其他的数据类型一样，都是实现了迭代器协议，只不过生成器附加了一个延迟计算省内存的好处，其余的可迭代对象可不有
这点好处。

def test():
    yield 1
    yield 2
v = test()
print(v)
print(v.__next__())
print(v.__next__())

#三元表达式
name = 'alex'
res = 'sb' if name == 'alex' else 'hansome'
print(res)

#列表解析
egg_list = []
for i in range(10):
    egg_list.append("egg_%s"%i)
print(egg_list)

egg_list_1 = ['egg_%s'%i for i in range(10) if i > 5]
print(egg_list_1)

egg_list_2 = ['egg_%s'%i for i in range(10)]        #列表解析
print(egg_list_2)

muji = ('egg_%s'%i for i in range(10))      #生成器表达式
print(muji.__next__())

print(sum(i for i in range(100000000)))     #省内存

#函数生存器的好处
import time
def born():
    print("borning now")
    print("borning now")
    yield 'yeye'
    time.sleep(3)
    print("borning now")
    yield 'baba'
    time.sleep(3)
    print("borning now")
    yield 'erzi'
    time.sleep(3)
    print("borning now")
    yield 'sz'

t = born()
print(t.__next__())
print(t.__next__())
print(t.__next__())

#函数包子生成器
def product_baozi():
    for i in range(100):
        yield '包子%s'%(i+1)


baozi_product = product_baozi()
print(baozi_product.__next__())

#母鸡下蛋
def product_eggs():
    for i in range(100):
        yield '鸡蛋%s'%(i+1)

egg_product = product_eggs()
for i in range(50):
    print(egg_product.__next__())

###生成器总结：
1语法上和函数类似，生成器函数和常规函数几乎是一样的，它们都是使用def语句定义，差别在于，生成器使用yield返回一个值，而函数用return

2自动实现迭代协议：对于生成器，python会自动实现迭代协议，以便应用到迭代背景中（如FOR循环，SUM函数）。由于生成器自动实现了迭代协议，
所以，我们可以调用它的next方法，并且，在没有值可以返回的时候，生成器自动产生Stoplteration异常。

3状态挂起，生成器使用yield语句返回一个值。yield语句挂起该生成器函数的状态，保留足够的信息，以便之后从它离开的地方继续执行。

优点：1生成器的好处是延迟计算，一次返回一个结果，也就是说，它不会一次生成所有的结果，这对于大数据处理，将会非常有用。
    2生成器还能有效提高代码可读性

def egg():
    print("first one")
    v1 = yield 1
    print("two",v1)
    v2 = yield 2
    print("three",v2)
    yield 3
    print("four")
    yield 4
    print("......")

e = egg()
e.__next__()
# e.send("hahaha")
v = next(e)
print(v)

#二线程吃包子
import time
def eat(name):
    print("%s开始吃包子了"%name)
    while True:
        time.sleep(1)
        baozi = yield
        print("%s吃掉了%s"%(name,baozi))

def product():
    n1 = eat("mark")
    n1.__next__()
    n2 = eat("mark")
    n2.__next__()
    for i in range(10):
        n1.send("肉包子%s" % (i + 1))
        n2.send("肉包子%s" % (i + 1))

product()

#多线程吃包子换着吃包子
import time
def eat(name):
    print("%s开始吃包子了"%name)
    while True:
        time.sleep(1)
        baozi = yield
        print("%s吃掉了%s"%(name,baozi))


def product(names,n,bz):
    for i in range(n):
        v = i
        v0 = int(len(names))
        while v >= v0:
            v -= int(len(names))
        n1 = eat(names[v])
        n1.__next__()
        n1.send(bz+"%s" % (i+1))


names1 = ['weiwei','dafei','mark','xigua']
product(names1,100,"肉包子")

生成器的值是生成的。而不固定存在的，所以t2为空。生成器只能便利一次
def test():
    for i in range(4):
        yield i             #__next()__碰到yield停上

t = test()
t1 = (i for i in t)
t2 = (i for i in t1)
print(list(t1))
print(list(t2))

生成器只能便利一次，所以t2为空
def test():
    for i in range(4):
        yield i

t = test()
t1 = (i for i in t)
t2 = (i for i in t)
print(list(t1))
print(list(t2))

def test():
    for i in range(4):
        yield i

t = test()
t1 = (i for i in t if i < 2)
t2 = (i for i in t if i >=2)
print(list(t1))     #[0, 1]
print(list(t))      #[]
print(list(t2))     #[]

计算总人口：
def p():
    with open('生成器.txt','r',encoding='utf-8') as f:
        for i in f:
            yield eval(i)
g=p()
all_p=sum([i['population'] for i in g])
print(all_p)

生产者消费模型：
1先生产完包子，再吃：
import time
def p_baozi(n):
    # return ['包子'+str(i) for i in range(n)]
    list1=[]
    for i in range(n):
        list1.append('包子'+str(i))
        time.sleep(1)
    return list1
def consumer(baoz):
    for index,baozi in enumerate(baoz):
        print('第%s个人，吃了%s'%(index,baozi))
res=p_baozi(10)
consumer(res)

2边生产包子，边吃：并发操作
import time
def p_baozi(n):
    for i in range(n):
        yield '包子'+str(i)
        time.sleep(1)
def consumer(baoz):
    for index,baozi in enumerate(baoz):
        print('第%s个人，吃了%s'%(index,baozi))

res=p_baozi(100)
consumer(res)

注：yield相当于return控制的是函数的返回值
#x=yield的另外一个特性，授受send传过来的值，赋值给x
#send接着向下走相当于yield，同时把上一个yield的值改变为传值send传值,
def p():
    print('start')
    first=yield
    print('one',first)
    yield 2
    print('two')
    yield 3
    print('3333')

res=p()
res.__next__()
v=res.send('666')
print(v)
res.__next__()

生产消费模型：
import time
def consumer(name):
    print('我是%s，我要开始吃包子了'%name)
    while True:
        time.sleep(1)
        baozi=yield
        print('我开始吃%s包子了'%baozi)
def producer(name,cai):
    c1=consumer(name)
    c1.__next__()
    for i in range(10):
        c1.send(cai+str(i))
producer('mark','肉')

'''
aa=[1,2,3]
bb=aa.copy()
def p():
    print(1,id(aa))
print(2,id(aa))
p()
print(3,id(bb))
name='fdsf543GFDGgfd443'
v=name.encode('utf-8')
print(v,type(v))