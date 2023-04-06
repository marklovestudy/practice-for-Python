'''
小电影url:https://v.qq.com/x/cover/prre4qvadyzdhr4/s0017hncfts.html?ptag=douban.cartoon
        https://v.qq.com/x/cover/prre4qvadyzdhr4/n00174zsq3r.html?ptag=douban.cartoon
        https://otheve.beacon.qq.com/analytics/v2_upload?appkey=JS0081LY3JY6J3
'''
import requests
url='https://v.qq.com/x/cover/prre4qvadyzdhr4/q001797o328.html'
headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                       ' AppleWebKit/537.36 (KHTML, like Gecko)'
                       ' Chrome/109.0.0.0 Safari/537.36'
    }
response=requests.get(url=url,headers=headers)
response=response.content
print(response)
with open('xiao.mp4','wb') as f:
    f.write(response)