'''
2.3非贪婪匹配
使用".*?"实现非贪婪匹配字符串
在上一节我们学习了贪婪匹配，使用起来非常的方便，不过在某些情况下，贪婪匹配并不会匹配我们所需要的结果。
以获取网址'https://www.hao123.com/'中的123为例
import re
pattern='https://.*(\d+).com'
match=re.findall(pattern,'https://www.hao123.com/')
print(match)
从上面的结果看出，'(\d+)'并没有匹配123，只匹配了一个'3'，这是因为.*会尽可能的多匹配字符，
而'\d+'则尽量少匹配字符，所以.*匹配了：'www.hao12',而只留了一个'3'给\d+匹配。
为了解决这个问题我们要让'.*'尽量少匹配，所以用'.*?'非贪婪匹配。
import re
pattern='https://.*?(\d+).com'
match=re.findall(pattern,'https://www.hao123.com/')
print(match)
因为'.*?'尽量少匹配的特性，如果用在尾部时，可能什么也匹配不到。
import re
pattern='https://(.*?)'
match=re.findall(pattern,'https://www.hao123.com/')
print(match)


import re
pattern='https://(.*)'
match=re.findall(pattern,'https://www.hao123.com/')
print(match)
'''

