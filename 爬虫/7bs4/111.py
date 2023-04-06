from bs4 import BeautifulSoup
f=open('t1.text','r',encoding='utf-8')
soup=BeautifulSoup(f,'lxml')
# print(soup.meta)
# print(soup.find('meta'))
# print(soup.find('div',class_="site-logo-img"))
# print(soup.find_all('a'))
print(soup.select('head>link')[0])
print(soup.select('head>link')[0]['rel'])