'''
打香洲二手房间
response=response.encode('iso-8859-1').decode('gbk')        #处理中文乱码的现象。
'''
import requests
from lxml import etree
import requests_cache
requests_cache.install_cache()
requests_cache.clear()
url='https://zh.58.com/xiangzhou/chuzu/0/j1/?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&PGTID=0d3090a7-0038-f86f-9939-4d7bd7115866&ClickID=2'
headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                       ' AppleWebKit/537.36 (KHTML, like Gecko)'
                       ' Chrome/109.0.0.0 Safari/537.36'
    }
response=requests.get(url=url,headers=headers).text
tree=etree.HTML(response)
des_list=tree.xpath('//div[@class="des"]')          #ip被封了
print(des_list)