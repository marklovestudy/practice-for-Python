# import urllib.request
# url='http://www.httpbin.org/get'
# #创建代理IP
# proxy_handler = urllib.request.ProxyHandler({'https':'2.32.123.32：3344'})
# opener=urllib.request.build_opener(proxy_handler)
# r=urllib.request.Request(url=url,headers={'User-Agent':'12333'})
# response=opener.open(r,timeout=2)
# print(response.read().decode('utf-8'))

import urllib.request
import re       #正则：解析数据
ips=[]
#确定访问对象
url='https://www.kuaidaili.com/free/inha/'
'https://www.kuaidaili.com/free/inha/1/'
for i in range(1,2):
    url='https://www.kuaidaili.com/free/inha/%s/'%i
#发起请求
#伪装,创建一个r对象(伪装信息和访问的服务对象)，
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
    r=urllib.request.Request(url=url,headers=header)
    response=urllib.request.urlopen(r)      #页面爬取：所有内容
    response=response.read().decode("utf-8")
    print(type(response))
    ip_list=re.findall('.*?<td data-title="IP">(.*?)</td>.*?',response)        #在response里找到所有的IP
    ip_port=re.findall('.*?<td data-title="PORT">(.*?)</td>.*?',response)         #找到我们的端口
    print(ip_list)
    print(ip_port)
    for i in range(len(ip_list)):
        #{'https':'2.32.123.32：3344'}
        v={'http':'{}:{}'.format(ip_list[i],ip_port[i])}
        ips.append(v)
print(ips)      #前五页的IP
import time
for i in ips:
    url='http://www.httpbin.org/get'
    #创建代理IP
    proxy_handler = urllib.request.ProxyHandler(i)
    opener=urllib.request.build_opener(proxy_handler)
    r=urllib.request.Request(url=url,headers={'User-Agent':'12333'})
    response=opener.open(r,timeout=2)
    print(response.read().decode('utf-8'))
    time.sleep(5)