'''
urlopen()方法，默认为get请求，如果需要发磅POST请求，可以为其设置data参数，该参数是bytes类型，
所以需要使用bytes()方法将参数进行数据类型的转换。
代码如下：
import urllib.request       #导入urllib.request模块
import urllib.parse         #导入urllib.parse模块
url='https://www.httpbin.org/post'      #POST请求测试地址
#将表单数据转换为BYTES类型，并设置编码方式为UTF-8
data=bytes(urllib.parse.urlencode({'hello':'python'}),encoding='utf-8')
response=urllib.request.urlopen(url=url,data=data)          #发送网络请求
print(response.read().decode('utf-8'))                      #读取HTML代码并进行， 打印请求结果
'''
import urllib.request
import urllib.parse
url='https://www.httpbin.org/post'
# url='https://www.baidu.com'
# data=bytes(urllib.parse.urlencode({'python':'hello'}),encoding='utf-8')
data=bytes(urllib.parse.urlencode({'hello':'python'}),encoding='utf-8')
r=urllib.request.Request(url=url,data=data,method='POST')   #此时头信息为程序
#r=urllib.request.Request(url=url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'},data=data,method='POST')
response=urllib.request.urlopen(r)
print(response.read().decode('utf-8'))