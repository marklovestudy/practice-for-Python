# f=open('book.txt','w',encoding='utf=8')
# f.write(input('请输入要保存的信息：'))
# f.close()
# #请读取文件，book.txt的内容，然后删除所有的标点符号和数字。
# # 把修改后的内容存在文件book1.txt里面。
f=open('abc.txt','r',encoding='utf-8').read()
s= set()
for i in f:
    if not i.isalpha():
        s.add(i)
for i in f:
    if i in s:
        f=f.replace(i,'')
fo=open('book.txt','w+',encoding='utf-8')
fo.write(f+'\n')        #w和w+
fo.write('终于统计完了')
v=fo.read()
print(v)
#请保留文章中所有的中文字符，其它的全删除
# 最小值：u'\u4e00'    最大值：u'\u9fa5'
# if u'\u4e00'<=i<=u'\u9fa5':