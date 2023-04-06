'''
使用urllib3发送网络请求时，首先需要创建PoolManager对象，通过该对象调用request()方法来实现网络请求的发送。格式如下：
request(method,url,field=None,headers=None,**urlopen_kw)
常用参数说明：
    method:必选参数，用于指定请求方式，如：GET,POST,PUT等。
    url:必选参数，用于设置需要请求的URL地址。
    fields:可选参数，用于设置请求参数。
    headers:可选参数，用于设置请求头。

用request()方法实现GET请求。
import urllib3
url='http://httpbin.org/get'
http=urllib3.PoolManager()              #创建连接池管理对象
r=http.request('GET',url)               #发送GET请求
print(r.status)                         #打印状态码

用request()方法实现一对多个服务器发送请求
import urllib3
jd_url='https://www.jd.com/'
py_url='https://www.python.org/'
baidu_url='https://www.baidu.com/'
http=urllib3.PoolManager()                  #创建连接池管理对象
r1=http.request('GET',jd_url)                #发送GET请求
r2=http.request('GET',py_url)
r3=http.request('GET',baidu_url)
print('京东请求状态码：',r1.status)                             #打印状态码
print('python请求状态码：',r2.status)                             #打印状态码
print('百度请求状态码：',r3.status)                             #打印状态码
'''
import urllib3
jd_url='https://www.jd.com/'
py_url='https://www.python.org/'
baidu_url='https://www.baidu.com/'
http=urllib3.PoolManager()                  #创建连接池管理对象
r1=http.request('GET',jd_url)                #发送GET请求
r2=http.request('GET',py_url)
r3=http.request('GET',baidu_url)
print('京东请求状态码：',r1.status)                             #打印状态码
print('python请求状态码：',r2.status)                             #打印状态码
print('百度请求状态码：',r3.status)                             #打印状态码
print(r1.data.decode('utf-8'))