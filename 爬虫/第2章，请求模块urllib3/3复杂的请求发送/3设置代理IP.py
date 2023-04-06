'''
设置代理IP
    创建ProxyManager对象设置代理IP
    在设置代理IP时，需要创建ProxyManager对象，在该对象中最好填写两个参数：
    proxy_url,表示需要填写的代理IP；
    headers,用于模拟浏览器请求，避免后台服务器发现。示例代码如下：
import urllib3
url='http://www.httpbin.org/ip'             #代理IP请求测试地址
headers={'User-Agent':123}
#创建代理管理对象
proxy=urllib3.ProxyManager('http://120.27.110.143:80',headers = headers)
r=proxy.request('GET',url,timeout=2.0)
print(r.data.decode())
注：ip失效请上网查找
'''
