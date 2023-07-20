scores=[['张三',56,67,78],['李四',58,87,48],['王五',36,97,78],['赵六',86,57,78]]
#1创建一个空字典
#2把名字和总分加入字典
# dict1={}
# dict1['a']=123   #直接加入内容dict1变成：{'a'：123}
# sc={}
# #2把名字和总分加入字典
# for i in scores:
#     print(i)
#     k=i[0]              #键
#     v=sum(i[1:])       #值        序列常用函数len ,min,max,sum
#     sc[k]=v
# print(sc)

d1={}
#1请在d1里添加键值对'chinese':88,'math':98,'english':88
d1['chinese']=88
d1['math']=98
d1['english']=88
#2请访问d1中的'chinese'和'math'的成绩。
print(d1['chinese'])
print(d1['math'])
#3请计算d1中的总分m，并在字典尾部添加一个键值对'all':m
m=d1['chinese']+d1['math']+d1['english']
d1['all']=m
print(d1)
#4请在d1中加入'综合':255,并更新总分。
d1['综合']=255
d1['all']=d1['all']+d1['综合']
#5请结合分数，帮助学生选择一所最恰当的大学{'A大学':480,'B大学':520,'C大学'：550,'D大学':580,'E大学':630,'F大学'：680}
schools={'A大学':480,'B大学':520,'C大学':550,'D大学':580,'E大学':630,'F大学':680}
print(d1)
maxsc=0
for i in schools:       #遍历所有的大学，遍历默认遍历键
    if d1['all']>schools[i]:             #i指的是大学名字，找出所有满足分数的大学
        if maxsc<schools[i]:            #找出大学中最高分
            maxsc=schools[i]            #把最高分存在maxsc里
for i in schools:
    if maxsc==schools[i]:
        print("你最好选择：",i)

ls1=[1,2,3]
ls1.remove()
ls1.pop()