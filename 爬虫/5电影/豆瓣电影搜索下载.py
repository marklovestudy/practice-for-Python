"""
分析：打开https://movie.douban.com/
    先用GET请求首页数据https://pagead2.googlesyndication.com/getconfig/sodar?sv=200&tid=gda&tv=r20230124&st=env
                    https://m.douban.com/rexxar/api/v2/movie/36186448/verify_users?start=0&count=2&ck=il7x
    电影ajax请求数据地址：https://movie.douban.com/j/search_subjects?type=movie&tag=热门&page_limit=50&page_start=0
    电视剧ajax请求数据地址：https://movie.douban.com/j/search_subjects?type=tv&tag=热门&page_limit=50&page_start=0      #获取电影和相关属性
                        https://movie.douban.com/j/subject_abstract?subject_id=26647087
                        https://movie.douban.com/j/subject_abstract?subject_id=35465232
                        https://movie.douban.com/j/subject_abstract?subject_id=36134370
"""
import requests
import json
headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                       ' AppleWebKit/537.36 (KHTML, like Gecko)'
                       ' Chrome/109.0.0.0 Safari/537.36'
    }
url1 = 'https://movie.douban.com/j/search_subjects?'
url2 = 'https://movie.douban.com/j/subject_abstract?'
data1 = {
        'type' : 'tv',
        'tag' : '热门',
        'page_limit' : str(50),
        'page_start' : str(0),
    }
data2 = {
'subject_id': '26647087',
}
def find_TV(url,data,headers) :
    # 1确定访问对象
    # url=url
    # data=data
    # headers=headers
    # 2发起请求
    response = requests.get(url=url, params=data, headers=headers)
    # 3获取数据
    response = response.json()
    # 4保存数据
    with open('tv.json', 'w', encoding='utf-8') as f :
        json.dump(response, f, ensure_ascii=False)

def look_TV(url,id_list,headers) :
    global data2
    # 1确定访问对象
    # url=url
    # data=data
    # headers=headers
    # 2发起请求
    # 3获取数据
    # 4保存数据
    with open('tvs.json', 'w+', encoding='utf-8') as f :
        for i in id_list:
            data2['subject_id']=i
            response = requests.get(url=url, params=data2, headers=headers)
            response = response.json()
            json.dump(response, f, ensure_ascii=False)

def dq_data(file):
    tv_id_list=[]
    with open(file,'r',encoding='utf-8') as f:
        tv_dict=json.load(f)
        tv_list=tv_dict['subjects']
        for i in tv_list:
            tv_id_list.append(i['id'])
    return tv_id_list
find_TV(url1,data1,headers)
id_list=dq_data('tv.json')
look_TV(url2,id_list,headers)


