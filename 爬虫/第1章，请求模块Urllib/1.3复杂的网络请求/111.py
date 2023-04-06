import urllib.request
url = "http://www.httpbin.org/get"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
    }
# 构建了两个代理Handler，一个有代理IP，一个没有代理IP
httpproxy_handler = urllib.request.ProxyHandler({"http": "61.135.217.7:80"})
opener = urllib.request.build_opener(httpproxy_handler)
request = urllib.request.Request(url, headers=header)
# 1. 如果这么写，只有使用opener.open()方法发送请求才使用自定义的代理，而urlopen()则不使用自定义代理。
response = opener.open(request)
# 2. 如果这么写，就是将opener应用到全局，之后所有的，不管是opener.open()还是urlopen() 发送请求，都将使用自定义代理。
# urllib2.install_opener(opener)
# response = urlopen(request)
print(response.read().decode('utf-8'))