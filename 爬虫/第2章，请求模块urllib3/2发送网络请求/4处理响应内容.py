'''
1获取响应头
    通过info()方法获取响应头信息
    发送网络请求后，将返回一个HTTPResponse对象，通过该对象中的info()方法即可获取HTTP响应头信息，该信息为字典类型数据，
所以需要通过for循环进行遍历才可清晰的看到每条响应头信息内容。代码如下：
import urllib3
urllib3.disable_warnings()
url='https://www.httpbin.org/get'
http=urllib3.PoolManager()
r=http.request('GET',url)
response_headers=r.info()
#第一种表达方式：
for k in response_headers.keys():
    print(k,':',response_headers.get(k))
#第二种表达方式：
for k,v in response_headers.items():
    print(k,':',v)
#第三种表达方式：
for k in response_headers.keys():
    print(k,':',response_headers[k])

2.JSON信息
    处理服务器返回的JSON信息
    如果服务器返回了一条JSON信息，而这条信息中只有某条数据为可用数据时，可以先返回的JSON数据转换为字典数据，
接着直接获取指定键所对应的值即可。代码如下：
import urllib3
import json
urllib3.disable_warnings()
url='https://www.httpbin.org/post'
params={'name':'mark','country':'中国','age':39}     #定义字典类型的请求参数
http=urllib3.PoolManager()
r=http.request('POST',url,fields=params)                    #发送POST请求
j=json.loads(r.data.decode('unicode_escape'))               #将响应数据转换为字典类型
print('响应数据类型：',type(r.data.decode('unicode_escape')))      #json字典字符类型
# print('响应数据：',r.data.decode('unicode_escape'))
print('数据类型：',type(j))
print('获取form对应数据：',j.get('form'))                  #dict.get(key)和dict[key]取值方式
print('获取country对应的数据',j['form']['country'])

3二进制数据
    处理服务器返回的二进制数据
    如果响应数据为二进制数据，也可以做出相应的处理，例如，响应内容为图片的二进制数据旰，则可以使用open()函数，
将二进制数据转换为图片。代码如下：
import urllib3
urllib3.disable_warnings()
url='https://img1.bdstatic.com/static/searchresult/img/baseimg4_bc62837.png'
http=urllib3.PoolManager()
r=http.request('GET',url)                    #发送请求
print(r.data)                               #打印二进制数据
f=open('123.png','wb+')                     #创建文件对象f
f.write(r.data)                             #在f中写入二进制数据
f.close()                                   #关闭文件
'''
import urllib3
urllib3.disable_warnings()
url='https://img1.bdstatic.com/static/searchresult/img/baseimg4_bc62837.png'
http=urllib3.PoolManager()
r=http.request('GET',url)                    #发送请求
print(r.data)
f=open('123.png','wb+')
f.write(r.data)
f.close()