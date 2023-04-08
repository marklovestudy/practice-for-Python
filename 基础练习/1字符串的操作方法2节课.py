'''
一、元组的概念：
类型名称：str
定界符:''等
可变行：不可变
有序性：有序

二、创建方法：
name='mark'
str1=str(123)
str2=str([1,2,3])

三、访问：
    索引访问：
    str1='abcdefghijklmn'
    print(str1[0])
    print(str1[2:4])
    print(str1[1:8:3])

四、通用操作：
1判断元素是否在序列之内：in,not in.
                2连接序列：list1+list2
                3重复序列元素：list1*n
                4索引访问：s[i]，s[i:j],s[i:j:k]
                5获取序列属性：长度len(s),最小值min(s),最大值max(s),和sum(s)
                6检索某个元素第一次出现的元素下标s.index('x')
                7检索某个元素出现的次数s.count('x')
五、方法。
1、capitalize(self, *args, **kwargs)首字母大写        6分
name = "mark"
v = name.capitalize()#1、capitalize(self, *args, **kwargs)首字母大写
print(v)   #输出：Mark

2、casefold(self, *args, **kwargs)所有大写转小写，包含别国语言     3分
name = "mArk"
v = name.casefold()#2、casefold(self, *args, **kwargs)所有大写转小写，包含别国语言
print(v)   #输出：mark

3-6、center()、ljust()、rjust()、zfill()            6分
name = "mark"
v1 = name.center(20,"_")#3、center(self, *args, **kwargs)，center(宽度，“一个字符，可有可无”),字放在中间
v2 = name.ljust(20,"_")#同上，字放在左边
v3 = name.rjust(20,"_")#同上，字放在右边
v4 = name.zfill(20)#同上，字放在右边，只不过只能用0填充
print(v1,v2,v3,v4)   #输出：_________mark________ mark________________ ________________mark 0000000000000000mark

7、count()                                       8分
name = "markmarkmark"
v = name.count("ar",0,8)#4、count(self, sub, start=None, end=None)    count("字符"，起始位，结束位)
print(v)   #输出：2

8-9
#encode(self, *args, **kwargs)5、
#decode()6、

10-11、endswith()、startswith()           7分
name = "markmarkmark"
v1 = name.endswith("ar",0,8)#7、endswith(self, suffix, start=None, end=None)是否以“ar”结束。
print(v1)       #输出：False
v2 = name.startswith("ma",0,8)#8、startswith(self, prefix, start=None, end=None)是否以“ma”开始
print(v2)       #输出：True

12、expandtabs()                     3分
name = "mark\tmar\tkmark"
v = name.expandtabs(10)#9、用着制表符的宽度设定
print(v)        #mark      mar       kmark即：mark后面补6个空位，mar后补7个空位。
test = "name\tjob\tage\nweiwei\tteacher\t28\ndafei\tteacher\t32\nmark\tteacher\t38"
v = test.expandtabs(20)
print(v)

13、find(),rfind()                   6分
name = "markmarkmark"
v = name.find("ar",0,8)# 10、find(self, sub, start=None, end=None) 找到返回最低位，没找到返回-1
print(v)        #输出：1
test = "markmarkmark"
v = test.rfind("r")#找到返回最高位，没找到返回-1
print(v)        #输出：10

14、format()                         9-10分
test = "i am {name}"
v = test.format(name = "mark")#11、format(self, *args, **kwargs)#格式化，将字符串中的占位符转换成指定值
print(v)        #输出:i am mark   将｛name｝转换成"mark"

test = "i am {0},age {1}"
v = test.format("mark",29)#format(self, *args, **kwargs)#格式化，将字符串中的占位符转换成指定值
print(v)        #输出:i am mark age 29   将｛name｝转换成"mark"  age转换成29

test = "i am {name},age {age}"
v = test.format(**{"name":"mark","age":38})#传递字典的键-值对前面加**
print(v)        #输出:i am mark age 38   将｛name｝转换成"mark"  age转换成38

15、format_map(self, mapping)            3分
test = "i am {name},age {a}"
v = test.format_map({"name":"markmark","a":"38"})#12、format_map(self, mapping)#格式化，将字符串中的占位符转换成指定值
print(v)        #输出:i am markmark,age 38   将｛name｝转换成"mark"  {a}转换成38传递字典的键所对应的值。

16、index()                              8分    索引
name = "markmarkmark"
v = name.index("ar")# 13、index(self, sub, start=None, end=None)找到“ar”,返回"ar"的位置,如果找不到就报错。
print(v)        #输出：1   在1号位置找到了“ar”

17、isalnum()                3
test = "usa890_"
v = test.isalnum()#14、判断test字符串是不是全是数字或字母,如果是返加True,否则返回False.
print(v)        #输出：False因为不是纯数字或字母

18、isalpha()                3
test = "我"
v = test.isalpha()#15、是否全是字母或汉字  是返加True     否则False
print(v)        #输出：True

19、isdecimal()              3
test = "123"
v1 = test.isdecimal()#16、是否是数字   如果字符串中的所有字符都是十进制字符并且至少有一个字符，则返回 True，否则返回 False。
# 十进制字符是可以用来组成以 10 为基数的数字的字符，例如 U+0660：阿拉伯-印度数字零。
# 形式上，十进制字符是 Unicode 通用类别 ·nd· 中的字符。
# isdecimal()
#True：Unicode 数字，全角数字（双字节）
#False：小数，罗马数字，汉字数字
#Error：byte 数字（半角、单字节）

20、isdigit()                3
v2 = test.isdigit()#17、是否是数字     如果字符串中的所有字符都是数字并且至少有一个字符，则返回 True，否则返回 False。
# 数字包括十进制字符和需要特殊处理的数字，如兼容性上标数字。
# 这包括不能用于以 10 为基数构成数字的数字，如 Kharosthi 数字。
# 从形式上讲，数字是一个具有属性值 numeric_type=digit 或 numeric_type=decimal 的字符。
#isdigit()
#True：Unicode 数字，全角数字（双字节），byte 数字（半角、单字节）
#False：小数，罗马数字，汉字数字
#Error：无

21、isnumeric()                  3
v3 = test.isnumeric()#18、是否是数字     如果字符串中的所有字符都是数字字符，并且至少有一个字符，则返回 True，否则返回 False。
# 数字字符除了包括数字字符，还有具有 Unicode 数值属性的所有字符，例如 U+2155：VULGAR FRACTION ONE FIFTH。
# 从形式上讲，数字字符是具有属性值 numeric_type=digit、numeric_type=decimal 或 numeric_type=numeric 的字符。
#True：Unicode 数字，全角数字（双字节），罗马数字，汉字数字
#False：小数
#Error：byte 数字（半角、单字节）
print(v1,v2,v3)        #输出：True  True  True

#isascii

22、isprintable()                3分
test = "oiua\tsdfkj"
v = test.isprintable()#19、是否有转义符之类的。如果有False,没有返回True
print(v)        #输出：False因为有转义符\t

23、isspace()                    2分
test = " a k"
v = test.isspace()#20、判断是否全是空格，全是空格True    没有空格，或没有全是空格返回False
print(v)        #输出：False因为不全是空格

24-25title()、istitle()
test = "Return True is all cased"
v1 = test.title()#21、转标题
v2 = test.istitle()#22、判断是否为标题,首字母是不是大写，如果是返回True  否则False
print(v1,v2)         #Return True Is All Cased      False

26、join()                       10分
test = "mark"
t = "_"
v = t.join(test)#23、把字符串t插入到test字符串中的每个字符之间。注：把t插入到序列test的元素间，变成一个字符串
print(v)        #输出：m_a_r_k

27-30islower()、lower()、isupper()、upper()                6分
test = "Mark"#27-30
v1 = test.islower()#是否是全小写，是返回True,否返回False
v2 = test.lower()#转小写
v3 = test.isupper()#是否是全大写，是返回True,否返回False
v4 = test.upper()#转大写
print(v1,v2,v3,v4)      #输出：False mark False MARK

31、swapcase()
test = "mark"
v = test.swapcase()#大小写转换
print(v)      #输出：MARK

32-34、lstrip()、strip()、rstrip()
test = "   mark   "
v1 = test.lstrip()#去左边空格和\t,\n
v2 = test.strip()#去所有空格和\t,\n
v3 = test.rstrip()#去右边空格和\t,\n
print(v1,v2,v3)

test = "market"
v1 = test.lstrip("ma")
v2 = test.strip("mark")
v3 = test.rstrip("43k53e53tar")#移除指定的字符，有限量最多匹配
print(v1,v2,v3)     #输出：rket et m

35-36、maketrans()、translate()
test = "abcdef"
test1 = "123456"
v = "fdsafdbadadbccsaf"
m = str.maketrans(test,test1)#34、创建一个名为m的对应关系。
new_v = v.translate(m)#35、把v这个字符串以对应关系m的形式翻译，translate（）
print(new_v)        #输出：64s16421414233s16

37-41、partition()、rpartition()、split()、splitlines()、rsplit()
test = "testasdsddfg"
v = test.partition("s")#36、以“s”开分，分成三份的元表，但最多只能是三份。包含分割字符
print(v)    #输出：('te', 's', 'tasdsddfg')
test = "testasdsddfg"
v = test.rpartition("s")#37、以“s”开分，分成三份的元表，但最多只能是三份。从右往左分，包含分割字符
print(v)        #输出：('testasd', 's', 'ddfg')
test = "testasdsddfg"
v = test.split("s")#38、以空格为分割符，把test字符串分割成若干个元素的列表。如有参数，则以参数为分割点分割，参数消失。不包含侵害字符
print(v)        #输出：['te', 'ta', 'd', 'ddfg']
正则表达式
是否想要保留分割的元素
test = "fdafdsaf\nfdsfggdf\ngdfsdfds"
v = test.splitlines(True)       #39、以换行符为分割符，分割成列表。True：保留分割符，False:不保留侵害符
print(v)         #输出：['fdafdsaf\n', 'fdsfggdf\n', 'gdfsdfds']
test = "testasdsddfg"
v = test.rsplit("s")#38、以空格为分割符，把test字符串从右到左分割成若干个元素的列表。如有参数，则以参数为分割点分割，参数消失。不包含侵害字符
print(v)        #输出：['te', 'ta', 'd', 'ddfg']

42、isidentifier()           2
test = "def_11"
v = test.isidentifier()#判断是否符合变量的规则，符合返回True,否则返回False
print(v)        #输出：True

43、len()                    10分
test = "deffff"
v = len(test)#计算test的长度
print(v)    #输出：6

44、replace()                     7分2-4
test = "markmarkmark"
v = test.replace("a","bbbb")#把“a”替换成“bbbb”，只替换第一个a
print(v)        #输出：mbbbbrkmarkmark

n = "makr"
n.swapcase()#选中等待，待出现str，点右下角三点，选择编辑源F4,进入builtins.py
'''

