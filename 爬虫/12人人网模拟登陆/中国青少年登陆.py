import requests
import requests_cache
from lxml import etree
import chaojiying
requests_cache.install_cache()
requests_cache.clear()
headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                       ' AppleWebKit/537.36 (KHTML, like Gecko)'
                       ' Chrome/109.0.0.0 Safari/537.36'
    }
url='https://www.qceit.org.cn/bos/default.html'
response=requests.get(url=url,headers=headers).text
tree=etree.HTML(response)
url_code='https://www.qceit.org.cn/calldata/calldata.aspx?g=ddd05678-bb76-7f1b-0075-13a0ccff32ec&datatype=getverifycodeimage&d=2023220205610'
image_code=requests.get(url=url_code,headers=headers).content
with open('image.jpg','wb') as f:
    f.write(image_code)
chaojiying = chaojiying.Chaojiying_Client('18973022769', 'mark123456', '944571')	#用户中心>>软件ID 生成一个替换 96001
# im = open('img.png', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
image_code=chaojiying.PostPic(image_code, 1902)['pic_str']
url_post='https://www.qceit.org.cn/calldata/calldata.aspx?datatype=logincheck'
data={
    '_usrename':'440402200812129313',
    '_userpassword':'wang123456',
    'logincheckcode':image_code
}
print(image_code,type(image_code))
response=requests.post(url=url_post,headers=headers,data=data)
print(response.status_code)
with open('11.text','w',encoding='utf-8') as f:
    response.text.encode('utf-8')
    f.write(response.text)