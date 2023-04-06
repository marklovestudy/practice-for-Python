'''
1添加请求头headers
添加请求头模拟浏览器头部信息访问网页
    有时在请求一个网页内容时，会发现无论通过GET，POST以及其他请求方式，都会出现403错误，这种现象多数为服务器拒绝您的访问，
那是因为这些网页为了防止恶意采集信息，所使用的反爬设置。此时可以通过模拟浏览器的头部信息来进行访问，这样就能解决以上反爬的
问题，下面介绍requests模块添加请求头的方式，代码如下：
import requests
url='https://www.baidu.com/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
response=requests.get(url,headers=headers)
print(response.status_code)
运行结果：
200
'''
import requests
url='https://www.baidu.com/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
response=requests.get(url,headers=headers)
print(response.status_code)