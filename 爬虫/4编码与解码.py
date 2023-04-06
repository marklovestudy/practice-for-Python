'''
一、编码：
编码在get请求中比较常见，是将请求地址中的参数进行编码，尤其是对于中文参数。
parse子模提供了urlencode()方法与quote()方法用于实现url的编码，
而unquote()方法可以实现对加密后的URL进行解码操作。
1.urlencode()方法实例：参数可以接受字典
import urllib.parse
base_url='http://httpbin.org/get'
params={'name':'mark','country':'china','age':'39'}
url=base_url+urllib.parse.urlencode(params)
print('编码后的请求地址为：',url)
2.quote()方法：参数可以接字符串
import urllib.parse
base_url='http://httpbin.org/get?country='
url=base_url+urllib.parse.quote('中国')
print('编码后的请求地址为：',url)

二、解码：
1.unquote()方法
import urllib.parse
base_url='http://httpbin.org/get?country='
params={'country':'中国'}
url1=base_url+urllib.parse.urlencode(params)
url2=base_url+urllib.parse.quote('country=中国')
print('urlencode编码后的请求地址为：',url1)
print('quote编码后的请求地址为：',url2)
print('urlencode解码：',urllib.parse.unquote(url1))
print('quote解码:',urllib.parse.unquote(url2))
'''
import urllib.parse
base_url='http://httpbin.org/get?country='
params={'country':'中国'}
url1=base_url+urllib.parse.urlencode(params)
url2=base_url+urllib.parse.quote('country=中国')
print('urlencode编码后的请求地址为：',url1)
print('quote编码后的请求地址为：',url2)
print('urlencode解码：',urllib.parse.unquote(url1))
print('quote解码:',urllib.parse.unquote(url2))