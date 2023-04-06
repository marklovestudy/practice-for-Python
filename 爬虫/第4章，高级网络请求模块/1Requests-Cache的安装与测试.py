'''
Requests-Cache模块是requests模块的一个扩展功能，为requests模块提供缓存支持，向一个URL发送请求时，
Requests-Cache会自动判断当前的请求是否产生了缓存，如果已经产生了缓存，就会从缓存中读取数据作为响应内容，
如果没有缓存，就会向服务器发送网络请求，获取服务器响应的内容，这样可以减少网络资源重复请求次数，相当于变向反爬。
安装：pip install requests-cache
'''
import requests_cache
version=requests_cache.__version__
print('模块板本：',version)
requests_cache.install_cache()