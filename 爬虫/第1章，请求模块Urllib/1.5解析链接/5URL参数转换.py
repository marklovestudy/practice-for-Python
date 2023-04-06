'''
URL参数的转换
请求地址URL是一个字符串，如果需要将其中的参数转换为字典类型，可以先使用urlsplit()拆分URL，
然后再用query属性获取URL中的参数，最后使用parse_qs()方法将参数转换为字典类型数据。
实例1：转字典
import urllib.parse
url='http://httpbin.org/get?name=Jack&country=%E4%B8%AD%E5%9B%BD&age=30'
q=urllib.parse.urlsplit(url).query
q_dict=urllib.parse.parse_qs(q)
print(q_dict)
实例2：转列表
import urllib.parse
url='http://httpbin.org/get?name=Jack&country=%E4%B8%AD%E5%9B%BD&age=30'
q=urllib.parse.urlsplit(url).query
q_dict=urllib.parse.parse_qsl(q)
print(q_dict)
'''
import urllib.parse
url='http://httpbin.org/get?name=Jack&country=%E4%B8%AD%E5%9B%BD&age=30'
q=urllib.parse.urlsplit(url).query
q_dict=urllib.parse.parse_qs(q)
print(q_dict)