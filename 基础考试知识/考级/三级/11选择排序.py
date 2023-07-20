'''
选择排序是一种简单直观的排序算法，无论什么数据进去都是 O(n²) 的时间复杂度。
所以用到它的时候，数据规模越小越好。唯一的好处可能就是不占用额外的内存空间。

1选择排序的基本思想
    1对于n个元素的数组，用选择算法进行排序时，比较次数与冒泡算法相同，但交换的次数
    2比冒泡排序要少，因此它具有较高的效率。

2选择排序的算法实现
    选择排序的程序同样采用双重循环嵌套来实现，外循环来控制是第几遍加工，内循环用来
    控制数组内进行排序元素的下标索引变化范围。在每一遍加工结束，都需要用一个变量来
    存储这一遍加工中所找出的最小(或最大)的数据在数组内的下标索引。

3算法步骤
    1首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
    2再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    3重复第二步，直到所有元素均排序完毕。

def selectionSort(l):
    for i in range(len(l) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

def slection_px(l,g):
    for i in range(len(l)-1):
        m = i
        for j in range(i+1,len(l)):
            if g == '<':
                if l[j] < l[m] :
                    m = j
            if g == '>':
                if l[j] > l[m] :
                    m = j
        l.insert(i,l.pop(m))
    return l
l = [1,5,3,8,2,4,7,6]
print(slection_px(l,'<'))

框架：
    for i in range(0,n-1)       共进行n-1趟
        k = i
        for j in range(i+1,n)   第i趟
            if 找到一个比K位置上小的元素，则：
                k = j
            if i != k,则：
                交换数据对

def sp(l):
    for i in range(len(l)-1):           #只要排n-1次，最后一个数不用排了
        k = i                           #记录当前要排的列表元素的索引号，并临时当作是未排好序的子序列的最小值。
        for j in range(i+1,len(l)):     #遍历当前要排的元素后面的子序列
            if l[j] < l[k]:             #如果子序列中有值比当前最小值小。
                k = j                   #更新最小值的索引号
        l[i],l[k]=l[k],l[i]             #把最小值与当前要排的元素的值互换。
    return l

print(sp(l))
'''
# def selectionSort(l):
#     for i in range(len(l) - 1):
#         # 记录最小数的索引
#         minIndex = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[minIndex]:
#                 minIndex = j
#         # i 不是最小数时，将 i 和最小数进行交换
#         if i != minIndex:
#             arr[i], arr[minIndex] = arr[minIndex], arr[i]
#     return arr

l = [2,1,5,3,8,2,4,7,6]
def sp(l):
    for i in range(len(l)-1):           #只要排n-1次，最后一个数不用排了
        k = i                           #记录当前要排的列表元素的索引号，并临时当作是未排好序的子序列的最小值。
        for j in range(i+1,len(l)):     #遍历当前要排的元素后面的子序列
            if l[j] < l[k]:             #如果子序列中有值比当前最小值小。
                k = j                   #更新最小值的索引号
        l[i],l[k]=l[k],l[i]             #把最小值与当前要排的元素的值互换。
    return l

print(sp(l))


# [3,6,7,8,9]         小到大排列min=7