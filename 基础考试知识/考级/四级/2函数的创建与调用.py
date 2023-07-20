'''
函数的返回值
    1函数不是直接显示输出的，它会处理一些数据并返回一个或一组值。在函数中用return语句将值返回到调用函数的代码行，
    返回值能将程序大部分繁重的工作移交到函数中去完成，从而简化主程序。
    下面是一个简单的程序，接收姓氏和名称，返回完整的人名信息

def name(first_name,last_name):
    full_name = first_name + ' ' + last_name
    return full_name

print(name('zhang','san'))
输出：zhang san

    2函数可以返回任何类型的值，包括字典，列表这样较复杂的数据结构。还是上面的例子，返回一个表示人的字典：
def name(first_name,last_name):
    full_name = {'first_name':first_name,'last_name':last_name}
    return full_name
print(name('zhang','san'))
输出：{'first_name': 'zhang', 'last_name': 'san'}

    3函数传递列表，传递列表在函数中很有用，在列表中包含数字，名字甚至更复杂的对象，下面举一个例子：
def f(names):
    for i in names:
        print('hello'+' '+i+'!!')
f(['mark','weiwei','dafei'])
运形结果：
hello mark!!
hello weiwei!!
hello dafei!!

请创建一个n的阶乘的函数，并返回其结果：def an_n(n):
    a1=1
    for i in range(1,n+1):
        a1 *= i
    return a1
n = int(input('n=?'))
print('%s的阶乘是%s'%(n,an_n(n)))

练习题，请说出下列运形结果
def rt1(a=3):
    for n in range(a):
        for m in range(n+1):
            print('*',end='')
        print()
rt1()
rt1(5)

'''
def rt1(a=3):
    for n in range(a):
        for m in range(n+1):
            print('*',end='')
        print()

rt1()
rt1(5)