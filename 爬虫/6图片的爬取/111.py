import requests
url='http://s1.chu0.com/src/img/jpg/12/1201c391f06248c2bd97d1a9a8351857.jpg?imageMogr2/auto-orient/thumbnail/!234x234r/gravity/Center/crop/234x234/quality/85/&e=1735488000&token=1srnZGLKZ0Aqlz6dk7yF4SkiYf4eP-YrEOdM1sob:4ylVIRHwjrg8_gaNuQneE68Dvj4='
headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                       ' AppleWebKit/537.36 (KHTML, like Gecko)'
                       ' Chrome/109.0.0.0 Safari/537.36'
    }
r=requests.get(url,headers=headers).content
print(r)
with open('123.jpg', 'wb') as f:
    f.write(r)