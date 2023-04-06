import urllib.request
import urllib.parse
url='https://www.qceit.org.cn/bos/myguide.html?id=bos_myguide&function_name=%u8003%u524d%u5f15%u5bfc&d=2023220212337'
url='https://www.qceit.org.cn/bos/myguide.html?id=bos_myguide&function_name=%u8003%u524d%u5f15%u5bfc&d=2023220213926'
data={
    'id':'bos_myguide',
     'function_name':'%u8003%u524d%u5f15%u5bfc',
     'd':'2023220212337'

}
r=urllib.parse.urlencode(data)
print(r)
r=urllib.parse.quote(r)
print(r)