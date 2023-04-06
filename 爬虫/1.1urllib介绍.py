'''
urllib介绍：多个功能的子模块，具体内容如下：
    urllib.request:用于实现基本HTTP请求的模块
    urllib.error:异常处理模块，如果在发送网络请求时出现了错误，可以捕获异常进行异常的有效处理。
    urllib.parse:用于解析URL的模块
    urllib.robotparser:用于解析robots.txt文件，判断网站是否可以爬取信息。
'''
import urllib.request
import urllib.error
import urllib.parse
import urllib.robotparser
url='http://www.baidu.com'
rp = urllib.robotparser.RobotFileParser()
# rp.set_url("http://www.baidu.com/robots.txt")
# v1=rp.can_fetch("*", "https://www.baidu.com/s?wd=%E2%80%9C%E5%8D%9A%E9%B3%8C%E6%BC%94%E8%AE%B2%E2%80%9D%E9%87%91%E5%8F%A5&sa=fyb_n_homepage&rsv_dl=fyb_n_homepage&from=super&cl=3&tn=baidutop10&fr=top1000&rsv_idx=2&hisfilter=1")
# v2=rp.can_fetch("*","http://www.baidu.com")
rp.set_url("http://www.musi-cal.com/robots.txt")
v3=rp.can_fetch("*","http://www.musi-cal.com/")
# can_fetch(useragent, url)
# 如果允许 useragent 按照被解析 robots.txt 文件中的规则来获取 url 则返回 True。
# print(v1)
# print(v2)
print(v3)