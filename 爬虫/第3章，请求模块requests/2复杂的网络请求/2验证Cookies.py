'''
通过验证Cookies模拟豆瓣登录
    在爬取某些数据时，需要进行网页的登录，才可以进行数据的抓取工作。Cookies登录就像很多网页
中的自动登录功能一样，可以让用户第二次登录时在不需要验证账号和密码的情况下进行登录。在使用requests
模块实现Cookies登录时，首先需要在浏览器的开发者工具页面中找到可以实现登录的Cookies信息，然后将
Cookies信息处理并添加到RequestCookieJar的对象中，最后将RequestCookieJar的对象作为网络
请求的Cookies参数发送网络请求即可。以获取豆瓣网页登录后用户名为例，具体步骤如下：
    1在谷歌浏览器中打开豆瓣网:https://www.douban.com/,按F12打开网络监视器，选择密码登录
账号：18973022769  密码：ww19850820    选择network,all,www.douban.com
    2在www.douban.com文件中找到头信息，
    3导入相应的模块，将'找到登录后网页中的Request Headers中的Cookie信息'以字符串形式保存，
然后创建RequestCookiesJar()对象并对Cookie信息进行处理，最后将处理后的RequestsCookieJar()
对象作为网络请求，实现网页的登录请求。代码如下：
import requests
from requests.cookies import RequestsCookieJar
from lxml import etree
cookies='ll="118283"; bid=na2bS5XhU5A; _pk_ses.100001.8cb4=*; __utma=30149280.1020769336.1674581440.1674581440.1674581440.1; __utmc=30149280; __utmz=30149280.1674581440.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; __utmv=30149280.16717; __yadk_uid=HLnUzT3YJ4I6migBGutdwQrbUIGDnsCa; __gads=ID=e9a12c9523e020c3-224f691364d90051:T=1674581424:RT=1674581424:S=ALNI_MbmaftUq2jLA-B-3UnANaDqIe8XpQ; __gpi=UID=00000bac0c32b5d1:T=1674581424:RT=1674581424:S=ALNI_MbCaBnnkQCNjuCey_pjCJ2jJUZudg; dbcl2="167179411:UKr7U1feubc"; ck=il7x; _pk_id.100001.8cb4=6763b662eb4edae0.1674581437.1.1674581762.1674581437.; __utmb=30149280.10.10.1674581440'
headers={'Host':'www.douban.com',
         'Referer':'https://www.hao123.com',
         'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
cookie_jar=RequestsCookieJar()
for cookie in cookies.split(';'):
    key,value=cookie.split('=',1)
    cookie_jar.set(key,value)
response=requests.get('https://www.douban.com/',headers=headers,cookies=cookie_jar)
if response.status_code == 200:
    html=etree.HTML(response.text)
    name=html.xpath('//*[@id="db-global-nav"]/div/div[1]/ul/li[2]/a/span[1]/text()')
    print(name[0])
'''
import requests
from requests.cookies import RequestsCookieJar
from lxml import etree
cookies='ll="118283"; bid=na2bS5XhU5A; _pk_ses.100001.8cb4=*; __utma=30149280.1020769336.1674581440.1674581440.1674581440.1; __utmc=30149280; __utmz=30149280.1674581440.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; __utmv=30149280.16717; __yadk_uid=HLnUzT3YJ4I6migBGutdwQrbUIGDnsCa; __gads=ID=e9a12c9523e020c3-224f691364d90051:T=1674581424:RT=1674581424:S=ALNI_MbmaftUq2jLA-B-3UnANaDqIe8XpQ; __gpi=UID=00000bac0c32b5d1:T=1674581424:RT=1674581424:S=ALNI_MbCaBnnkQCNjuCey_pjCJ2jJUZudg; dbcl2="167179411:UKr7U1feubc"; ck=il7x; _pk_id.100001.8cb4=6763b662eb4edae0.1674581437.1.1674581762.1674581437.; __utmb=30149280.10.10.1674581440'
headers={'Host':'www.douban.com',
         'Referer':'https://www.hao123.com',
         'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
cookie_jar=RequestsCookieJar()
for cookie in cookies.split(';'):
    key,value=cookie.split('=',1)
    cookie_jar.set(key,value)
response=requests.get('https://www.douban.com/',headers=headers,cookies=cookie_jar)
if response.status_code == 200:
    html=etree.HTML(response.text)
    name=html.xpath('//*[@id="db-global-nav"]/div/div[1]/ul/li[2]/a/span[1]/text()')
    print(name[0])