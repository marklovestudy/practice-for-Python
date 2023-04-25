'''
使用'\b'匹配字符串的边界
    如果字符串在开始处、结尾处，或者是字符串的分界符为空格、
    标点符号以及换行，可以使用'\b'匹配字符串的边界，
代码如下：
import re
pattern=r'\bmr\b'       #r表示字符串中\不是转义符print(r'ok\nok')
match=re.search(pattern,'mr')   #成功，因为二边都是边界
print(match)
match=re.search(pattern,'mrsoft')   #失败，右边不是边界
print(match)
match=re.search(pattern,'mr soft')   #成功，因为二边都是边界
print(match)
match=re.search(pattern,'mr.soft')   #成功，因为二边都是边界
print(match)
'''

