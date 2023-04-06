'''
使用urllib3模块向服务器发送POST请求时并不复杂，与发送GET请求相似，只是需要在request()方法中将method参数设置为：POST
然后将field参数设置为字典类型的表单参数。
实现POST请求
import urllib3
urllib3.disable_warnings()                      #关闭ssl警告
url='https://www.httpbin.org/post'              #POST请求测试地址
params={'name':'Jack','chinese_name':'杰克','age':39}     #定义字典类型的请求参数
http=urllib3.PoolManager()                      #创建连接池管理对象
r=http.request('POST',url,fields=params)        #发送POST请求
print(r.status)
print(r.data.decode('utf-8'))                   #杰克显示为："\u6770\u514b"
print(r.data.decode('unicode_escape'))          #用这种编码可以把"\u6770\u514b"显示为中文
'''
import urllib3
urllib3.disable_warnings()                      #关闭客户端ssl验证警告
url='https://www.httpbin.org/post'              #POST请求测试地址
params={'name':'Jack','chinese_name':'杰克','age':39}     #定义字典类型的请求参数
http=urllib3.PoolManager()                      #创建连接池管理对象
r=http.request('POST',url,fields=params)        #发送POST请求
print(r.status)
print(r.data.decode('utf-8'))                   #杰克显示为："\u6770\u514b"
print(r.data.decode('unicode_escape'))          #用这种编码可以把"\u6770\u514b"显示为中文