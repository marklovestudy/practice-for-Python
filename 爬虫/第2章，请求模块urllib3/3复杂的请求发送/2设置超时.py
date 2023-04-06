'''
设置超时
    在没有特殊要求的情况下，可以将设置超时的参数与时间填写在request()方法或者是PoolManager()代码如下：
import urllib3
urllib3.disable_warnings()
baidu_url='https://www.baidu.com/'
python_url='https://python.org/'
http1=urllib3.PoolManager()
try:
    r=http1.request('GET',baidu_url,timeout=0.01)
except Exception as error:      #Exception错误类型
    print('百度超时：',error)
http2=urllib3.PoolManager(timeout=0.01)
try:
    r=http2.request('GET',python_url)
except Exception as error:
    print('python超时：',error)

可以设置timeout()的参数：connect连接时间,read读取时间
import urllib3
urllib3.disable_warnings()
baidu_url='https://www.baidu.com/'
python_url='https://python.org/'
http1=urllib3.PoolManager()
timeout=urllib3.Timeout(connect=0.5,read=0.1)
try:
    r=http1.request('GET',baidu_url,timeout=timeout)
except Exception as error:      #Exception错误类型
    print('百度超时：',error)
http2=urllib3.PoolManager(timeout=timeout)
try:
    r=http2.request('GET',python_url)
except Exception as error:
    print('python超时：',error)
'''
import urllib3
urllib3.disable_warnings()
baidu_url='https://www.baidu.com/'
python_url='https://python.org/'
http1=urllib3.PoolManager()
timeout=urllib3.Timeout(connect=0.5,read=0.1)
try:
    r=http1.request('GET',baidu_url,timeout=timeout)
except Exception as error:      #Exception错误类型
    print('百度超时：',error)
http2=urllib3.PoolManager(timeout=timeout)
try:
    r=http2.request('GET',python_url)
except Exception as error:
    print('python超时：',error)
