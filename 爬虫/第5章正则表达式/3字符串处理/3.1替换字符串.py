'''
3.1替换字符串
    sub()方法用于实现将某个字符串中所有匹配正则表达式的部分替换成其他字符串。其语法格式如下：
    re.sub(pattern,repl,string,count,flags)
    pattern 表示模式字符串，由要匹配的正则表达式转换而来。
    repl    表示替换的字符串。
    string  表示要被查找替换的原始字符串。
    count   可选参数，表示模式匹配后替换的最大次数，默认值为0，表示替换所有的匹配。
    flags   可选参数，表示修饰符，用于控制匹配方式，例如是否区分字母大小写。

实例：使用sub方法替换字符串
import re
pattern=r'1[34578]\d{9}'       #定义要替换的模式字符串  [34578]表示第二个数字为34578的，\d{9}表示后面的9个数字字符
string='中将号码为：84978981  联系电话为：13611111111'
result = re.sub(pattern,'1xxxxxxxxxx',string)
print(result)

实例：删除字符串中的数字
import re
pattern='[0-9]'       #删除字符串中的数字
string='中将号码为：84978981  联系电话为：13611111111'
result = re.sub(pattern,'',string)
print(result)

实例：删除字符串中的字母
import re
pattern='[a-z]'       #删除字符串中的数字
string='asdf998d9safd86786fdsa'
result = re.sub(pattern,'',string)
print(result)

实例：删除字符串中的字母
import re
pattern='[A-z]'       #删除字符串中的数字，按unicode编码排列。
string='asssdf998d9safd86786fAAAdsa'
result = re.sub(pattern,'',string)
print(result)

实例：删除字符串中的汉字
import re
pattern='[\u4e00-\u9fa5]'       #删除字符串中的字符，按unicode编码排列。
string='埼998d9safd86786fA堿sa'
result = re.sub(pattern,'',string)
print(result)

实例：替换为目标字符
import re
pattern='mark'       #删除字符串中的数字，按unicode编码排列。
string='hello,mark,你好，今天是一个欢乐的日子，你可以找个环境优美的地方和好朋友聚聚'
result = re.sub(pattern,'weiwei',string)
print(result)

import re
pattern='mark'       #删除字符串中的数字，按unicode编码排列。
string='hello,mark,你好，mark今天是一个欢乐的日子，你可以找个环境优美的地方和好朋友聚聚'
result = string.replace('mark','aa')
print(result)
'''
import re
pattern='mark'       #删除字符串中的数字，按unicode编码排列。
string='hello,mark,你好，mark今天是一个欢乐的日子，你可以找个环境优美的地方和好朋友聚聚'
result = re.subn(pattern,'weiwei',string)
print(result)
