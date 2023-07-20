'''
集合的概念：
类型名称：set
定界符:{}
可变行：可变
有序性：无序
对元素类型与值的要求：可哈希
元素是否重复：不可以
元素查找速度：非常快
增删元素速度：快

集合属于 Python 无序可变序列，使用一对大括号作为定界符，元素之间使用逗号分隔，
同一个集合内的每个元素都是唯一的，元素之间不允许重复。
集合中只能包含数字、字符串、元组等不可变类型（可哈希）的数据，而不能包含列表、
字典、集合等可变类型数据。可以使用 set 函数将列表、元组，字符串、range对象
等其他可迭代对象转换为集合。如果原来的数据中存在重复元素，则在转化为集时只留一个；
如果原序列和迭代对象中有不可哈希的值，无法转换成集合，抛出异常。

1将range对象转集合。
>>> set(range(3))
{0, 1, 2}
2集合推导式
>>> {i for i in range(5)}
{0, 1, 2, 3, 4}

1、add()在集合里添加元表
s = set("hello")
print(s)   #输出：{'h', 'l', 'e', 'o'}
s.add("ss")
s.add(1)
print(s)   #输出：{'h', 1, 'o', 'l', 'e', 'ss'}

2、clear()清空集合
s = set("hello")
s.clear()
print(s)

3、copy()复制
s = set("hello")
v = s.copy()
print(s)
print(v)

4、difference()二个集合不同的元素，属于s集体不属于a集合的元素组成的集合S-A，并赋值给V，输出：{'e', 'h', 'l'}
s = set("hello")
a = set("work")
v = s.difference(a)
print(s)
print(v)

5、difference_update()从此集合中删除另一个集合存在的元素，如下：从S中删除A集合中存在的元素。S-A，并赋值给S
s = set("hello")
a = set("oe")
v = s.difference_update(a)
print(s)    #{'l', 'h'}
print(v)    #None

6、discard()指定删除，如果没有不会报错。
s = set("hello")
v = s.discard("a")
print(s)    #{'l', 'h', 'o', 'e'}
print(v)    #None

7、intersection()求二个集合的交集，赋值给v = {'e', 'o'}
s = set("hello")
a = set("oeak")
v = s.intersection(a)
print(s)    #{'l', 'e', 'o', 'h'}
print(v)    #{'e', 'o'}

8、intersection_update()在S集合中找到S、a集合的交集，并赋值给S
s = set("hello")
a = set("oeak")
v = s.intersection_update(a)
print(s)    #{'o', 'e'}
print(v)    #None

9、isdisjoint()   s、a有交集返回False,无交集返回True
s = set("hello")
a = set("oeak")
v = s.isdisjoint(a)
print(s)    #{'o', 'h', 'l', 'e'}
print(v)    #False

10、issubset()  判断集合s是不是属于a,s属于a返回True,否则返回False.
s = set("hello")
a = set("helkscsdsdsdsao")
v = s.issubset(a)
print(s)    #{'l', 'o', 'e', 'h'}
print(v)    #True

11、issuperset()判断s是不是包含a，如果包含则返回True,否则返回False
s = set("hello")
a = set("he")
v = s.issuperset(a)
print(s)    #{'l', 'o', 'e', 'h'}
print(v)    #True

12、pop()随机删除
s = set("hello")
v = s.pop()
print(s)
print(v)

13、remove()指定删除，如果没有会报错。
s = set("hello")
v = s.remove("h")
print(s)    #{'e', 'l', 'o'}
print(v)    #None

14、symmetric_difference()  返回s交a的补集，并赋值给v
s = set("hello")
a = set("hegk")
v = s.symmetric_difference(a)
print(s)    #{'o', 'h', 'l', 'e'}
print(v)    #{'o', 'g', 'k', 'l'}

15、symmetric_difference_update()  返回s交a的补集，并赋值给s
s = set("hello")
a = set("hegk")
v = s.symmetric_difference_update(a)
print(s)    #{'l', 'o', 'k', 'g'}
print(v)    #None

16、union()   求  s和a的并集，并赋值给v = s 并 a
s = set("hello")
a = set("heak")
v = s.union(a)
print(s)    #{'h', 'l', 'o', 'e'}
print(v)    #{'h', 'a', 'k', 'e', 'l', 'o'}

17、update()   求 s和a的并集，并赋值给s = s 并 a,也可以是把集合a的元素添加到s中
s = set("hello")
a = set("heak")
v = s.update(a)
print(s)    #{'h', 'o', 'k', 'a', 'e', 'l'}
print(v)    #None



内置函数len()、max()、min()、sum()、sorted()、map()、filter()、
enumerate()等也适合于集合
支持数学意义上的交集
#&:交集符,|并集符，^交补集符,-差集符 > >= < <=包含符可用

'''