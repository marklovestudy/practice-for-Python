import requests
import json
#确定访问对象https://movie.douban.com/j/chart/top_list?type=24&interval_id=100:90&action=&start=20&limit=20
url='https://movie.douban.com/j/chart/top_list?'        #问号后的参数封装到data,如下：
param={
'type': '24',
'interval_id': '100:90',
'action':'',
'start':'0',
'limit':'20'
}
hearders={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                 ' AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/109.0.0.0 Safari/537.36'
}
#2发起请求：
response=requests.get(url=url,params=param,headers=hearders)

#3获取数据：
list_data=response.json()
response_list=json.loads(response.text)
print(list_data==response_list)
#4数据存取
filename=param['start']+'--'+str(eval(param['start'])+eval(param['limit']))+'.json'
with open(filename,'w',encoding='utf-8') as f:
    json.dump(list_data,f,ensure_ascii=False)