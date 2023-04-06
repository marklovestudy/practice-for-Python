'''
若网络请求成功表示可用。否则表示不可用：

'''
import requests
import pandas
from lxml import etree
ip_table=pandas.read_excel('ip.xlsx')
ip=ip_table['ip']
hearders={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/109.0.0.0 Safari/537.36'
}
for i in ip:
    proxies={'http':'http://{ip}'.format(ip=i),
             'https':'https://{ip}'.format(ip=i),}
    try:
        response=requests.get('http://www.baidu.com/',headers=hearders,proxies=proxies,timeout=2)
        if response.status_code==200:
            response.encoding='utf-8'
            html=etree.HTML(response.text)
            info=html.xpath('/html/dody/p[1]//text()')
            print(info)
    except Exception as e:
        print(e)