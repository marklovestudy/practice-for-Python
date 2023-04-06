'''
HTTPError类是URLError类的子类，主要用于处理HTTP请求所出现的异常，该类有以下三个属性：
code:返回HTTP状态码
reason：返回错误原因
headers：返回请求头

实例1：
import urllib.request    # 导入urllib.request模块
import urllib.error      # 导入urllib.error模块
try:
    # 向不存在的网络地址发送请求
    response = urllib.request.urlopen('http://site2.rjkflm.com:666/123index.html')
except urllib.error.URLError as error:    # 捕获异常信息
    print(error.reason)                    # 打印异常原因

实例2
import urllib.request    # 导入urllib.request模块
import urllib.error      # 导入urllib.error模块
try:
    # 向不存在的网络地址发送请求
    response = urllib.request.urlopen('http://site2.rjkflm.com:666/123index.html')
    print(response.status)
except urllib.error.HTTPError as error:    # 捕获异常信息
    print('状态码为：',error.code)                      # 打印状态码
    print('异常信息为：',error.reason)                  # 打印异常原因
    print('请求头信息如下：\n',error.headers)           # 打印请求头

实例3：
import urllib.request    # 导入urllib.request模块
import urllib.error      # 导入urllib.error模块
try:
    # 向不存在的网络地址发送请求
    response = urllib.request.urlopen('https://www.python.org/',timeout=0.1)
except urllib.error.HTTPError as error:    # HTTPError捕获异常信息
    print('状态码为：',error.code)                      # 打印状态码
    print('HTTPError异常信息为：',error.reason)         # 打印异常原因
    print('请求头信息如下：\n',error.headers)           # 打印请求头
except urllib.error.URLError as error:     # URLError捕获异常信息
    print('URLError异常信息为：',error.reason)
'''
import urllib.request    # 导入urllib.request模块
import urllib.error      # 导入urllib.error模块
try:
    # 向不存在的网络地址发送请求
    response = urllib.request.urlopen('http://site2.rjkflm.com:666/123index.html')
    print(response.status)
except urllib.error.HTTPError as error:    # 捕获异常信息
    print('状态码为：',error.code)                      # 打印状态码
    print('异常信息为：',error.reason)                  # 打印异常原因
    print('请求头信息如下：\n',error.headers)           # 打印请求头

