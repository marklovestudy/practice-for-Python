'''
上传文件
用requests模块实现上传图片文件
    使用requests模块向服务器上传文件，只需要指定POST函数中files参数即可。files参数可以指定一个BufferedReader对象，
该对象可以使用open()函数返回。代码如下
import requests
bd=open('bd_logo.png','rb')
file={'file':bd}
response=requests.post('http://httpbin.org/post',files=file)
print(response.text)
'''
