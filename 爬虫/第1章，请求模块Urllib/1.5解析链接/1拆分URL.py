'''
一、拆分方法：urlparse(),urlsplit()
urlparse()把url分解成不同部分：
语法urllib.parse.urlparse(urlstring,scheme='',allow_fragments=True)
urlstring:url字符串
scheme:可选参数，表示需要设置的默认协议。如果需要拆分的URL中没有协议（https,http等），
可以通过该参数设置一个默认的协议，该参数的默认值为空字符串
allow_fragments:可选参数，如果该参数设置为False，表示忽略fragment这部分内容，默认为True.

拆分URL实例：
urlparse()方法
import urllib.parse
url='https://docs.python.org/3/library/urllib.parse.html'
parse_result=urllib.parse.urlparse(url)
print(type(parse_result))
print(parse_result)

拆分URL返回结果parse_result属性
ParseResult(scheme='https', netloc='docs.python.org', path='/3/library/urllib.parse.html', params='', query='', fragment='')
print('sheme:',parse_result.scheme)
print('netloc:',parse_result.netloc)
print('path:',parse_result.path)

urlsplit()方法：与urlparse()唯一不同之处：把params加入到了path中
import urllib.parse
url='https://docs.python.org/3/library/urllib.parse.html'
parse_result=urllib.parse.urlsplit(url)
print(type(parse_result))
print(parse_result)
print(parse_result[0])      #可索引取值
'''
import urllib.parse
url='https://docs.python.org/3/library/urllib.parse.html'
parse_result=urllib.parse.urlsplit(url)
print(type(parse_result))
print(parse_result)


