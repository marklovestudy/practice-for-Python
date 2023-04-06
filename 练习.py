'''

'''
import urllib.request
import urllib.parse

url="https://s1.chu0.com/src/img/png/7d/7d041ef577b6465699c37f691a45097b.png?imageMogr2/auto-orient/thumbnail/!88x132r/gravity/Center/crop/88x132/quality/85/%7Cwatermark/3/image/aHR0cHM6Ly9zMS5haWdlaS5jb20vd2F0ZXJtYXJrLzYwLTIucG5nP2U9MTczNTQ4ODAwMCZ0b2tlbj1QN1MyWHB6ZnoxMXZBa0FTTFRrZkhON0Z3LW9PWkJlY3FlSmF4eXBMOnpYaVVCU1Y3SmNxRUUtUTZmTkdGOHVLZ3l2bz0=/dissolve/20/gravity/NorthWest/dx/29/dy/66/ws/0.0/wst/0&e=1735488000&token=1srnZGLKZ0Aqlz6dk7yF4SkiYf4eP-YrEOdM1sob:hlpFE8KTH1uRVOVi1ds5YAZOeeU="
data=bytes(urllib.parse.urlencode({'py':345}),encoding='utf-8')
r=urllib.request.Request(url=url,data=data,method='POST')
response=urllib.request.urlopen(r)
with open('jieta.png','wb') as f:
    f.write(response.read())