'''
在使用Requests-Cache模块实现请求缓存时，只需要调用install_cache()函数即可，语法如下：
install_cache(
    cache_name: str = 'http_cache',                         #表示缓存文件名称，默认为cache
    backend: BackendSpecifier = None,                       #表示缓存存取机制，默认为NONE，表示默认使用sqlite进行存储
    expire_after: ExpirationTime = -1,                      #表示设置缓存的有效时间，默认为None，表示永久有效
    urls_expire_after: Dict[str, ExpirationTime] = None,    #同上
    allowable_codes: Iterable[int] = (200,),                #表示设置状态码：默认为200。
    allowable_methods: Iterable['str'] = ('GET', 'HEAD'),   #设置方法头文件，默认为GET，只有GET请求有缓存
    filter_fn: Callable = None,
    stale_if_error: bool = False,
    session_factory: Type[OriginalSession] = CachedSession, #表示设置缓存执行的对象，需要实现CachedSession类。
    **kwargs,                                               #如果缓存的存储方式为sqlite、mongo、redis数据库，该参数表示设置数据库的连接方式。
):

在使用install_cache()函数实现请求缓存时，一般情况下是不需要单独设置任何参数的，只需要使用默认参数即可。判断是否存在缓存的代码如下：

import requests
import requests_cache
requests_cache.install_cache()              #设置缓存
requests_cache.clear()                      #清除缓存
url='http://httpbin.org/get'
r=requests.get(url)                         #发送请求
print('是否有缓存：',r.from_cache)            #False表示不存在缓存
r=requests.get(url)                         #发送请求
print('是否有缓存：',r.from_cache)            #True表示存在缓存

    在发送网络请求爬取网页数据时，如果频繁地发送网络请求，后台服务器则会视为爬虫程序，此时将会采取反爬措施。
所以多次请求中要出现一定的时间间隔，设置延时是一个不错的选择。但是如果在第一次请求后已经生成了缓存，那么第
二次请求也就无需设置延时，对于此类情况Requests-Cache模块可以使用自定义钩子函数的方式，合理地判断是否需要
设置延时操作。代码如下：
import requests_cache
import time
requests_cache.install_cache()
requests_cache.clear()

#定义钩子函数
def make_throttle_hook(timeout=0.1):
    def hook(response,*args,**kwargs):
        print(response.text)
        if not getattr(response,'from_cache',False):
            print('等待',timeout,'秒')
            time.sleep(timeout)
        else:
            print('是否存在缓存：',response.from_cache)
        return response
    return hook

if __name__ == '__main__':
    requests_cache.install_cache()
    requests_cache.clear()
    s=requests_cache.CachedSession()
    s.hooks={'response':make_throttle_hook(2)}
    s.get('http://httpbin.org/get')
    s.get('http://httpbin.org/get')

以上运行结果可以看出，第一次请求时，有延时，后面的请求没有延时，并输出是否存在缓存。
说明：Requests-Cache模块支持4种不同的储存机制：分别是：memory,sqlite,mongoDB,redis,说明如下：
memory:以字典的形式缓存存储在内存当中，程序运行完以后缓存将被销毁
sqlite:将缓存存储在sqlite数据库中
mongoDB:将缓存存储在mongoDB数据库中
redis:将缓存存储在redis数据库中。
用backend指明即可，设置方式如下：
import requests_cache
requests_cache.install_cache(backend='memory')
requests_cache.install_cache(backend='sqlite')
requests_cache.install_cache(backend='mongoDB')
requests_cache.install_cache(backend='redis')

在设置存储机制为mongoDB与redis数据存时，需要提前安装对应的操作模块与数据库。安装模块命令如下：
pip install pymongo
pip install redis
'''
import requests_cache
requests_cache.install_cache(backend='memory')
requests_cache.install_cache(backend='sqlite')
requests_cache.install_cache(backend='mongoDB')
requests_cache.install_cache(backend='redis')