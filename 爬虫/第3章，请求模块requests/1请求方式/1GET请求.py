'''
requests是python中实现HTTP请求的一种方式，requests是第三方模块，该模块在实现HTTP请求时要比urllib,
urllib3模块简化很多，操作更加人性化。
请求方式：
    由于requests模块为第三方模块，requests功能特性如下：
    Keep-Alive&连接池              Unicode响应体              自动解压
    国际化域名和URL                 HTTP(S)代理支持             支持.netrc
    带持久Cookie的会话              文件分块上传                 分块请求
    浏览器式的SSL认证                流下载                     优雅的key/value Cookie
    自动内容解码                    连接超时                    基本/摘要式的身份认证

GET请求的二种方式，1不带参，2带参数
1实例：实现不带参数的GET网络请求：
import requests
url='https://www.baidu.com'
response=requests.get(url)
print('响应状态码：',response.status_code)
print('请求的网络地址为：',response.url)
print('头信息：',response.headers)
print('cookie信息：：',response.cookies)

2对响应结果进行UTF-8编码：
import requests
url='https://www.baidu.com'
response=requests.get(url)
response.encoding='utf-8'
print(response.text)

3爬取二进制数据
实例：爬取百度页面中图片
import requests
url='https://www.baidu.com/img/flexible/logo/pc/result.png'
response=requests.get(url)
print(response.content)
with open('bd_logo.png','wb') as f:
    f.write(response.content)

4GET带参请求：1URL带参，2params参数
***1URL带参如下：
    如果需要为GET请求指定参数时，可以直接将参数添加在请求地址URL后面，然后用问号(?)进行分隔，
    如果一个URL地址中有多个参数，参数之间用'&'进行连接。
GET请求代码如下：
import requests
url='http://www.httpbin.org/get?name=mark&age=39'
response=requests.get(url)
print(response.text)

***params参数
    requests模块提供了传递参数的方法，允许使用params关键字参数以一个字符串字典来提供这些参数。
    例如，想传递key1=value1和key2=value2到httpbin.org/get,可以使用如下代码：
import requests
url='http://www.httpbin.org/get'
data={'name':'mark','age':'36'}
response=requests.get(url,params=data)
print(response.text)
'''
import requests
url='http://www.httpbin.org/get'
data={'name':'mark','age':'36'}
response=requests.get(url,params=data)
print(response.text)
