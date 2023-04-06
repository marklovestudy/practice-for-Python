'''
使用urlopen()方法发送请求
    urllib.request模块提供了urlopen()方法，用于实现基本的HTTP请求，然后接收服务端所返回的响应数据。
    urlopen()方法的语法格式如下：
    urllib.request.urlopen(url,data=None,[timeout,]*,cafile=None,capath=None,cadefault=False,context=None)

    *url:需要访问网站的URL完整地址。
    *data:参数默认为None，通过该参数确认请求方式，如果是None,表示请求方式为GET，否则请求方式为POST，在发送POST请求时，
    参数data需要以字典形式的数据作为参数值，并且需要将字典类型的参数值转换为字节类型的数据才可以实现POST请求
    *timeout:以秒为单位，设置超时。
    *cafile、capath:指定一组HTTPS请求受信任的CA证书，cafile指定包含CA证书的单个文件，capath指定证书文件的目录。
    cadefault:CA证书默认值。
    *context：描述SSL选项的实例。
'''