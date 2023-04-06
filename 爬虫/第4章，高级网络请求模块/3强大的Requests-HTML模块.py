'''
Requests-HTML模块是requests模块的亲兄弟，是同一个开发者所开发的。Requsts-HTML模块不仅包含了requests模块中的所有功能，
还增加了对JavaScript的支持、数据提取以及模拟真实浏览器等功能。
pip install requests-html
一、使用Requests-HTML模块实现网络请求：
1GET请求
from requests_html import HTMLSession
session=HTMLSession()
url='http://news.youth.cn/'
r=session.get(url)
print(r.html)
POST()请求
    在实现网络请求时，POST请求也是一种比较常见的请求方式，使用Requests-HTML实现POST请求与requests的实现方法
类似都需要单独设置表单参数data，不过它也是需要通过会话实例进行网络请求的发送，示例代码如下：
from requests_html import HTMLSession
session=HTMLSession()
data = {'user':'admin','password':123456}
r = session.post('http://httpbin.org/post',data=data)
if r.status_code == 200:
    print(r.text)

    从以上的运行结果中，不仅可以看到form所对应的表单内容，还可以看到User-Agent所对应的值并不是
像requests模块发送网络请求时所返回的默认值(python-requests/2.22.0),而是一个真实的浏览器请求
头信息，这与requests模块所发送的网络请求有着细小的改进。

3.修改请求头信息
    说到请求头信息，Requsets-HTML模块是可以通过指定headers参数来默认的浏览器请求头信息进行修
改的，修改请求头信息的关键代码如下：
headers={'User-Agent':123}
r=session.post(url,data=data,headers=headers)

4生成随机请求头
ua=UserAgent().random
r=session.get(url,headers={'User-Agent':ua})
print(r.text)

二、数据的提取
    以往使用requests模块实现爬虫程序时，还需要为其配置一个解析HTML代码的搭档。Requests-HTML
模块对此进行了一个比较大的升级，不仅支持CSS选择器还支持XPath的节点提取方式。
    1.CSS选择器
    CSS选择器中需要使用HTML的find()方法，该方法中包含5个参数，其语法格式与参数含义如下：
    find(selector:str='*',              #使用CSS选择器定位网页元素
        containing:_Containing=None,    #通过指定文本获取网页元素
        clean:bool=False,               #是否清除HTML中的<script>和<style>标签，默认为False表示不清除。
        first:bool=False,               #是否只返回网页中第一个元素，默认为False表示全部返回。
        _encoding:str=None)             #表示编码格式。
    2.XPath选择器
    XPath选择器同样需要使用HTML进行调用，该方法中有4个参数，其语法格式与参数含义如下：
    xpath(selector:str,                 #使用xpath选择器定位网页元素
        clean:bool=False,               #是否清除HTML中的<script>和<style>标签，默认为False表示不清除。
        first:bool=False,               #是否只返回网页中第一个元素，默认为False表示全部返回。
        _encoding:str=None)             #表示编码格式。

    3.爬取即时新闻
    学习了Requests-HTML模块中两种提取数据的函数后，以爬取'中国青年网'，即时新闻为例。数据提取的具体步骤如下：
        1输入：http://news.youth.cn/jsxw/index.htm
        2点击获取即时新闻网址：http://news.youth.cn/jsxw/202301/t20230127_14279410.htm
        3创建HTML会话与获取随机请求对象，然后对'即时新闻'首页发送请求代码如下：
from requests_html import HTMLSession,UserAgent
session=HTMLSession()
ua=UserAgent.random
r=session.get('http://news.youth.cn/jsxw/index.htm',headers={'user-agent':ua})
r.encoding='gb2312'
        4网络请求发送完成以后，需要通过请求状态码判断请求是否为200，如果是200则表示请求成功，
        然后根据数据定们位的标签分别获取'新闻详情url地址'以及新闻的发布时间，代码如下：
'''
from requests_html import HTMLSession,UserAgent
session=HTMLSession()
ua=UserAgent().random
r=session.get('http://news.youth.cn/jsxw/index.htm',headers={'user-agent':ua})
r.encoding='gb2312'

if r.status_code == 200:
    #获取所有class=tj3_1中的<li>标签
    li_all = r.html.xpath('.//ul[@class="tj3_1"]/li')
    for li in li_all:
        news_title = li.find('a')[0].text
        #获取新闻详情对应的地址
        news_href = 'http://news.youth.cn/jsxw' + \
                    li.find('a[href]')[0].attrs.get('href').lstrip('.')
        news_time = li.find('font')[0].text  # 获取新闻发布的时间
        print('新闻标题为：', news_title)  # 打印新闻标题
        print('新闻url地址为：', news_href)  # 打印新闻url地址
        print('新闻发布时间为：', news_time)  # 打印新闻发布时间