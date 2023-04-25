'''
3.2分割字符串
    split()方法用于实现根据正则表达式分割字符串，并以列表的形式返回。
    其语法如下:
re.split(pattern,string,[maxsplit],[flags])
    pattern 表示模式字符串，由要匹配的正则表达式转换而来。
    string  表示要匹配的字符串。
    maxsplit    可选参数，表示最大的拆分次数。
    flags:  可选参数，表示修饰符，用于控制匹配方式，如是否区分字母大小写。

实例：使用split()方法分割字符串
从给定的url中提取出请求地址和各个参数，代码如下：
import re
pattern=r'[?|&]'        #-到，|或，&与。
url='http://www.mingrisoft.com/login.jsp?username="mark"&pwd="mark123"'
result=re.split(pattern,url)
print(result)

实例：设定分割的次数
import re
pattern='\|'        #-到，|或，&与。\|表示为｜和\d，表示数字，\s表示为空格
url='fds|k756|cct|yhl|LUL|asss|sfd|667'
result=re.split(pattern,url,maxsplit=3)
print(result)
'''
