'''
通过retries参数设置重试请求
    urllib3模块可以自动重试请求，这种相同的机制还可以处理重定向。在默认情况下request()方法的请求重试次数为3次，
如果需要修改重试次数可以设置retries参数。修改重试测试的示例代码如下：
import urllib3
urllib3.disable_warnings()
url='https://www.httpbin.org/get'
http=urllib3.PoolManager()
r=http.request('GET',url)
r1=http.request('GET',url,retries=5)                #发送GET请求，设置5次重试请求
r2=http.request('GET',url,retries=False)            #关闭重试请求
print('r默认重试请求次数：',r.retries.total)
print('r1设置重试请求次数：',r1.retries.total)
print('r2关闭重试请求次数：',r2.retries.total)

'''
import urllib3
urllib3.disable_warnings()
url='https://www.httpbin.org/get'
http=urllib3.PoolManager()
r=http.request('GET',url)
r1=http.request('GET',url,retries=5)                #发送GET请求，设置5次重试请求
r2=http.request('GET',url,retries=False)            #关闭重试请求
print('r默认重试请求次数：',r.retries.total)
print('r1设置重试请求次数：',r1.retries.total)
print('r2关闭重试请求次数：',r2.retries.total)