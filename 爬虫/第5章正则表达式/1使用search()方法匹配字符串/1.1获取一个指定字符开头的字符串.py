'''
    re模块中的search()方法用于整个字符串中搜索第一个匹配的值，如果在第一个匹配的位置匹配成功，
    则返回Match对象，否则返回None。其语法格式如下：
    re.search(pattern,string,[flags])
    pattern:    表示模式字符串，由要匹配的正则表达式转换而来。
    string:     表示要匹配的字符串。
    flags：可选参数，表示修饰符，用于控制匹配方式，如是否区分字母大小写。

1.1获取一个指定字符开头的字符串。
实例：搜索第一个“mr_”开头的字符串。
import re
pattern="mr_\w+"            #模式字符串
string="MR_SHOP mr_shop"    #要匹配的字符串
match1=re.search(pattern,string)        #搜索字符串，区分大小写
match2=re.search(pattern,string,re.I)   #搜索字符串，不区分大小写
print(match1)
print(match2)

string="项目名称MR_SHOP mr_shop"    #要匹配的字符串
match3=re.search(pattern,string)        #搜索字符串，区分大小写
match4=re.search(pattern,string,re.I)   #搜索字符串，不区分大小写
print(match3)
print(match4)
#说明search方法可以在字符串首和中的位置都可以。
'''
