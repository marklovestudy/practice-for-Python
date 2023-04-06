import urllib.request
import urllib.parse
url='https://wkstatic.bdimg.com/static/ndpcwenku/static/ndsula/js/amd.min/LibAllCommon/index.LibAllCommon.750342e6.amd.min.js'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                 ' AppleWebKit/537.36 (KHTML, like Gecko)'
                 ' Chrome/109.0.0.0 Safari/537.36'
}
r=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(r)
response=response.read().decode('')
print(response)
with open('zl.text','w') as f:
    f.write(response)