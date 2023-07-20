'''
函数的全局变量和局部变量
    一般定义在程序的最开始的变量称为函数变量，在子程序中定义的变量称为局部变量，在子程序中定义
    的变量为局部变量，可以简单的理解为，无缩进的为全局变量，而局部变量的作用域是子程序内部，当
    程序运行时，首先会找程序内部有没有局部变量，如果有，则调用，如果没有，才会去调用全局变量。

例1：
name = 'mark'           #全局变量
def f():
    name = 'weiwei'     #局部变量
    print(name)
f()
运形结果是：
'weiwei'

例2：
name = 'mark'
def f():
    print(name)
f()
运形结果是：
'mark'

例3：
name = 'mark'               #全局变量
def f():
    global name             #把局部变量设为全局变量
    name = 'weiwei'
    print(name)
f()
print(name)                 #全局变量已被修改。
运形结果：
'weiwei'
'weiwei'

局部变量的作用域，只在局部有作用，如：
def f1():
    x=5
    y=6
    print(x+y)
def f2():
    y=1
    print(x+y)      #报错，不能引用f1()中的x
f1()
f2()

把局部变量变为全局变量后可以使用，例：注，要先局部变量变为全局变量写在顺序结构的前面。
def f1():
    global x
    x=5
    y=3
    print(x+y)
def f2():
    y=1
    print(x+y)      #报错，不能引用f1()中的x
f1()
f2()

global与nonlocal的区别：
    通过global,在定义局部变量的同时，也修改了全局变量的值。
    nonlocal关键字用来在函数或局部作用域使用外层(非全局)变量。表示整个函数内部的变量，

c= -2
def add():
    c = 1
    def f():
        print(c)
        def foo():
            nonlocal c
            c+=3
            print(c,c,c)
        return foo()
    return f
a = add()
a()
a()
a()
'''

c= -2
def add():
    c = 1
    def f():
        print(c)
        def foo():
            nonlocal c
            c+=3
            print(c,c,c)
            def kk():
                c = 6
                print(c)
            print(c)
            kk()
            print(c)
        return foo()
    return f
a = add()
a()

