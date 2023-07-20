list4=['1',3,'5',7,'2,3']
list4.append(7)
len1=len(list4)
print(len1)
#小题目：请给list7从小到大排序，打印出第二个元素的值。
list7=[-3,6,3,7,5,-4,10]
list7.sort()
print(list7[1])
#请删除下列列表中的最大值和最小值
list9=[11,4,514,191,9,81,0]
list9.remove(max(list9))
list9.remove(min(list9))
#请在下面列表末尾添加'mk'，并在元素2前面添加元素11。最后用index找出'mk'的索引号。
list10=[1,2,3]
list10.append('mk')
list10.insert(1,11)
list10.index('mk')
#第一大题：
list1=[['mark',55,45,67],
       ['weiwei',65,85,67],
       ['dafei',45,85,97],
       ['xiaoz',54,76,37]]
#请找出总成绩最高的同学打印出：名字和总分
#请找出总成绩最低的同学打印出：名字和总分
#请算出四位同学的平均成绩
max_name=list1[0][0]           #['mark',55,45,67],
maxscore=sum(list1[0][1:])         #[55,45,67]
for st in list1[1:]:        #[['weiwei',65,85,67],['dafei',45,85,97],['xiaoz',54,76,37]]
    if maxscore < sum(st[1:]):     #['weiwei',65,85,67]
        max_name =st[0]
        maxscore =sum(st[1:])
print(max_name,maxscore)