'''
连接URL:urljoin()方法：
urllib.parse.urljoin(base,url,allow_fragments=True)
base:表示基础链接
url:表示新的链接
allow_fragments:可选参数，如果该参数设置为False，表示忽略fragment这部分内容，默认为True.
import urllib.parse
base_url='https://docs.python.org'      #定义基础链接
#第二参数不完整时
print(urllib.parse.urljoin(base_url,'3/library/urllib.parse.html'))
#第二参数完整时
print(urllib.parse.urljoin(base_url,'https://docs.python.org/3/library/urllib.parse.html#url-parsing'))
'''

import urllib.parse
base_url='https://docs.python.org'      #定义基础链接
#第二参数不完整时
print(urllib.parse.urljoin(base_url,'3/library/urllib.parse.html'))
#第二参数完整时
print(urllib.parse.urljoin(base_url,'https://docs.python.org/3/library/urllib.parse.html#url-parsing'))