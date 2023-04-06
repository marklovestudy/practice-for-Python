import requests
from lxml import etree
url='https://www.liankexue.cn/examQuestions?type=0&id=413&category=2&categoryid=29'
hearders={
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                 ' AppleWebKit/537.36 (KHTML, like Gecko)'
                 ' Chrome/97.0.4692.71 Safari/537.36'
}
response=requests.get(url=url,headers=hearders).text
tree=etree.HTML(response)
path=tree.xpath('//*[@id="app"]//.text()')
print(path)




