import urllib.request    # 导入urllib.request模块
import urllib.error      # 导入urllib.error模块
try:
    # 向不存在的网络地址发送请求
    response = urllib.request.urlopen('http://site2.rjkflm.com:666/123index.html',timeout=0.1)
    print(response.status)
except urllib.error.HTTPError as error:    # 捕获异常信息
    print('状态码为：',error.code)                      # 打印状态码
    print('异常信息为：',error.reason)                  # 打印异常原因
    print('请求头信息如下：\n',error.headers)           # 打印请求头
except urllib.error.URLError as error:
    print('URLError.reason:',error.reason)