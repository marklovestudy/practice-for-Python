'''
#索引取值
>>> name = 'mark'
>>> name[2]
'r'
>>> name[0]
'm'
>>> name[3]
'k'
>>> name[1:3]
'ar'
>>> name[:3]
'mar'
>>> name[2:]
'rk'

#字符串的方法：
1find('a')左查找，找到指定字符的索引号
v1=txt.find('a')
2rfind('set')右查找，找到指定字符的索引号
v2=txt.rfind('set')
3capitalize()首字母大写
4title()标题化
5upper()全大写
6lower()全小写
txt = 'write book'
print(txt,type(txt))
v1=txt.capitalize()
v2=txt.title()
v3=txt.upper()
print(v1,'v1')
print(v2,'v2')
print(v3,'v3')
txt2='WSF kar'
v4=txt2.lower()
print(v4,'v4')
7,8,9,10，中，左，右，O填充
txt = 'mark'
v1=txt.center(20,'*')
v2=txt.ljust(20,'*')
v3=txt.rjust(20,'*')
v4=txt.zfill(20)
print(v1,'v1')
print(v2,'v2')
print(v3,'v3')
print(v4,'v4')
#创建文件
f = open('123.csv','w',encoding='utf-8')
f.write("file is either a text or byte string giving the name (and the path\n"
        "if the file isn't in the current working directory) of the file to\n"
        "be opened or an integer file descriptor of the file to be\n"
        "wrapped. (If a file descriptor is given, it is closed when the\n"
        "returned I/O object is closed, unless closefd is set to False.)")
f.close()
#打开文件
f = open('123.csv','r',encoding='utf-8')
txt = f.read()
print(txt,type(txt))
v1=txt.find('a')
v2=txt.rfind('set')
print(v1,v2)
print(txt[15:304])
'''
