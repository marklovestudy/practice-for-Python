import requests
#1确定被访问的网络地址url
url='https://www.sogou.com/web'
kw=input('your want to get')
param={
    'query':kw
}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
#2发起访问请求
response=requests.get(url,params=param,headers=headers)
#3获取数据
page_text=response.text
filename=kw+'.html'
#4保存数据
with open(filename,'w',encoding='utf-8') as f:
    f.write(page_text)