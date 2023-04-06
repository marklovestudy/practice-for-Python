import requests
r=requests.get('https://www.dieniao.com/FreeProxy/1.html')
r.encoding='utf-8'
print(r.text)