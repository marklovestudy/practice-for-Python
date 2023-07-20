'''
二、创建方式如下：
    第一种方式：直接创建一个列表：
    list1 = [1,2,3]
    第二种方式：函数创建：
    list1 = list(range(10))
    第三种方式：推导式创建：
    list1 = [i for i in range(2,10,2)]

三、访问列表：
    索引访问：
    list1 = [i for i in range(2,20,2)]
    print(list1[0])
    print(list1[2:4])
    print(list1[1:8:3])             #1代表起始索引位置，8代表结束位置，3代表步长

实列：
list2 = [1,2,3]                         #直接创建
list3 = list(range(10))                 #函数创建
list1 = [i for i in range(2,20,2)]      #推导式创建
print(list1)
print(list1[0])
print(list1[2:4])
print(list1[1:8:3])

四、通用操作：
                1判断元素是否在序列之内：in,not in.
                2连接序列：list1+list2
                3重复序列元素：list1*n
                4索引访问：s[i]，s[i:j],s[i:j:k]
                5获取序列属性：长度len(s),最小值min(s),最大值max(s),和sum(s)
                6检索某个元素第一次出现的元素下标s.index('x')
                7检索某个元素出现的次数s.count('x')

五、列表的使用方法详解：
1、append()原来列表的最后添加元素
li = [1,3,4,5]
v = li.append(6)  #把6添加到列表li的最后一项*
print(li)       #[1,3,4,5,6]

2、clear()清空列表
li = [1,3,4,5]
v = li.clear()
print(li)           #[]

3、copy()浅拷贝
li = [1,3,4,5]
v = li.copy()
print(v)

4、count()计算元素的数量
li = [1,3,4,5]
v = li.count(3)
print(v)   #输出：1

5、extend()在列表后添加可迭代对象
li = [1,3,4,5]
v = li.extend([66,"mark"])#extend里面加可迭代对象，用的是for循环添加
print(li)       #[1,3,4,5,66,"mark"]
注：
for i in [66,"mark"]
    li.append(i)
#[1, 3, 4, 5, 66, 'mark']

6、index()根据值找到值的位置index()，从左开始找，找到一个就不向后面找了。
li = [1,3,4,5,3]
v = li.index(3)
print(v)   #输出 1

7、 insert(2,66)在指定位置插入值。
li = [1,3,4,5,3]
v = li.insert(2,66)     #[1,3,66,4,5,3]
print(li)

8、pop()默认删除最后一个元素的值，并获取删除的值，如果指定索引，将删除索引的值，并获得这个值。
li = [1,3,4,5,3]
v = li.pop()
print(li)
print(v)

9、remove()删除指定值，左边优先
li = [1,3,4,5,3]
v = li.remove(3)  #不获得值
print(li)    #[1, 4, 5, 3]
print(v)

10、reverse()将当前列表翻转
li = [1,3,4,5,3]
v = li.reverse()
print(li)
print(v)

11、sort()排序，从小到大reverse = False    从大到小排reverse = True
li = [1,3,4,5,3]
v = li.sort()
print(li)   #[1, 3, 3, 4, 5]
print(v)
'''

#小题目：请在下面列表list4中添加数字7，前求出list4的长度。
list4=['1',3,'5',7,'2,3']
#小题目：请给list7从小到大排序，打印出第二个元素的值。
list7=[-3,6,3,7,5,-4,10]
#请删除下列列表中的最大值和最小值
list9=[11,4,514,191,9,81,0]
#请在下面列表末尾添加'mk'，并在元素2前面添加元素11。最后用index找出'mk'的索引号。
list10=[1,2,3]
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