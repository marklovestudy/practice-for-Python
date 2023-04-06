import urllib.request
import urllib.parse
url='https://www.baidu.com/'
response=urllib.request.urlopen(url=url)
response=response.read().decode('utf-8')
print(response)
with open('4K.text','w',encoding='utf-8') as f:
    f.write(response)
