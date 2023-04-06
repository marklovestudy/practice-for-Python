import requests
from lxml import etree
import requests_cache
import os
if not os.path.exists('./jianli'):
    os.mkdir('./jianli')
requests_cache.install_cache()
requests_cache.clear()
headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                       ' AppleWebKit/537.36 (KHTML, like Gecko)'
                       ' Chrome/109.0.0.0 Safari/537.36'
    }
url='https://sc.chinaz.com/jianli/free.html'
response=requests.get(url=url,headers=headers).text
tree=etree.HTML(response)
load_paths=tree.xpath('//div/a/@href')
for url in load_paths:

    if url[0:4] != 'http':
        pass
    else:
        jl_response = requests.get(url=url,headers=headers).text
        fy_tree = etree.HTML(jl_response)
        url=fy_tree.xpath('//div/ul[@class="clearfix"]/li[3]/a/@href')
        if len(url) == 0:
            pass
        else:
            url=url[0]
            if url[0:4] != 'http':
                pass
            else:
                filename = url.split('/')[-1]
                jl_rar = requests.get(url,headers=headers).content
                with open(filename,'wb') as f:
                    f.write(jl_rar)
                    print(url,'was filished')

