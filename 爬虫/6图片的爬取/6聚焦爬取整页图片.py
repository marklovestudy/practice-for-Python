import requests
import re
import os
headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                       ' AppleWebKit/537.36 (KHTML, like Gecko)'
                       ' Chrome/109.0.0.0 Safari/537.36'
    }
# url='https://www.aigei.com/s?q=三国志&type=design'
#
# response=requests.get(url,headers=headers).text
# with open('text.text','w',encoding='utf-8') as f:
#     f.write(response)
with open('text.text', 'r', encoding='utf-8') as f:
    url=f.read()
    # print(url,type(url))
# pattern='<img width=.*?\s+.*?\s"\s++src="(.*?)"\s+>'
pattern='<img width=.*?\s+.*?\s+"\s+src="(.*?)"\s+>'
r=re.findall(pattern,url)
print(r)
for i in r:
    url='http:'+i
    response=requests.get(url,headers=headers).content
    filename=i.split('/')[-1][-6:-1]+'.jpg'
    with open(filename,'wb') as f:
        f.write(response)
        print(filename,'下完了')
