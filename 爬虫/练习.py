import urllib.request
import urllib.error
import urllib.parse
import socket
url='https://www.httpbin.org/post'
data=bytes(urllib.parse.urlencode({1:22}),encoding='utf-8')
r=urllib.request.Request(url=url,data=data,headers={'User-Agent':'hahaha'})
try:
    response=urllib.request.urlopen(r,timeout=1)
    print(response.read().decode('utf-8'))
except urllib.error.URLError as error:
    print(error.reason,type(error.reason))
    print(socket.timeout)
    if isinstance(error.reason,socket.timeout):
        print('next')