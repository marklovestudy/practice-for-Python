'''
    Cookie是服务器向客户端返回响应数据是留下的标记，当客户端再次访问服务器时将携带这个标记。一般在实现登录一个页面时，
登陆成功后，会在浏览器的Cookie中保留一些信息，当浏览器再次访问时会携带Cookie中的信息，经过服务器核对后便可以确认当前用户
已经登陆过，此时可以直接将登陆后的数据返回。
    在使用爬虫获取网页登陆后的数据时，除了使用模拟登录以外，还可以获取登录后的Cookie，然后利用这个Cookie再次发送请求时，
就能以登录用户的身份获取数据。
实例如：
    登录后的用户名信息--中国电子学会网等

模拟登录
示例：发送POST请求实现网页的模拟登录。
    在实现爬虫的模拟登录时，首选需要获取登录验证的请求地址，然后通过POST请求的方式将正确的用户名与密码发送至登录验证的后台地址。
    （1）在火狐浏览器中打开地址https://www.zhihu.com/,然后单击网页中右上角的'登录'按钮，此时将弹出登录窗口
    （2）F12。点开网络，再单击右边的设置按钮，勾选‘持续记录’
    （3）在登录窗口中输入正确的用户名和密码，然后单击登录。在‘开发者工具箱’的网络请求列表中找到

实例：
import urllib.request
import urllib.parse
url='http://www.baidu.com'
data=bytes(urllib.parse.urlencode({'username':'179722881','password':'ww19850820@'}),encoding='utf-8')
r=urllib.request.Request(url=url,data=data,method='POST')
response=urllib.request.urlopen(r)
print(response.read().decode('utf-8'))

实例：模拟登录过程中获取Cookie信息
import urllib.request
import urllib.parse
import http.cookiejar
import json

url='http://www.baidu.com'
data=bytes(urllib.parse.urlencode({'username':'179722881','password':'ww19850820@'}),encoding='utf-8')
cookie=http.cookiejar.CookieJar()
cookie_processor=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(cookie_processor)
response=opener.open(url,data=data)
response=response.read().decode('utf-8')
print(cookie)
for i in cookie:
    print(i.name + '=' + i.value)

保存cookie信息：
import urllib.request
import urllib.parse
import http.cookiejar
import json

url='http://www.baidu.com'
data=bytes(urllib.parse.urlencode({'username':'179722881','password':'ww19850820@'}),encoding='utf-8')
cookie_file='cookie.txt'                                        #保存Cookie文件
cookie=http.cookiejar.LWPCookieJar(cookie_file)                 #创建LWPCookieJar对象
cookie_processor=urllib.request.HTTPCookieProcessor(cookie)     #生成cookie处理器
opener=urllib.request.build_opener(cookie_processor)            #创建opener对象
response=opener.open(url,data=data)
response=response.read().decode('utf-8')
cookie.save(ignore_discard=True,ignore_expires=True)            #保存Cookie文件
不难看出两个参数的实际作用是：
ignore_discard的意思是即使cookies将被丢弃也将它保存下来，
ignore_expires的意思是如果cookies已经过期也将它保存并且文件已存在时将覆盖，在这里，我们将这两个全部设置为True。
运行之后，cookies将被保存到cookie.txt文件中。

读取cookie中的信息
import urllib.request
import urllib.parse
import http.cookiejar
import json

url='http://www.baidu.com'
data=bytes(urllib.parse.urlencode({'username':'179722881','password':'ww19850820@'}),encoding='utf-8')
cookie_file='cookie.txt'
cookie=http.cookiejar.LWPCookieJar(cookie_file)
cookie.load(cookie_file,ignore_expires=True,ignore_discard=True)
cookie_processor=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(cookie_processor)
response=opener.open(url,data=data)
response=response.read().decode('utf-8')
print(response)
'''
import urllib.request
import urllib.parse
import http.cookiejar
import json

url='http://www.baidu.com'
data=bytes(urllib.parse.urlencode({'username':'179722881','password':'ww19850820@'}),encoding='utf-8')
cookie_file='cookie.txt'
cookie=http.cookiejar.LWPCookieJar(cookie_file)
cookie.load(cookie_file,ignore_expires=True,ignore_discard=True)
cookie_processor=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(cookie_processor)
response=opener.open(url,data=data)
response=response.read().decode('utf-8')
print(response)