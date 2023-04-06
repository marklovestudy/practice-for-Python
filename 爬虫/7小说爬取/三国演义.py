import requests
import time
from bs4 import BeautifulSoup
if __name__ == '__main__':
    url='http://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                       ' AppleWebKit/537.36 (KHTML, like Gecko)'
                       ' Chrome/109.0.0.0 Safari/537.36'
    }
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    response=response.text
    #从首页返回数据中解析出章节标题和详情页面的URL
    soup=BeautifulSoup(response,'lxml')
    res=soup.select('.book-mulu>ul>li>a')
    #print(res)
    f = open('sangguo.text', 'w', encoding='utf-8')
    for i in res:
        url='http://www.shicimingju.com'+i['href']
        filename=i.string+'.text'
        #获取当前页面的数据
        response=requests.get(url,headers=headers)
        response.encoding='utf-8'
        response=response.text
        #解析当前页面要的数据内容
        detail_soup = BeautifulSoup(response,'lxml')
        div_tag=detail_soup.find('div',class_='chapter_content')
        content=div_tag.text            #所有内容
        # print(content)
        f.write(filename+':'+content+'\n')
        print(filename,'下载完毕')
    f.close()