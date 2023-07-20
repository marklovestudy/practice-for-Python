'''
1、abs()绝对值

2、divmod(x,y)         #主要用于内容可以是几页，分页功能,返回元组（x//y，x%y）
print(divmod(10,3))     #(3,1)      10除以3得3余1
返回元组（x//y，x%y）。不变量：div*y+mod=x。

3类型转换类：bool,ord,chr,set,enumerate,object.
# >>> bool([])    转换成布尔值
# False
#
# >>> ord('a')    输出编码编号
# 97

chr()根据值求出对应的字符，与ord()相反。

set()创建一个无序集合
&交集，|并集，-差集，^交补
a = set('hello')
b = set('ok')
print(a^b)

enumerate       #函数用于将一个可遍历的数据对象(如列表，元组或字符串)组合为一个索引序列，
                同时列出数据和数据下标，一般用在for循环当中。
l = [34,65,76,89]
for a,i in enumerate(l):
    print(a,i)

object
object类是python中所有类的基类，如果定义一个类时没有指定继承哪个类，则默认继承object类。
object没有定义__dict__，所以不能对object类实例对象尝试设置属性。
语法：
object()
参数介绍：无
返回值：返回一个新的无特征对象
'''
l = [34,65,76,89]
for a,i in enumerate(l):
    print(a,i)
