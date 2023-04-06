"""
一、lxml库简介
        lxml库是python的第三方库，安装方式也是十分简单，这里就不多赘述。
        而lxml库的特点就是简单和易上手，并且解析大型文档（特指xml或html文档）
        的速度也是比较快的，因此写爬虫解析网页的时候它也是我们的一个不错的选择。

    安装：1但是安装lxml有点麻烦，因为依赖关系，如果直接使用easy_install或者pip安装，会报gcc错误。(先联网安装:pip install lxml)
        2在https://pypi.python.org/pypi/lxml找到相匹配的版本，下载好。
        3把下载的文件lxml-4.9.2-pp38-pypy38_pp73-win_amd64放在对应的路径python_lxml文件夹中。
        4pip install lxml-4.9.2-pp38-pypy38_pp73-win_amd64

二、初始化
使用lxml库的第一个步骤永远是初始化，只有初始化之后我们才可以去使用它的语法。
初始化方法如下：
html = etree.HTML(text)
1>参数：
text ：html内容的字符串
2>返回值：
html :  一个lxml库的对象

三、xpath（lxml）语法讲解
也许你会惊讶，说我们不是在讲解lxml库吗？为什么这里写的是xpath语法？好吧，其实我忘记说了，lxml库的语法就是基于xpath语法来的，所以会了xpath语法，自然就会了lxml语法，xpath语法在我们这个爬虫系列的第一部分就讲过了，忘了的同学可以去看看。

而且观察返回的结果，发现大部分返回的都是以列表的形式返回的结果，这一点请注意。

1>语法1：寻找节点

语法	含义
nodename(节点名字)	直接根据写的节点名字查找节点,如：div
//	在当前节点下的子孙节点中寻找,如：//div
/	在当前节点下的子节点中寻找,如：/div
.	代表当前节点（可省略不写，就像我们有时候写的相对路径），如：./div
..	当前节点的父节点，如：../div
实例：
from lxml import etree

text = '''
<body>
    <div>这时测试的div</div>
    <div>
        <div>
            这是嵌套的div标签
            <p>
                这时嵌套的p标签
            </p>
        </div>
    </div>
    <p>这时测试的p</p>
</body>
'''

html = etree.HTML(text)
result = html.xpath('//div')  # 使用xpath语法,一是在子孙节点中寻找，二是寻找div的标签
print(result)
# 结果：
# [<Element div at 0x1e4cadbf608>, <Element div at 0x1e4cae512c8>, <Element div at 0x1e4cae51348>]

首先，说明下lxml如何使用xpath语法：
使用方法就是对初始化的对象调用xpath(str)方法即可，这里参数为传入的xpath语法字符串。
其次，分析下上面的代码：
首先，我们初始化一个html对象，然后调用在此基础上调用xpath语法，其中传入的参数为：//div，
意思是寻找其中的div标签。然后我们观察text字符串中的html代码，可以看见，里面总共只有三个div标签，符合结果。
（div标签是成对出现，一组为：<div></div>）
from lxml import etree

text = '''
<body>
    <div>这时测试的div</div>
    <div>
        <div>
            这是嵌套的div标签
            <p>
                这时嵌套的p标签
            </p>
        </div>
    </div>
    <p>这时测试的p</p>
</body>
'''

html = etree.HTML(text)
result = html.xpath('/html/body/div')
print(result)
#结果：
#[<Element div at 0x1ea38b7f4c8>, <Element div at 0x1ea38c11188>]

首先，说明下lxml库的一个功能：补全与完善功能。
即我们传入的html代码不是标准的html代码，因为标准的html代码结构如下。
#标准结构
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
 <!--主题代码 -->
</body>
</html>

虽然我们传入的不是完整结构，但是lxml会在一定程度上完善我们的html代码，尽量使它变为标准的结构。
那么如何查看这个事实呢？只需要调用etree.tostring(html)结果。如下：
from lxml import etree

text = '''
<body>
    <div>这时测试的div</div>
    <div>
        <div>
            这是嵌套的div标签
            <p>
                这时嵌套的p标签
            </p>
        </div>
    </div>
    <p>这时测试的p</p>
</body>
'''

html = etree.HTML(text)
result = etree.tostring(html)
print(result)
#结果如下,中文没有正常显示,但是结构是正确的
'''
<html><body>
    <div>&#36825;&#26102;&#27979;&#35797;&#30340;div</div>
    <div>
        <div>
            &#36825;&#26159;&#23884;&#22871;&#30340;div&#26631;&#31614;
            <p>
                &#36825;&#26102;&#23884;&#22871;&#30340;p&#26631;&#31614;
            </p>
        </div>
    </div>
    <p>&#36825;&#26102;&#27979;&#35797;&#30340;p</p>
</body>
</html>
'''

其次，分析下代码的结果。我们这里传入的xpath语法为：/html/body/div 。这样我们首先获取了html标签。
在获取的了html标签内的body标签，而属于body内的子节点的div总共有两个。故结果打印两个标签。
2>语法2：筛选
有时候单纯的选择还不够，因为我们有时候需要的信息只在某一种标签中的某一个标签中，如一个网页中有很多的
div标签，但是只有拥有class="hello"的属性的标签才具有我们需要的信息。因此，掌握一些筛选的方法是必须的事情。
重要说明：
当我们使用筛选时，筛选的方法都是包含在[]（中括号）中的。

方法集合一：属性筛选
方法名\符号	作用
@	获取属性或者筛选属性,如：@class
contains	判断属性中是否含有某个值（用于多值判断），如：contains(@class,'hello')
        属性筛选示例：
from lxml import etree

text = '''
<div class="hello">
    <p>Hello,this is used to tested</p>
</div>
<div class="hello test hi">
    <div>
        <div>你好，这是用于测试的html代码</div>
    </div>
</div>
<div class="button">
    <div class="menu">
        <input name="btn" type="button" value="按钮" />
    <div>
</div>
'''

#初始化
html = etree.HTML(text)
#根据单一属性筛选

#筛选出class="hello"的div标签
hello_tag = html.xpath('//div[@class="hello"]')  #注意筛选的方法都是在中括号里面的
print(hello_tag) #结果为： [<Element div at 0x2ba41e6d088>]，即找到了一个标签，符合条件

#找出具有name="btn"的input标签
input_tag = html.xpath('//input[@name="btn"]')
print(input_tag) #结果为：[<Element input at 0x1751d29df08>]，找到一个input标签，符合条件

#筛选出具有class="hello"的div标签
hello_tags = html.xpath('//div[contains(@class,"hello")]')
print(hello_tags) #结果为：[<Element div at 0x1348272d248>, <Element div at 0x1348272d6c8>]，即找到了两个div标签，符合条件

方法集合二：按序选择
有时候我们会有这样的需求，我们爬取的内容是一个table标签（表格标签），或者一个ul（标签），
了解过html的应该都知道这样的标签，内部还有很多标签，比如table标签里就有tr、td等，ul里面就有li标签等。
对于这样的标签，我们有时候需要选择第一个或者最后一个或者前几个等。这样的方式我们也可以实现。
方法	作用
last()	获取最后一个标签
1	获取第一个标签
position() < = > num	筛选多个标签（具体见实例）
        按序选择示例：
这里需要注意这里的序是从1开始而不是从0开始
from lxml import etree

text = '''
<ul>
    <li>1</li>
    <li>2</li>
    <li>3</li>
    <li>4</li>
    <li>5</li>
    <li>6</li>
    <li>7</li>
    <li>8</li>
</ul>
'''

#初始化
html = etree.HTML(text)

#获取第一个li标签
first_tag = html.xpath('//li[1]') #令人吃惊，lxml并没有first()方法
print(first_tag)

#获取最后一个li标签
last_tag = html.xpath('//li[last()]')
print(last_tag)

#获取前五个标签
li_tags = html.xpath('//li[position() < 6]')
print(li_tags)

方法集合三：逻辑和计算
其实在写筛选时是可以加入逻辑方法的，如：and、or、>、>=等。当然也是可以写入一些计算方法的，如：+、-等。
下面给出示例：
from lxml import etree

text = '''
<ul>
    <li>1</li>
    <li>2</li>
    <li>3</li>
    <li>4</li>
    <li>5</li>
    <li>6</li>
    <li>7</li>
    <li>8</li>
</ul>
'''

#初始化
html = etree.HTML(text)

#获取第二个li标签，使用=判断
second_tag = html.xpath('//li[position() = 2]')
print(second_tag)

#获取第一个和第二个标签，使用or
tags = html.xpath('//li[position() = 1 or position() = 2]')
print(tags)

#获取前三个标签，使用<
three_tags = html.xpath('//li[position()<4]')
print(three_tags)

其余的方法使用思路都是一样的。会了一个其余的按照思路写即可。
3>语法3：获取属性和文本
好的，终于到这一步了（写得太累了，^_^）。我们寻找标签、筛选标签的最终目的就是获取它的属性或者文本内容。下面讲解获取文本和属性的方法。
方法	作用
@	获取属性或者筛选属性
text()	获取文本
        获取文本示例：

from lxml import etree
text = '''
<div class="hello">
    <p>Hello,this is used to tested</p>
</div>
<div class="hello test hi">
    <div>
        <div>你好，这是用于测试的html代码</div>
    </div>
</div>
<div class="button">
    <div class="menu">
        <input name="btn" type="button" value="按钮" />
    <div>
</div>
'''

#初始化
html = etree.HTML(text)
#获取第一个div中的p标签中的文本
content = html.xpath('//div/p/text()')    #注意使用text()的时机和位置
print(content)  #结果为：['Hello,this is used to tested']，仍然是以列表形式返回结果

#获取拥有第二个div中的文本,注意观察下面的不同之处
content_two = html.xpath('//div[position() = 2]/text()')
print(content_two)  #结果为： ['\n    ', '\n']

content_three = html.xpath('//div[position() = 2]//text()')
print(content_three)  #结果为： ['\n    ', '\n        ', '你好，这是用于测试的html代码', '\n    ', '\n']
#两者不同之处在于：一个为//，一个为/。我们知道//获取其子孙节点中的内容，而/只获取其子节点的内容。

获取属性示例：
from lxml import etree

text = '''
<div class="hello" name="test">
    <p>Hello,this is used to tested</p>
</div>
<div class="hello test hi">
    <div>
        <div>你好，这是用于测试的html代码</div>
    </div>
</div>
<div class="button">
    <div class="menu">
        <input name="btn" type="button" value="按钮" />
    <div>
</div>
'''

#初始化
html = etree.HTML(text)

#获取第一个div的name属性
first_div_class = html.xpath('//div[@class="hello"]/@name')
print(first_div_class)  #结果为：['test']

#获取input标签的name值
input_tag_class = html.xpath('//input/@name')
print(input_tag_class) #结果为：['btn']

lxml库的讲解差不多就到此为止了，至于更多的方法还是推荐查官方文档。因为有些方法确实不常用。

"""
