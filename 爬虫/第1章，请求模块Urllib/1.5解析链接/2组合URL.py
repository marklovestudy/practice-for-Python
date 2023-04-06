'''
一，组合URL二种方法：urlunparse(),urlunsplit()
urlunparse()实例：
import urllib.parse
list_url=['https','docs.python.org','/3/library/urllib.parse.html','','','']
tuple_url=('https','docs.python.org','/3/library/urllib.parse.html','','','')
dict_url={'scheme':'https','netloc':'docs.python.org','path':'/3/library/urllib.parse.html','params':'','query':'','fragment':''}
print('组合列表：',urllib.parse.urlunparse(list_url))
print('组合元组：',urllib.parse.urlunparse(tuple_url))
print('组合字典：',urllib.parse.urlunparse(dict_url.values()))

urlunsplit()实例：不需要传入params参数。
import urllib.parse
list_url=['https','docs.python.org','/3/library/urllib.parse.html','','']
tuple_url=('https','docs.python.org','/3/library/urllib.parse.html','','')
dict_url={'scheme':'https','netloc':'docs.python.org','path':'/3/library/urllib.parse.html','query':'','fragment':''}
print('组合列表：',urllib.parse.urlunsplit(list_url))
print('组合元组：',urllib.parse.urlunsplit(tuple_url))
print('组合字典：',urllib.parse.urlunsplit(dict_url.values()))
'''
import urllib.parse
list_url=['https','docs.python.org','/3/library/urllib.parse.html','','']
tuple_url=('https','docs.python.org','/3/library/urllib.parse.html','','')
dict_url={'scheme':'https','netloc':'docs.python.org','path':'/3/library/urllib.parse.html','query':'','fragment':''}
print('组合列表：',urllib.parse.urlunsplit(list_url))
print('组合元组：',urllib.parse.urlunsplit(tuple_url))
print('组合字典：',urllib.parse.urlunsplit(dict_url.values()))