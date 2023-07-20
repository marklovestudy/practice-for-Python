'''
序列操作类：all,any,filter,map,iter把序列变成迭代器

1,all()、any()
0、[]、None、False、""，，，0、0.0    None    空  为假
v=all([1,2,"1","a",""])
print(v)     #为假一个为假全为假。
v=all([" "])
print(v)        #为真，里面有一个空格也为真

2、any()           #一个为真全为真

3，filter(),函数用于过滤序列，过滤不符合条件的元素，返回一个迭代器对象，如果要转换成列表用list()转换
该函数接接收二个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回True
或False，最后将返回True的元素放到新列表中。
def jishu(n):
    return n%2 == 1

newlist = filter(jishu,[1,2,3,4,5,6,7,8,9,10])
n = list(newlist)
print(n)

map(func,iterable)

"""
1、map()函数x代表元素
num = [1,2,3,4,5,6,7,8]
dictnum = {"age":38,"name":"mark","job":"teacher"}
v = map(lambda x:x**2,num)
v1 = map(str,num)       #转字符串
print(list(v))

2、filter()函数x代表元素
num = [1,2,3,4,5,6,7,8]
names = ["s_mark","s_wei","s_dafei","xigua"]
dictnum = {"age":38,"name":"mark","job":"teacher"}
v = map(lambda x:x**2,num)
print(list(v))

v1 = map(lambda x:x.startswith("s"),names)
v2 = filter(lambda x:x.startswith("s"),names)       #True 保留，False删除
print(list(v1))
print(list(v2))

3、reduce(),x,y代表元素，一次赋二个值，x是S_an
from functools import reduce
num = [1,2,3,4,5,6,7,8]
v1 = reduce(lambda x,y:x+y,num,1)           #最后一个参数x:提供一个初始值x=1
v2 = reduce(lambda x,y:x*y,num,1)
print(v1,v2)

总结：map()得到一个可迭代对象,语法map(fuc,序列)
filter()遍历每个元素，判断元素法则后的布尔值，True保留，False删除，filter(fuc,序列)
reduce()先要载入库from functools import reduce，得到可迭代对象法则结果。
"""
#用map把[1,2,3,4,5],[6,7,8,9,10],合并成列表[7,9,11,13,15]
#用map把[1,2,3,4,5],[6,7,8,9,10],合并成列表[(1,6),(2,7),(3,8),(4,9),(5,10)]
v = map(lambda x,y:(x,y),[1,2,3],[4,5,6])
map(None,)
zip()
print(list(v))

v1=map(int,(1,2,3))
v2=map(int,'123')
print(list(v1))
print(list(v2))

help()
定义内置的“帮助”。
这是pydoc的包装。提供有用信息的帮助在Python交互提示下键入“help”时。
在Python提示符下调用help（）将启动交互式帮助会话。
调用help（thing）打印python对象“thing”的帮助。

dir()        #显示目录
v = dir(all)    #显示all所有的方法
print(v)

ascii()           #ascii() 函数类似 repr() 函数, 返回一个表示对象的字符串,
但是对于字符串中的非 ASCII 字符则返回通过 repr() 函数使用 \x, \u 或 \U 编码的字符。
生成字符串类似 Python2 版本中 repr() 函数的返回值。
ascii([1,2])
'[1, 2]'

ascii('械')
"'\\u68b0'"

vars(p_object=None)     函数返回对象object的属性和属性值的字典对象。返回对象object的属性和属性值的
                        字典对象，如果没有参数，就打印当前调用位置的属性和属性值。
vars（[object]）->dictionary没有参数，相当于locals（）。带有一个参数，相当于object__迪克特。
def mss():
    msg = "fdlsjafldjsl"
    print(locals())
    print(vars())
mss()
print(vars(int))
可以在交互式下观看
'''

v1=map(int,(1,2,3))
v2=map(int,'123')
print(list(v1))
print(list(v2))