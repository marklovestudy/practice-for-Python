'''
例1:
请读取文件IP.txt 的数据，数据内容如下图显示：
文件中每一行存储一个 IP 地址，下列代码实现了读取数据，每次读取一行数据，都删除了行末的换行符，最后逆序输出文件中的每行 IP 地址，请你补全代码。
输出参考如下：
49.97.132.119
32.33.23.232
112.114.44.44
IP . txt - Notepad
File Edit Format View Help
112.114.44.44
32.33.23.232
49.97.132.119
实例1：
with open('IP.txt','r',encoding='utf-8') as f:
    list1 = f.readlines()
print(list1)
for i in range(0,len(list1)):
    list1[i] = list1[i].strip()
print(list1)
for i in range(len(list1)-1,-1,-1):
    print(list1[i])
f.close()

小文的运动时间数据存储在文件“ sportcsv ”中，数据内容如下图显示：下列代码实现了读取数据，求和并统计个数，输出平均时长，并保留2位小数，请你补全代码。
时长
47
41
31

例2：
import csv
with open('sport.csv','r',encoding='utf-8') as f:
    rows = list(csv.reader(f))
    print(rows)
    s = 0
    c = 0
    for row in rows[1:]:
        s += eval(row[0])
        c = c + 1
print(round(s/c,3))     #第二个参数是保留几位小数的意思

例3:
请读取文件 subways . csv 的数据，数据内容如下图显示下列代码实现了读取“学号”和“身高”信息，
输出“身高”达到120的学号，请你补全代码。
学号
YZ07    116
SZ19    117
YZ02    123
CZ31    122
BZ20    112
TC03    115
SZ11C715    127
YZ22    114
2X      118
SZ38    112


例3：
import csv
with open('subways.csv','r',encoding='utf-8') as f:
    rows = list(csv.reader(f))      #读出来的每行为这个列表的一个元素，并且每行都是一个列表元表，这个列表元表的元表是这行的每列信息。
    print(rows)
    s = 0
    for row in rows[1:]:
        if int(row[1]) >= 120:
            print(row[0])
'''
import csv
with open('sport.csv','r',encoding='utf-8') as f:
    rows = list(csv.reader(f))
    print(rows)
    s = 0
    c = 0
    for row in rows[1:]:
        s += eval(row[0])
        c = c + 1
print(round(s/c,3))     #第二个参数是保留几位小数的意思