'''
findall()方法用于整个字符串中搜索所有符合正则表达式的字符串，并以列表的形式返回。
如果匹配成功，则返回包含匹配结构的列表，否则返回空列表。其语法格式如下：
re.findall(pattern,string,[flags])
参数说明如下：
    pattern:    表示模式字符串，由正则表达式转换而来。
    string:     表示要匹配的字符串。
    flags:      可选参数，用来控制匹配方式，如是否区分字母大小写。
2.1匹配所有指定字符开头的字符串
搜索开头为'mr_'开头的所有字符串
import re
pattern='mr_\w+'
string='MR_SHOP mr_shopf32ds mr_ss22s'
match=re.findall(pattern,string,re.I)
print(match)
'''
import re
pattern='mr_(\w+)'      #区分打括号和不打括号的区别
string='MR_SHOP mr_shopf32ds mr_ss22s'
match=re.findall(pattern,string,re.I)
print(match)