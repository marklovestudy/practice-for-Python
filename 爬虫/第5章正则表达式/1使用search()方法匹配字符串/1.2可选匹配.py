'''
1.2可选匹配
    使用"?"实现可选匹配字符串中的内容
    在匹配字符时，有时会遇到部分内容可有可无的情况，对于这样的情况可以使用"?"来解决。
    ”？“可以理解为可选符号，通过该符号即可实现可选匹配字符串中的内容。
实例代码如下：
import re
#表达式，(\d?)+表示多个数字可有可无       无+号表示单个,单个时可以无括号
#       (\w?)+表示多个字符可有可无
#       (\s)+表示多个字符可有可无
#       ([\u4e00-\u9fa5]?)+多个汉字可有可无
pattern="(\d?)+mrsoft(\s?)+([\u4e00-\u9fa5]?)+"
match1=re.search(pattern,'1111mrsoft')
print(match1)
match2=re.search(pattern,'mrsoft')
print(match2)
match3=re.search(pattern,'mrsoft   ')
print(match3)
match4=re.search(pattern,'mrsoft 第一')
print(match4)
match5=re.search(pattern,'rsoft 第一')    #匹配失败，因为字符串'rsoft 第一'中没有一个完整的‘mrsoft’
print(match5)
'''
import re
#表达式，(\d?)+表示多个数字可有可无       无+号表示单个,单个时可以无括号
#       (\w?)+表示多个字符可有可无
#       (\s)+表示多个字符可有可无
#       ([\u4e00-\u9fa5]?)+多个汉字可有可无
pattern="(\d?)+mrsoft(\s?)+([\u4e00-\u9fa5]?)+"
match1=re.search(pattern,'1111mrsoft')
print(match1)
match2=re.search(pattern,'mrsoft')
print(match2)
match3=re.search(pattern,'mrsoft   ')
print(match3)
match4=re.search(pattern,'mrsoft 第一')
print(match4)
match5=re.search(pattern,'rsoft 第一')    #匹配失败，因为字符串'rsoft 第一'中没有一个完整的‘mrsoft’
print(match5)