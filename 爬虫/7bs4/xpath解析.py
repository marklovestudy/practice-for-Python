'''
建议首选XPATH解析，应用范围广，
    - XPATH解析原理：from lxml import etree
        1.先建立一个etree对象，且将被解析的页面源码数据加载到etree对象之中
        2.通过调etree对象中的xpath()方法结合xpath表达式实现标签定位和内容的捕获
    - 环境安装：
        -pip install lxml
    - 如何实例化一etree对象
        -1.将本地的HTML文件源码数据加载到etree对象中。
            tree=etree.parse(filepath)
        -2.可以将网上获取的源码数据加载到该对象中.
            tree=etree.HTML('page_text')
        -3.xpath('xpath表达式')
            r=tree.xpath('/html/body/div')
            表达式讲解：
            /:表示一个层级
            //:表示多个层级：如：'/html//div'    如：'//div'       定位所有div
            属性定位：'//div[@class='属性名称']'    tag[@attrName="attrValue"]
            索引定位：'//div[@class='属性名称']/p[3]'         索引是从1开始的，和传统的0开始有差异。
            取文本：'//div[@class='属性名称']/p[3]/text()'       /text()获取直接文本，//text()获取非直系的所有文本。
            取属性：'//div[@class='属性名称']/p[3]/@str'      /@attrName： /@加属名

'''
