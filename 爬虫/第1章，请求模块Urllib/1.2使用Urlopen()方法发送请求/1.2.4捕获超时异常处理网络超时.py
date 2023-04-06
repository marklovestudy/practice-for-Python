
#如果遇到了超时异常，爬虫程序将在此处停止。所以在实际开发中开发者可以将超时异常捕获，然后再处理下面的爬虫任务。
#代码如下：
'''
import urllib.request
import urllib.error
import socket
url='https://www.python.org/'
try:
    response=urllib.request.urlopen(url=url,timeout=0.1)        #发送网络请求，超时设置为0.1秒
    print(response.read().decode('utf-8'))              #把HTML代码进行UTF-8解码
except urllib.error.URLError as error:                  #处理异常
    if isinstance(error.reason,socket.timeout):         #判断是否为超时异常
        print('当前任务超时，即将开始执行下一任务！')
'''
import urllib.request
import urllib.error
import socket
url='https://www.python.org/'
try:
    response=urllib.request.urlopen(url=url,timeout=0.01)
    print(response.read().decode('utf-8'))
except urllib.error.URLError as error:
    if isinstance(error.reason,socket.timeout):
        print('next')
##isinstance(3,int)    二个参数：前一个是实例，后一个是范例，如果二者相同返回：True,否则返回False.