import urllib.request
import urllib.parse
url='https://s1.chu0.com/src/img/png/bc/bccc893273d24cff84db9e96b10368b6.png?imageView2/2/w/115/%7Cwatermark/3/text/54ix57uZ/font/5b6u6L2v6ZuF6buR/fontsize/341/fill/cmVk/dissolve/91/gravity/SouthEast/dx/6/dy/6/text/MkTmsb0=/font/5b6u6L2v6ZuF6buR/fontsize/341/fill/cmVk/dissolve/91/gravity/NorthWest/dx/6/dy/6/text/MTE1w5c=/font/5b6u6L2v6ZuF6buR/fontsize/341/fill/cmVk/dissolve/91/gravity/SouthWest/dx/6/dy/6/text/Y2FyMg==/font/5b6u6L2v6ZuF6buR/fontsize/341/fill/cmVk/dissolve/91/gravity/NorthEast/dx/6/dy/6//text/54ix57uZ572RIGFpZ2VpLmNvbQ==/font/5b6u6L2v6ZuF6buR/fontsize/300/fill/QmxhY2s=/dissolve/51/gravity/NorthWest/dx/10/dy/132&e=1735488000&token=1srnZGLKZ0Aqlz6dk7yF4SkiYf4eP-YrEOdM1sob:pFtmKygc1HhHFjp3GqcT7HBDjKo='
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                 ' AppleWebKit/537.36 (KHTML, like Gecko)'
                 ' Chrome/109.0.0.0 Safari/537.36'
}
r=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(r)
response=response.read()
print(response)
with open('car.png','wb') as f:
    f.write(response)
''.strip()