import requests
import requests_cache
from lxml import etree
import chaojiying
from requests.auth import HTTPBasicAuth
#下载验证码图片
requests_cache.install_cache()
requests_cache.clear()
headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                       ' AppleWebKit/537.36 (KHTML, like Gecko)'
                       ' Chrome/109.0.0.0 Safari/537.36'
    }
url='https://www.qceit.org.cn/bos/default.html'
page_text=requests.get(url=url,headers=headers).text
tree=etree.HTML(page_text)
image_code_url='https://www.qceit.org.cn/calldata/calldata.aspx?g=638489f9-51a0-6798-658e-1ba5bad9b727&datatype=getverifycodeimage&d=20232322326'
image_code=requests.get(url=image_code_url,headers=headers).content
with open('codema.jpg','wb') as f:
    f.write(image_code)
chaojiying = chaojiying.Chaojiying_Client('18973022769', 'mark123456', '944571')	#用户中心>>软件ID 生成一个替换 96001
# im = open('img.png', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
image_code=chaojiying.PostPic(image_code, 1902)
print(image_code)


