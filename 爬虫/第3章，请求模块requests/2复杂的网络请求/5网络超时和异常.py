'''
演示网络超时与异常现象
    在访问一个网页时，如果该网页长时间未响应，系统就会判断该网页超时，无法打开网页。
    下面通过代码来模拟一个网络超时的现象，代码如下：
import requests
for a in range(50):
    try:
        response=requests.get('https://www.baidu.com/',timeout=0.1)
        print(response.status_code)
    except Exception as e:
        print('异常'+str(e))

识别网络异常的分类
    针对网络异常信息，requests模块同样提供了三种常见的网络异常类捕获异常
代码如下：


'''
import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException
for i in range(50):
    try:
        response=requests.get('https://www.baidu.com/',timeout=0.1)
        print(response.status_code)
    except ReadTimeout:                         #超时
        print('timeout')
    except HTTPError:                           #HTTP异常
        print('httperror')
    except RequestException:                    #请求异常
        print('RequestException')