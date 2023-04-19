'''
cookie获取与设置
获取
import urllib.request
import urllib.parse
import http.cookiejar

url='http://www.baidu.com'
data=bytes(urllib.parse.urlencode({'username':'179722881','password':'ww19850820@'}),encoding='utf-8')
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
r=urllib.request.Request(url=url,data=data,headers=headers)
cookie_file='co419.txt'
cookie_ob=http.cookiejar.LWPCookieJar(cookie_file)
cookie_process=urllib.request.HTTPCookieProcessor(cookie_ob)
opener=urllib.request.build_opener(cookie_process)
response=opener.open(r)
cookie_ob.save(ignore_expires=True,ignore_discard=True)

设置
import urllib.request
import urllib.parse
import http.cookiejar

url='http://www.baidu.com'
data=bytes(urllib.parse.urlencode({'username':'179722881','password':'ww19850820@'}),encoding='utf-8')
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
r=urllib.request.Request(url=url,data=data,headers=headers)
cookie_file='co419.txt'
cookie_ob=http.cookiejar.LWPCookieJar(cookie_file)
cookie_ob.load(cookie_file,ignore_discard=True,ignore_expires=True)
cookie_process=urllib.request.HTTPCookieProcessor(cookie_ob)
opener=urllib.request.build_opener(cookie_process)
response=opener.open(r)
print(response.headers)

#IP设置
import urllib.request
import urllib.parse
import http.cookiejar
url='http://www.baidu.com'
data=bytes(urllib.parse.urlencode({'username':'179722881','password':'ww19850820@'}),encoding='utf-8')
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
r=urllib.request.Request(url=url,data=data,headers=headers)
ip={'https':'58.220.95.114:10053'}
proxy_ip=urllib.request.ProxyHandler(ip)
cookie_file='co4191.txt'
cookie_ob=http.cookiejar.LWPCookieJar(cookie_file)
cookie_process=urllib.request.HTTPCookieProcessor(cookie_ob)
opener=urllib.request.build_opener(proxy_ip,cookie_process)
response=opener.open(r)
print(response.read().decode('utf-8'))

异常处理
import urllib.request
import urllib.error
url='http://www.baidu.com'
try:
    urllib.request.urlopen(url=url,timeout=0.001)
except urllib.error.URLError as error:
    print(error.reason)
except urllib.error.HTTPError as error:
    print(error.reason)
    print(error.code)
    print(error.headers)
拆分和组合：
import urllib.request
import urllib.parse

url='https://docs.python.org/3/library/urllib.parse.html'
v1=urllib.parse.urlparse(url)
v2=urllib.parse.urlsplit(url)
v3= urllib.parse.urlunparse(v1)
v4= urllib.parse.urlunsplit(v2)
print(v1)
print(v2)
print(v3)
print(v4)

连接
import urllib.parse
url_base='https://docs.python.org'
v1='3/library/urllib.parse.html'
v2='https://docs.python.org/3/library/urllib.parse.html'
v11=urllib.parse.urljoin(url_base,v1)
v22=urllib.parse.urljoin(url_base,v2)
print(v11)
print(v22)

#编码和解码，编码过程中只接受字典
import urllib.parse
url='https://www.aigei.com/s?q=%E5%90%83%E8%B1%86%E4%BA%BA'
url_split=urllib.parse.urlsplit(url)
print(url_split)
v=urllib.parse.unquote(url_split.query)     #解码过程
print(v)
v1=urllib.parse.urlencode({v.split('=')[0]:v.split('=')[1]})        #编码
print(v1)

把把内容转换为想要的参数
import urllib.parse
url='https://www.aigei.com/s?q=%E5%90%83%E8%B1%86%E4%BA%BA'
url_split=urllib.parse.urlsplit(url)
print(url_split)
v=urllib.parse.unquote(url_split.query)     #解码过程
print(v)
v1=urllib.parse.urlencode({v.split('=')[0]:v.split('=')[1]})        #编码
v2=urllib.parse.parse_qs(v)             #转字典:qs   转列表:qsl
print(v1)
print(v2)
'''
