'''
    F12打开开发者工具箱，点network，看消息头，找到User-Agent。

设置请求头，代码如下：
import urllib3
urllib3.disable_warnings()
url='https://www.httpbin.org/get'
headers={'User-Agent':123}
http=urllib3.PoolManager()
r=http.request('GET',url,headers=headers)
print(r.data.decode('utf-8'))
'''
import urllib3
urllib3.disable_warnings()
url='https://www.httpbin.org/get'
headers={'User-Agent':123}
http=urllib3.PoolManager()
r=http.request('GET',url,headers=headers)
print(r.data.decode('utf-8'))