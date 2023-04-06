'''
urlopen()方法中的timeout参数，用于设置请求超时，该参数以秒为单位，表示如果在请求时，
如果超出了设置时间还没有得到时就抛出异常。
代码如下：
import urllib.request
url='https://www.python.org/'
response=urllib.request.urlopen(url=url,timeout=0.1)    #发送网络请求，设置超时为0.1秒，没超时返回数据，超时抛出异常
print(response.read().decode('utf-8'))                  #读取HTML代码并进行UTF-8解码。
'''
