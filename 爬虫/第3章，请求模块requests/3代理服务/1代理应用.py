'''
在爬取网页的过程中，经常会出现不久前爬取的网页现在无法爬取的情况，这是因为IP被访问网页服务器给屏蔽了。
此时，代理服务可以解决这一问题，如下：
import requests
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/109.0.0.0 Safari/537.36'}

proxy={'http':'http://117.88.176.38:3000',
       'https':'https://117.88.176.38:3000'}
try:
    response=requests.get('http://202020.ip138.com',headers=headers,proxies=proxy,verify=False,timeout=3)
    print(response.status_code)
except Exception as e:
    print('错误异常：',e)
'''

