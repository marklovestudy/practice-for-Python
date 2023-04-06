'''
很多人想要使用ip，有很多方式，比如我们去找免费的，当然这种方式获取的ip基本上很多人都在使用，效果并不稳定，
或者我们还可以付费去使用，ip的使用期间只有自己在使用，譬如在收费的期间这个ip地址属于购买者，如果对购买ip很感兴趣的话，可以来看下。
获取ip的几种方式：
1、选择当地的运营商专线合作业务，从而获取固定公网IP；如果仅仅只是需要固定IP可以考虑运营商的合作代理商。
2、自架服务器：优点是IP质量好，IP时效和IP数量自己可以调节；缺点是价格贵，还要培养专业的运维人员。
3、免费代理IP：优点是不花钱；缺点是稳定性堪忧，数量也无法满足中大量规模的使用，而且要花费大量时间进行筛选，十分费事。
4、单台拨号服务器抓取：优点是IP质量好；缺点是无法多线程操作，工作效率太低。
5、使用HTTP代理IP：优点IP数量大，质量好，价格便宜；缺点是市面品牌众多，难以选择适用自己的一款。
长效ip、短效ip，动静态ip都有，支持免费试用，芝麻HTTP代理拥有全国数百所自建机房，安全稳定、海量资源、登录即可免费试用：
芝麻HTTP官网：高匿HTTP代理IP,SOCKS5代理IP,360天IP去重服务


'https://www.dieniao.com/     账号：18973022769        密码：ww19850820
获取免费的代理IP，为了避免被访问的服务实施封锁IP的操作，我们每发一次请求更换一次IP，从而降低被发现的风险。
其实在获取免费的代理IP之前，需要先找到提供免费代理IP，然后通过爬虫技术将大量的代理IP提取并保存在文件当中。
以某免费代理IP网页为例，代码如下：

注：error:ModuleNotFoundError: No module named 'openpyxl'
遇到这样的错误是因为我们在安装openpyxl的时候，所用的Python版本为3.9以下不支持所导致。
执行命令pip install openpyxl
'''
import requests
from lxml import etree
import pandas as pd
ip_list=[]
def get_ip(url,headers):
    response = requests.get(url,headers=headers)
    response.encoding='utf-8'
    if response.status_code == 200:
        html =etree.HTML(response.text)
        print(html)         ###
        li_all=html.xpath('//li[@class="f-list col-lg-12 col-md-12 col-sm-12 col-xs-12"]')
        for i in li_all:
            ip = i.xpath('span[@class="f-address"]/text()')[0]      #获取IP
            port=i.xpath('span[@class="f-port"]/text()')[0]         #获取端口
            ip_list.append(ip+':'+port)

hearders={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/109.0.0.0 Safari/537.36'}


if __name__=='__main__':
    ip_table=pd.DataFrame(columns=['ip'])       #创建临时表格数据
    for i in range(1,5):
        #获取免费代理IP的请求地址：
        url='https://www.dieniao.com/FreeProxy/{page}.html'.format(page=i)
        get_ip(url,hearders)
    ip_table['ip']=ip_list
    #生成xlsx文件
    ip_table.to_excel('ip.xlsx',sheet_name='data')