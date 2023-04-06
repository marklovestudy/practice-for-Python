'''
    通过上一节的学习可以得知，urlopen()方法能够发送一个最基本的网络请求，但这并不是一个完整的网络请求。
如果要构建一个完整的网络请求，还需要在请求中添加Header、Cookies以及代理IP等内容，这样才能更好的模拟一个
浏览器所发送的网络请求。Request类则可以构建一个多种功能的请求对象，其语法格式如下：
urllib.request.Request(url,data,headers={},origin_req_host=None,unverifiable=False,method=None)
    *url:需要访问的网址
    *data:参数默认为None，通过该参数确认请求方式，如果是None,表示请求方式为GET，否则请求方式为POST，在发送POST请求时，
    参数data需要以字典形式的数据作为参数值，并且需要将字典类型的参数值转换为字节类型的数据才可以实现POST请求
    *headers:设置请求头部信息，该参数为字典类型。添加请求头信息最常见的用法就是修改User-Agent为伪装成浏览器。
    例如：headers={'User-Agent':'Mozilla/5.0(Windows NT 10.0;WOW64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/83.0.4103.61 Safari/537.36'},
    表示伪装成谷歌浏览器进行网络请求
    *origin_req_host:用于设置请求方的host名称或者是IP.
    *unverifiable:用于设置网页是否需要验证，默认是False.
    *method:用于设置请求方式，如GET、POST等，默认为GET请求。

一、查看当前头信息，以及头信息的作用。
设置请求头参数是为了模拟浏览器向网页后台发送网络请求，这样可以避免服务器的反爬措施，使用urlopen()方法发送网络请求时，
其本身并没有设置请求头参数，所以向http://www.httpbin.org/post请求测试地址发送请求时，返回的信息中headers将显示为默认值：Python-urllib/3.8
import urllib.request       #导入urllib.request模块
import urllib.parse         #导入urllib.parse模块
url='https://www.httpbin.org/post'      #POST请求测试地址
#将表单数据转换为BYTES类型，并设置编码方式为UTF-8
data=bytes(urllib.parse.urlencode({'hello':'python'}),encoding='utf-8')
response=urllib.request.urlopen(url=url,data=data)          #发送网络请求
print(response.read().decode('utf-8'))                      #读取HTML代码并进行， 打印请求结果

运行结果：
{
  "args": {},
  "data": "",
  "files": {},
  "form": {
    "hello": "python"
  },
  "headers": {
    "Accept-Encoding": "identity",
    "Content-Length": "12",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "www.httpbin.org",
    "User-Agent": "Python-urllib/3.8",          ########默认值
    "X-Amzn-Trace-Id": "Root=1-63c6861c-76af282b13a5ae830d069266"
  },
  "json": null,
  "origin": "223.73.237.104",
  "url": "https://www.httpbin.org/post"
}

二、获取请求头信息：F12打开‘开发者工具’：
    1选择：network
    2打开网址：https://www.python.org
    3选择请求信息：www.python.org
    4选择headers
    5获取：User-Agent:对应的值为请求头信息

三、设置请求头信息：
    如果需要设置请求头信息，1先通过Request类构造一个带有headers请求头信息的Request对象，然后为urlopen()方法传入Request对象，
    再进行网络请求。代码如下：
import urllib.request       #导入urllib.request模块
import urllib.parse         #导入urllib.parse模块
url='https://www.httpbin.org/post'      #POST请求测试地址
#将表单数据转换为BYTES类型，并设置编码方式为UTF-8
data=bytes(urllib.parse.urlencode({'hello':'python'}),encoding='utf-8')
#创建一个Request对象
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
r=urllib.request.Request(url=url,data=data,headers=headers,method='POST')
response=urllib.request.urlopen(r)          #发送网络请求
print(response.read().decode('utf-8'))                      #读取HTML代码并进行， 打印请求结果

运行后：User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36

实例1：不设置头信息和设置头信息的区别，以百度为例：
不设置头信息如下：
import urllib.request
url='https://www.baidu.com'
response=urllib.request.urlopen(url)
print(response.read().decode('utf-8'))

<html>
<head>
	<script>
		location.replace(location.href.replace("https://","http://"));
	</script>
</head>
<body>
	<noscript><meta http-equiv="refresh" content="0;url=http://www.baidu.com/"></noscript>
</body>
</html>

设置头信息如下
import urllib.request
import urllib.parse
url='https://www.baidu.com/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
r=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(r)
print(response.read().decode('utf-8'))

运行结果：略。
'''
# import urllib.request       #导入urllib.request模块
# import urllib.parse         #导入urllib.parse模块
# url='https://www.httpbin.org/post'      #POST请求测试地址
# #将表单数据转换为BYTES类型，并设置编码方式为UTF-8
# data=bytes(urllib.parse.urlencode({'hello':'python'}),encoding='utf-8')
# #创建一个Request对象
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
# r=urllib.request.Request(url=url,data=data,headers=headers,method='POST')
# response=urllib.request.urlopen(r)          #发送网络请求
# print(response.read().decode('utf-8'))                      #读取HTML代码并进行， 打印请求结果
#
import urllib.request
import urllib.parse
url='https://www.baidu.com/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
r=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(r)
print(response.read().decode('utf-8'))