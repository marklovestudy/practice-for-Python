import urllib.request
import urllib.parse
import http.cookiejar
import json

url='http://www.baidu.com'
cookie_file='cookie.txt'
cookie=http.cookiejar.LWPCookieJar()
cookie.load(cookie_file,ignore_discard=True,ignore_expires=True)
cookie_processor=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(cookie_processor)
r=opener.open(url)
print(cookie,type(cookie))

