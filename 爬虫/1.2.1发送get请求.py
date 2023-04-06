'''
一、发送GET请求
    在使用urlopen()方法实现网络请求时，所返回的是一个'http.client.HTTPResponse'对象。
示例代码如下：
import urllib.request
response=urllb.request.urlopen('https://www.baidu.com/')   #发送网络请求
print('响应数据类型为:',type(response))
print(response)

示例：HTTPResponse常用的方法与属性获取信息
    在HTTPResponse对象中包含可以获取的方法及属性，下面通下几个常用的方法与属性进行演示。如下：
import urllib.request
url='https://www.python.org/'
response=urllib.request.urlopen(url=url)   #发送网络请求
print('响应状态码：',response.status)
print('响应头文件：',response.getheaders())
print('响应头指定信息：',response.getheader('Accept-Ranges'))
#读取HTML代码，并进行UTF-8解码
print('Python官网HTML代码如下：\n',response.read().decode('utf-8'))
print(response)
'''
import urllib.request
url='https://s1.aigei.com/src/img/jpg/b4/b42dfcfea9bb497f93967256e4f82edc.jpg?imageMogr2/auto-orient/thumbnail/!500x465r/gravity/Center/crop/500x465/quality/85/%7CimageView2/2/w/500/%7Cwatermark/3/text/54ix57uZ572R57Sg5p2Q57yW5Y-3IzQxMDkyNzM3/font/5b6u6L2v6ZuF6buR/fontsize/287/fill/cmVk/dissolve/37/gravity/SouthEast/dx/13/dy/13/text/6K6-6K6h57Sg5p2Q/font/5b6u6L2v6ZuF6buR/fontsize/287/fill/cmVk/dissolve/37/gravity/NorthWest/dx/13/dy/13/text/5pe25bCa5Y2h6YCa576O5aWz/font/5b6u6L2v6ZuF6buR/fontsize/287/fill/cmVk/dissolve/37/gravity/NorthEast/dx/13/dy/13//text/54ix57uZ572RIGFpZ2VpLmNvbQ==/font/5b6u6L2v6ZuF6buR/fontsize/300/fill/R3JlZW4=/dissolve/55/gravity/NorthWest/dx/255/dy/249/image/aHR0cHM6Ly9zMS5haWdlaS5jb20vd2F0ZXJtYXJrLzI0MC0xLnBuZz9lPTE3MzU0ODgwMDAmdG9rZW49UDdTMlhwemZ6MTF2QWtBU0xUa2ZITjdGdy1vT1pCZWNxZUpheHlwTDpxLUpqN1BxODhPMnFlOW81eDQ2TVI3bkREQmc9/dissolve/40/gravity/NorthWest/dx/115/dy/98/ws/0.0/wst/0&e=1735488000&token=P7S2Xpzfz11vAkASLTkfHN7Fw-oOZBecqeJaxypL:ZvnreoQFOy-dgMZ5ogUD9lr3Fjc='
response=urllib.request.urlopen(url)
print(response.status)
print(response.getheaders())
print(response.getheader('Accept-Ranges'))
v=response.read()
with open('11.png','wb') as f:
    f.write(v)