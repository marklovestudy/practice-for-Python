'''
使用".*"实现贪婪匹配字符串
'.*'是一种万能匹配方式，其中'.'可以匹配除换行符以外的任意字符，
而'*'表示匹配前面字符0次或无限次，当在一起时就成了万能匹配方式。
以网络地址的中间部分为例，代码如下：
import re
pattern = 'https://.*/'        #.*尽可能的多匹配，.*?尽可能的少匹配
match=re.findall(pattern,'https://www.hao123.com/')
print(match)

import re
pattern = 'https://(.*)/'        #.*尽可能的多匹配，.*?尽可能的少匹配,()表示只保留()中的字符
match=re.findall(pattern,'https://www.hao123.com/')
print(match)
'''
import requests
import re
# url='https://www.baidu.com/'
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
# response=requests.get(url,headers=headers).text
# print(response)
# with open('ht.txt','w',encoding='utf-8') as f:
#     f.write(response)

f=open('ht.txt','r',encoding='utf-8').read()
pattern = 'https://.*?/'        #.*尽可能的多匹配，.*?尽可能的少匹配
match=re.findall(pattern,f)
print(match)

import re
pattern = 'https://.*/'        #.*尽可能的多匹配，.*?尽可能的少匹配
match=re.findall(pattern,'https://www.hao123.com/')
print(match)