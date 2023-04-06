'''
bs4只能用在python中
    - 数据解析的原理
        - 1.标签定位
        - 2.提取标签、标签属性中存储的数据值
    - bs4数据解析的原理:
        - 1.实例化一个BeautifulSoup对象，并且将页面源码数据加载到该对象中
        - 2.通过调用BeautifulSoup对象中相关的属性或者方法进行标签定位和数据提取
    - 环境安装:
    - pip install bs4
    - pip install lxml

    - 如何实例化BeautifulSoup对象:
    - from bs4 import BeautifulSoup - 对象的实例化:
    - 1.将本地的html文档中的数据加载到该对象中
        fp = open('./test.html','r',encoding='utf-8')
        soup =BeautifulSoup(fp,'lxml')
    - 2.将互联网上获取的页面源码加载到该对象中
        page_text = response.text
        soup = BeatifulSoup(page_text,'lxml')

    bs4的方法和属性
        - soup.tagName      #返回第一次出点tagName标签的内容
        - soup.find('div')  #返回第一次出点div的标签内容。相当于soup.tagName
        - soup.find('div',class_="site-logo-img")       #属性定位
        - soup.find_all('a')        #列表形式返回所有符合要求的标签，

        层级选择
        - soup.select('某种选择器：id,class,标签')      #返回一个列表
        - soup.select('.tang > ul > li > a ')[0]    #返回一个列表，层级标签，>表示一个层级，li a中间的空格表示多个层级。

        获取标签之间的文本数据：
        - soup.a.text/string/get_text()
        - text/get_text()：可以获取某一个标签中所有的文本内容。
        - string:只获取标签直系内容。

        获取标签中的属性值
        - soup.a['href']
'''
from bs4 import BeautifulSoup

fp=open('text.text','r',encoding='utf-8')
soup=BeautifulSoup(fp,'lxml')
print(soup.select('div > ul > li > a'))