'''
/html/body/div/div[3]/div/div[1]/div[2]/div[2]/div[3]/div[5]/img
#input()   等待用户输入，然后将输入内容以字符变量的形式返回。
#v = input()  等待用户输入，然后将输入内容以字符变量的形式赋值给v
'''

import requests
import requests_cache
from lxml import etree
requests_cache.install_cache()
requests_cache.clear()
url='https://www.qceit.org.cn/bos/default.html'
hearder={
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                 ' AppleWebKit/537.36 (KHTML, like Gecko)'
                 ' Chrome/97.0.4692.71 Safari/537.36'
}
response=requests.get(url=url,headers=hearder).text
tree=etree.HTML(response)
image_code=tree.xpath('//div[@style="overflow: hidden; zoom: 1; text-align: left; margin-top: 5px;"]/img/@src')

print(image_code)
