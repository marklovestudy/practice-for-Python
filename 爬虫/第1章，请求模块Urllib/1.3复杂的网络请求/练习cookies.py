# import urllib.request
# import urllib.parse
# # from pprint import pprint
# #1确定访问对象
# url = 'https://www.baidu.com'
# #2发起请求:伪装/data设置
# #伪装
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
# #设置data
# data=bytes(urllib.parse.urlencode({'username':'mynameismark23','password':'ww19850820'}),encoding='utf-8')
# #创建一个Request()
# r=urllib.request.Request(url=url,data=data,headers=headers)
# response=urllib.request.urlopen(r)
# #3数据处理
# print(response.read().decode('utf-8'))

import urllib.request
import urllib.parse
import http.cookiejar
url = 'https://www.baidu.com'#1确定访问对象
#2发起请求
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
#设置data
data=bytes(urllib.parse.urlencode({'username':'mynameismark23','password':'ww19850820'}),encoding='utf-8')
#创建一个Request()
r=urllib.request.Request(url=url,data=data,headers=headers)     #被访问的对象
cookie_file='cookie.txt'        #创建文件对象
cookie = http.cookiejar.LWPCookieJar(cookie_file)     #创建一个LWPCOOKIEJAR对象
cookie_process=urllib.request.HTTPCookieProcessor(cookie)     #创建处理器
opener=urllib.request.build_opener(cookie_process)      #创建一个opener对像
opener.open(r)
cookie.save(ignore_discard=True,ignore_expires=True)    #把cookie文件保存起来
for i in cookie:
    print(i.name+'='+i.value)