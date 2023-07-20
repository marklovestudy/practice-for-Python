'''
冒泡排序的概念：
    冒泡排序是在一列数据中把较大(小)的数据逐次向右推移的一种排序技术。

1. 算法步骤
    1比较相邻的元素。如果第一个比第二个大，就交换他们两个。
    2对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
    3针对所有的元素重复以上的步骤，除了最后一个。范围n -= 1
    4持续每次对越来越少的元素重复上面的步骤(n=1)，直到没有任何一对数字需要比较。

冒泡排序的基本思想
    由于每一趟加工都是将本趟最大(小)的数元素像气泡一样移动至本趟的右端位置，所以称作冒泡排序。冒泡有多种变式。
    1基本思想(以升序为例)
        依次比较相邻的两个数，将大数放在后面，小数放在前面。
        n个数排序共需进行n-1趟

def maopao(list1):
    for i in range(1, len(list1)):
        for j in range(0, len(list1)-i):
            if list1[j] > list1[j+1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
    return list1

v = maopao([2,5,3,6,9,5,4,3,2])
print(v)

冒泡程序框架
    for i in range(1,n)     共进行了n-1次
        for j in range(0,n-i)   第i趟排序时
            if 数据对反序，则：
            交换数据对

list1 = [3,4,5,6,73,4,2,1,4,5,56,8,9,0,0,123,12355]
def mp(l,g):
    for i in range(1,len(l)):
        for j in range(len(l)-i):
            if g == '>':
                if l[j] > l[j+1]:
                    l[j],l[j+1] = l[j+1],l[j]
            if g == '<':
                if l[j] < l[j+1]:
                    l[j],l[j+1] = l[j+1],l[j]
    return l
print(mp(list1,'<'))

def mp(l,g):
    for i in range(1,len(l)):                   #只需要遍历n-1次
        for j in range(len(l)-i):               #遍历未排好序的子序列
            if g == '<':                        #升序
                if l[j] > l[j+1]:               #两两相比，如果左边的值大于右边
                    l[j],l[j+1] = l[j+1],l[j]   #左右值互换
            elif g == '>':                      #降序
                if l[j] < l[j+1]:               #两两相比，如果左边的值小于右边
                    l[j],l[j+1] = l[j+1],l[j]   #左右值互换
            else:
                pass
    return l

'''
l = [1,2,3,4,5,45,8,7,6]
def mp(l,g):
    for i in range(1,len(l)):                   #只需要遍历n-1次
        for j in range(len(l)-i):               #遍历未排好序的子序列
            if g == '<':                        #升序
                if l[j] > l[j+1]:               #两两相比，如果左边的值大于右边
                    l[j],l[j+1] = l[j+1],l[j]   #左右值互换
            elif g == '>':                      #降序
                if l[j] < l[j+1]:               #两两相比，如果左边的值小于右边
                    l[j],l[j+1] = l[j+1],l[j]   #左右值互换
            else:
                pass
    return l
print(mp(l,'>'))