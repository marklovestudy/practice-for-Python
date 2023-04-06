import requests
from lxml import etree
import requests_cache
requests_cache.install_cache()
requests_cache.clear()
url='https://www.zhihu.com/market/paid_column/1586380657579499520/section/1599093768459935744'
headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                       ' AppleWebKit/537.36 (KHTML, like Gecko)'
                       ' Chrome/109.0.0.0 Safari/537.36'
    }
response=requests.get(url=url,headers=headers).text
tree=etree.HTML(response)
des_list=tree.xpath('/html/body/main/div/div[2]//text()')
f=open('瑶瑶如意.text','w',encoding='utf-8')
n=1
for div in des_list:
    f.write(div+'\n')
print(n,'已经下载完了')