#
# str1 = 'fdsafdsafd的世界安抚魂牵梦萦哽32132133324......91847832,'
# num_int = 0
# num_str = 0
# num_other = 0
# for i in str1:
#     if i.isdigit():         #判断是否为数字
#         num_str += 1
#     elif i.isalpha():       #判断是否为字母或汉字
#         num_int += 1
#     else:
#         num_other += 1      #其它
# print('数字有：',num_int)
# print('字母和汉字',num_str)
# print('其它：',num_other)
# 编写一个重复执行的程序，要求用户输入一个字符串。
# 如果输入的字符串的长度是奇数，就输出字符串最中间的字符。
# 如果字符串的长度是偶数，就输出字符串的最后一个字符。然后重复以上操作。
# while 1:
#     str1=input("请输入一个字符串")        #input输入一个字符串
#     n=len(str1)                     #len计算长度
#     #判断
#     if n%2==1:                         #是奇数
#         print(str1[n//2])                         #输出中间的字符
#     else:
#         print(str1[-1])                         #输出最后一个字符

#str1=input("请输入一个字符串：")
# list1=list(str1[1::2])
# print(list1)
# list1=[]        #'abcdef'[1::2]----'bdf'
# for i in str1[1::2]:        #for i in 序列
#     list1.append(i)
# print(list1)
# while 1:
#     print([i for i in input("请输入一个字符串：")[1::2]])

