'''
会话请求
    在实现获取某个登录后页面的信息时，可以使用设置Cookies的方式先实现模拟登录，然后再获取
登录后页面的信息内容。这样虽然可以成功地获取页面中的信息，但是比较烦琐。

实例：通过Session对象实现会话请求
    requests模块中提供了Session对象，通地该对象可以实现在同一会话内发送多次网络请求的功能，
这相当于在浏览器中打开了一个新的选项卡，此时再获取登录后页面中的数据时，可以发送两次请求，第一
次发送登录请求，而第二次请求就可以在不登录的情况下获取登录后的页面数据。示例代码如下：
import requests
url='https://www.baidu.com'
data={'User-Agent':123}
s=requests.session()
response1=s.post(url,data=data)
response2=s.get(url)
print('登陆信息：',response1.text)
response2.encoding='utf-8'
print('登陆后页面信息如下：',response2.text)
'''
import requests        # 导入requests模块
# 原理：使用同一个对象获取，分别从这个对象读取不同的页面信息
s = requests.Session()  # 创建会话对象
data={'username': 'LiBiGor', 'password': '123456'}  # 创建用户名、密码的表单数据
# 发送登录请求
response_1 = s.post('http://site.XXXX.com:8001/index/checklogin.html',data=data)
response_2 = s.get('http://site.XXXX.com:8001')   # 发送登录后页面请求
print('登录信息：',response_1.text)                # 打印登录信息
print('登录后页面信息如下:\n',response_2.text)    # 打印登录后的页面信息