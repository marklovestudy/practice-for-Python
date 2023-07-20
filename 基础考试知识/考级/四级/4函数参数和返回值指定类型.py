'''
函数的参数和返回值指定类型
    python是动态语言，新建变量时不需要声明与指定类型。
    自定义函数时也是如此。
    但是，在python3.5后，就新增了对函数参数和返回值的类型指定和检查，以及在新建变量时也可以指定类型。

基本类型指定
    例如，下面这个函数，指定了输入参数a为int类型，而b为str类型，并且返回值为str类型。
    可以看到，在方法中，最终返回了一个str。
    当我们在调用这个函数时，但如果参数a输入的是字符串，实际上运行不会报错，毕竟python的本质还是动态语言。

def f(a:int,b:str)->str:
    c = a * b
    print(c)
    return f
f(4,6)

def f(a:int,b:str)->str:
    print(a,b)
    return f
f('ok','okkk')

'''
def f(a:int,b:str)->str:
    print(a,b)
    return f
f('ok','okkk')


