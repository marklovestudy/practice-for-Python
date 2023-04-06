'''
设置代理IP，反爬，多次同一IP获取大量数据会被禁止IP。所以要修改不同的IP。
代码如下：代理IP存在时间很短，免费的IP会在后面二章中学习。
import urllib.request
url='http://www.httpbin.org/get'
#创建代理IP
proxy_handler = urllib.request.ProxyHandler({'https':'58.220.95.114:10053'})
opener=urllib.request.build_opener(proxy_handler)
r=urllib.request.Request(url=url,headers={'User-Agent':'12333'})
response=opener.open(r,timeout=2)
print(response.read().decode('utf-8'))
'''

import urllib.request
url='http://www.httpbin.org/get'
#创建代理IP
proxy_handler = urllib.request.ProxyHandler({'https':'59.110.154.102:8080'})
opener=urllib.request.build_opener(proxy_handler)
r=urllib.request.Request(url=url,headers={'User-Agent':'12333'})
response=opener.open(r,timeout=5)
print(response.read().decode('utf-8'))
