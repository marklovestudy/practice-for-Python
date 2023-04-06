'''
    验证请求
    在访问页面时，可能会出现用户名和密码后才可以访问
    填写auth参数实现验证请求功能
    requests模块自带了验证功能，只需要在请求方法中填写auth参数，该参数的值是一个带有验证参数
(用户名与密码)的HTTPBasicAuth对象。代码如下：

'''
import requests
from requests.auth import HTTPBasicAuth
from lxml import etree
url='https://www.douban.com/'
headers={'Host':'www.douban.com',
         'Referer':'https://www.hao123.com',
         'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
ah=HTTPBasicAuth('18973022769','ww19850820')
response=requests.get(url=url,auth=ah,headers=headers)
if response.status_code == 200:
    print(response.text)
