'''
time 模块下有很多函数可以转换常见日期格式。
>>> import time
>>> ticks = time.time()
>>> ticks
1663694244.206387
函数 time.time()用于获取当前时间戳，时间间隔是以秒为单位的浮点小数。
每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。

格式化时间：
根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是 asctime ():
>>> time.localtime(time.time())
time.struct_time(tm_year=2022, tm_mon=9, tm_mday=21, tm_hour=1, tm_min=23, tm_sec=17, tm_wday=2, tm_yday=264, tm_isdst=0)
>>> time.asctime(time.localtime(time.time()))
'Wed Sep 21 01:22:36 2022'

使用 time 模块的 strftime 方法来格式化日期：
#格式化成2016-03-20114539形式
>>> print(time.strftime("%Y-%m-%d %H:%M:%S ",time.localtime ()))
2022-09-21 01:28:10
＃格式化成 Sat Mar 282224242016形式
>>> print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
Wed Sep 21 01:30:41 2022
>>> timesleep ( secs )#推迟调用线程的运行， secs 指秒数

datetime 模块
日期时间模块 datetime 提供了与日期和时间有关的很多对象。
>>> import datetime
>>> d = datetime.date.today()
>>> d
datetime.date(2022, 9, 21)
>>> d.year
2022
>>> d.month
9
>>> d.day
21
>>> d=datetime.date(2022,3,31)-datetime.date(2022,1,1)
>>> d.days
89
>>> datetime.date.today()
datetime.date(2022, 9, 21)
>>> datetime.date.today().weekday()     #0-6代表周一到周日
2

time库模块介绍：
1 time()    从1970年1月1日到现在过去了多少秒
2 asctime() 显示格式：当前-星期几 几月几日 时分秒 年
3 ctime()   显示格式：星期几 几月几日 时分秒 年 ，注：参数传入一个秒，转为星期几 几月几日 时分秒 年
4 gmtime()  time.struct_time(tm_year=2022, tm_mon=12, tm_mday=17, tm_hour=5, tm_min=50, tm_sec=31, tm_wday=5, tm_yday=351, tm_isdst=0)
"""
'''