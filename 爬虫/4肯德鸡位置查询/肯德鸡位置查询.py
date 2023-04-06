import requests
import json
#确定访问对象
url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

city=input('what is the city you want to find:')
param={
'cname': '',
'pid': '',
'keyword': city,
'pageIndex': '1',
'pageSize': '10',
}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                 'AppleWebKit/537.36 (KHTML, like Gecko)'
                 ' Chrome/109.0.0.0 Safari/537.36'
}
#2发起请求
response=requests.post(url=url,params=param,headers=headers)

#3获取数据
response=response.text
print(response)

#数据存取：略
filename=city+'.text'
with open(filename,'w',encoding='utf-8') as f:
    f.write(response)