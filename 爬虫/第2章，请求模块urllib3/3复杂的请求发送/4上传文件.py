'''
request()方法有二种方式上传文件：
    fields:以元组形式分别指定文件名，文件内容以及文件类型，这种方式适合上传文本文件时使用。如txt等
    body：如果需要上传图片则可以使用第二种方式，在request()方法中指定body参数，该参数所对应的值为
    图片的二进制数据，然后还需要使用headers参数为其指定文件类型。
实例1：通过指定fields参数上传文本文件
import urllib3
import json
url='http://httpbin.org/post'
with open('text.txt','r',encoding='utf-8') as f:
    data=f.read()
http=urllib3.PoolManager()      #创建连接池管理对象
r=http.request('POST',url,fields={'filefield':('example.txt',data),})
files=json.loads(r.data.decode('utf-8'))['files']
print(files)

实例2：通过body参数上传图片文件
import urllib3
import json
url='http://httpbin.org/post'
with open('123.png','rb') as f:
    data=f.read()
http=urllib3.PoolManager()      #创建连接池管理对象
r=http.request('POST',url,body=data,headers={'content-Type':'image/jpeg'})
print(r.data.decode())
'''
import urllib3
import json
url='http://httpbin.org/post'
with open('123.png','rb') as f:
    data=f.read()
http=urllib3.PoolManager()      #创建连接池管理对象
r=http.request('POST',url,body=data,headers={'content-Type':'image/jpeg'})
print(r.data.decode())
