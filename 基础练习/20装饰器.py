"""
装饰器：本质就是函数，功能是为其他函数添加附加功能

原则：
1不修改被修饰函数的源代码
2不修改被修饰函数的调用方式

装饰器的知识储备

装饰器 = 高阶函数 + 函数嵌套 + 闭包
高阶函数的定义：1函数参数是一个函数名。2.函数返回值是一个函数名。3.满足以上一个条件为高阶函数

计算时间
高阶函数：实例1，实例2
实例1：参数是一个函数名，修改了函数的调用方式
import time
def foo():
    for i in range(1000):
        print("from foo")

def fank(func):
    starttime = time.time()
    func()
    stoptime = time.time()
    print("函数运行的时间是%s"%(stoptime-starttime))

fank(foo)

实例2，返回值为函数名，多运行了一次不合格。
import time
def foo():
    time.sleep(1)
    print("from foo")

#不修改foo源代码
#不修改foo调用方式

def fank(func):
    starttime = time.time()
    func()
    stoptime = time.time()
    print("函数运行的时间是%s"%(stoptime-starttime))
    return func

foo = fank(foo)
foo()

函数嵌套
def father():
    def son():
        def grandson():

装饰器的基本结构：**********
def foo():
    pass
def timmer(func):
    def wrapper():
        res = func()
        return res
    return wrapper
foo = timmer(foo)   #返回的wraper地址，把wraper的地址给foo
foo()               #执行wraper地址的函数

装饰器：实例1
import time
def foo():
    time.sleep(1)
    print("very good,from foo")
def timmer(func):
    def wrapper():
        star_time = time.time()
        func()
        stop_time = time.time()
        print("用时%s"%(stop_time-star_time))
    return wrapper

foo = timmer(foo)   #返回的wraper地址，把wraper的地址给foo
foo()

@timmer             #运行装饰器语法。要装饰谁就放在谁的前面

实例2：装饰器正确用法
import time
def timmer(func):
    def wrapper():
        star_time = time.time()
        res = func()
        stop_time = time.time()
        print("用时%s"%(stop_time-star_time))
    return res

@timmer
def foo():
    time.sleep(1)
    print("very good,from foo")

foo()

#时间装饰器：
import time
def timmer(func):
    def wrapper():
        star_time = time.time()
        res = func()
        stop_time = time.time()
        print("用时%s"%(stop_time-star_time))
        return res
    return wrapper

@timmer
def foo():
    time.sleep(1)
    print("very good,from foo")
    return 123

v = foo()
print(v)

有参数的装饰器：
import time
def tim(func):
    def wapper(*args,**kwargs):
        start = time.time()
        res = func(*args,**kwargs)
        endd = time.time()
        print('用时%s'%(endd-start))
        return res
    return wapper

@tim            #ak=tim(ak)
def ak(aa,bb):
    time.sleep(0.1)
    print(aa,bb)

ak(11333,22)

#验证装饰器
import time
def auth_func(func):
    def warpper(*args,**kwargs):
        username=input('your name').strip()
        password=input('password:').strip()
        if username == 'sb' and password == '123':
            v=func(*args,**kwargs)
            return v
        else:
            print('登陆失败，请重新登陆')
            return warpper()
    return warpper

@auth_func
def index():
    print('欢迎来到京东')

@auth_func
def home(name):
    print(name,'回来了')

@auth_func
def shopping_car(name):
    print(name,'车里有：',['水果','菜','肉'])

home('mark')

#优化，不用做复复登陆
import time
users_list=[
    {'username':'mark','password':'mark123'},
    {'username':'weiwei','password':'weiwei123'},
    {'username':'dafei','password':'dafei123'},
    {'username':'xigua','password':'xigua123'},
               ]
corrent_dic={'username':None,'login':False}

def auth_func(func):
    def warpper(*args,**kwargs):
        if corrent_dic['username'] and corrent_dic['login']:
            v=func(*args,**kwargs)
            return v
        username=input('your name').strip()
        password=input('password:').strip()
        for user_dic in users_list:
            if username == user_dic['username'] and password == user_dic['password']:
                corrent_dic['username']=username
                corrent_dic['login']=True
                v=func(*args,**kwargs)
                return v
        print('用户名和密码错误。。')
        warpper(*args,**kwargs)
    return warpper

@auth_func
def index():
    print('欢迎来到京东')

@auth_func
def home(name):
    print(name,'回来了')

@auth_func
def shopping_car(name):
    print(name,'车里有：',['水果','菜','肉'])

home('mark')

shopping_car('mark')

#参数传值
import time
users_list=[
    {'username':'mark','password':'mark123'},
    {'username':'weiwei','password':'weiwei123'},
    {'username':'dafei','password':'dafei123'},
    {'username':'xigua','password':'xigua123'},
               ]
corrent_dic={'username':None,'login':False}

def auth(auth_type='users.txt'):
    def auth_func(func):
        def warpper(*args,**kwargs):
            print('认证类型',auth_type)
            if corrent_dic['username'] and corrent_dic['login']:
                v=func(*args,**kwargs)
                return v
            username=input('your name').strip()
            password=input('password:').strip()
            f=open(auth_type,'r',encoding='utf-8')
            for user_dic in f:
                user_dic=eval(user_dic)
                if username == user_dic['username'] and password == user_dic['password']:
                    corrent_dic['username']=username
                    corrent_dic['login']=True
                    v=func(*args,**kwargs)
                    return v
            print('用户名和密码错误。。')
            warpper(*args,**kwargs)
        return warpper
    return auth_func
@auth(auth_type='users.txt')
def index():
    print('欢迎来到京东')

@auth(auth_type='users.txt')
def home(name):
    print(name,'回来了')

@auth(auth_type='users.txt')
def shopping_car(name):
    print(name,'车里有：',['水果','菜','肉'])

home('mark')

shopping_car('mark')
"""
import time
users_list=[
    {'username':'mark','password':'mark123'},
    {'username':'weiwei','password':'weiwei123'},
    {'username':'dafei','password':'dafei123'},
    {'username':'xigua','password':'xigua123'},
               ]
corrent_dic={'username':None,'login':False}

def auth(auth_type='users.txt'):
    def auth_func(func):
        def warpper(*args,**kwargs):
            print('认证类型',auth_type)
            if corrent_dic['username'] and corrent_dic['login']:
                v=func(*args,**kwargs)
                return v
            username=input('your name').strip()
            password=input('password:').strip()
            f=open(auth_type,'r',encoding='utf-8')
            for user_dic in f:
                user_dic=eval(user_dic)
                if username == user_dic['username'] and password == user_dic['password']:
                    corrent_dic['username']=username
                    corrent_dic['login']=True
                    v=func(*args,**kwargs)
                    return v
            print('用户名和密码错误。。')
            warpper(*args,**kwargs)
        return warpper
    return auth_func
@auth(auth_type='users.txt')
def index():
    print('欢迎来到京东')

@auth(auth_type='users.txt')
def home(name):
    print(name,'回来了')

@auth(auth_type='users.txt')
def shopping_car(name):
    print(name,'车里有：',['水果','菜','肉'])

home('mark')

shopping_car('mark')