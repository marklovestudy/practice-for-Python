'''
设置请求参数data实现POST请求
    POST请求方式也叫作提交表单，表单中的数据内容就是对应的请求参数。使用requests模块实现POST请求时需要设置请求参数data.
代码如下：
import requests
import json
data={'1':'好好学习',
      '2':'天天向上'}
url='http://httpbin.org/post'
response=requests.post(url,data=data)
print(type(response.text))
response_dict=json.loads(response.text)
print(response_dict)
'''
import requests
import json
data={'1':'好好学习',
      '2':'天天向上'}
url='http://httpbin.org/post'
response=requests.post(url,data=data)
print(type(response.text))
response_dict=json.loads(response.text)
print(response_dict)