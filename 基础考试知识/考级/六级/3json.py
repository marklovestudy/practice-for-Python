'''
概念：
    json 库主要包括两类，操作类函数和解析类函数，
    操作类函数主要完成外部 json 格式和程序内部数据类型之间的转换功能；
    解析类函数主要用于解析键值对内容。 json 格式包括对象和数组，用大括号{}和方括号［］表示，
    分别对应键值对的组合，关系和对等关系。使用json库时，需要注意 json 格式的“对象”和“数组”
    概念与 python 语言中的“字典”和“列表”的区别和联系，一般来说，json格式的对象将json库解析为字典。
    json格式的数组将被解析为列表。

    json库包含两个过程：编码和解码，编码是将 python 数据类型变换成json格式的过程，
    解码是从 json 格式中解析数据对应的 python 数据类型的过程。

    JSON ( JavaScript Object Notation )是一种轻量级的数据交换格式，易于人阅读和编写。
    使用 Python 语言来编码和解码 JSON 对象： JSON 函数：
    JSON函数：
    使用 JSON 函数需要导入 json 库： import json
    json.dumps 将 Python 对象编码成 JSON字符串
    json.loads 将已编码的 JSON 字符串解码为 Python 对象
    语法：
    json.dumps(obj,skipkeys = False , ensure_ascii = True , check_circular = True ,
    allow_nan = True , cls = None , indent = None , separators = None , encoding =" utf -8",
    default = None , sortkeys = False ,**kw)
    json.loads(s[,encoding[,cls[,object_hook[,parse_float[,parse_int[,parse_constant[,object_pairs_hook[,**kw]]]]]]]])
参数说明：
    1.obj:转化成json的对象。
    2.sort_keys =True:是告诉编码器按照字典排序(a到z)输出。如果是字典类型的python对象，就把关键字按照字典排序。
    3.indent:参数根据数据格式缩进显示，读起来更加清晰。
    4.separators:是分隔符的意思，参数意思分别为不同dict项之间的分隔符和dict项内key和value之间的分隔符，把：和，后面的空格都除去了。
import json
x = {'name':'你猜','age':19,'city':'四川'}
#用dumps将python编码成json字符串
y = json.dumps(x)
print(y)
i = json.dumps(x,separators=(',',':'))
print(i)
# 输出结果
{"name": "\u4f60\u731c", "age": 19, "city": "\u56db\u5ddd"}
{"name":"\u4f60\u731c","age":19,"city":"\u56db\u5ddd"}
    5.skipkeys：默认值是False，如果dict的keys内的数据不是python的基本类型(str,unicode,int,long,float,bool,None)，设置为False时，就会报TypeError的错误。此时设置成True，则会跳过这类key 。
    6.ensure_ascii=True：默认输出ASCLL码，如果把这个该成False,就可以输出中文。
    7.check_circular：如果check_circular为false，则跳过对容器类型的循环引用检查，循环引用将导致溢出错误(或更糟的情况)。
    8.allow_nan：如果allow_nan为假，则ValueError将序列化超出范围的浮点值(nan、inf、-inf)，严格遵守JSON规范，而不是使用JavaScript等价值(nan、Infinity、-Infinity)。
    9.default：default(obj)是一个函数，它应该返回一个可序列化的obj版本或引发类型错误。默认值只会引发类型错误。


例1：
import json
data = [{'a':1,'b':2,'c':3}]
data2 = json.dumps(data)
print(data2)

import json
jsondata = '{"a":1,"b":2,"c":3}'        #json的object类型转成dict
text = json.loads(jsondata)
print(text)

python原始类型向json类型转化对照表：
python                      json
dict                        object-str          py  {1:2,3:4}       js   " {1:2,3:4} "
list,tuple                  array-str       #排列，列阵，数组，阵列    py [1,2,3]   js "[1,2,3]"
str,unicode                 string-str
int,long,float              number-str
True                        true-str
False                       false-str
None                        null-str

例2
#存入
import json
numbers = [2,3,5,7,11,13]
filename = 'numbers.json'
with open(filename,'w') as f:
    json.dump(numbers,f)        #1把py数据转成js数据，并且写入f文件

#读取
import json
filename = 'numbers.json'
with open(filename,'r') as f:
    numbers = json.load(f)
print(numbers)

注：dumps(data)和dump(data,f)的区别
dumps(data)将PYTHON数据转化成json数据
dump(data,f)将PYTHON数据转化成json数据，并存入文件
loads(data)将json数据转化成PYTHON数据
load(f)从文件中取出数据，并将json数据转化成PYTHON数据，
'''
# import json
# dict1 = {"a":1,"b":2,"c":3}        #json的object类型转成dict
# v = json.dumps(dict1)           #把python数据dict1转变成json类型数据
# print(v,type(v))
# v1 = json.loads(v)              #把json类型的数据转变成python数据
# print(v1,type(v1))
# with open('aaa.json','w') as f:   #f=open('文件名','模式',编码)
#     json.dump(dict1,f)
# with open('aaa.json', 'r') as f:
#     v2=json.load(f)
#     print(v2,type(v2))
# import json
#
# a=[123,234,456]
# with open('aaa.json','w',encoding='utf-8') as f:
#     json.dump(a,f)
# with open('aaa.json','r',encoding='utf-8') as f:
#     v=json.load(f)
#     print(v,type(v))

# import json
# x = {'name':'你猜','age':19,'city':'四川'}
# #用dumps将python编码成json字符串
# y = json.dumps(x)
# print(y)
# i = json.dumps(x,ensure_ascii=False)
# print(i)

import json
numbers = [2,3,5,7,11,13]
#json.dumps 将 Python 对象编码成 JSON字符串
num_js=json.dumps(numbers)
print("这个是json数据")
print(num_js)
print(type(num_js))
num_py=json.loads(num_js)
print("这个是py数据")
print(num_py)
print(type(num_py))
