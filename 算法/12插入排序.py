'''
插入排序
    插入排序的代码实现虽然没有冒泡排序和选择排序那么简单粗暴，但它的原理应该是最容易理解的了，
    因为只要打过扑克牌的人都应该能够秒懂。插入排序是一种最简单直观的排序算法，它的工作原理是
    通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

    插入排序和冒泡排序一样，也有一种优化算法，叫做拆半插入。

1. 算法步骤
    将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
    从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素
    与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）

插入排序的基本思想
    先将列表中的头两个元素按顺序排列(比如：升序)。
    接着，每次将一个待排序的元素，按其大小插入前面已经排好序的元素序列中，使序列依然有序，直
    到所有待排序元素全部插入完成。

    如：待排数据：53528。
    第一步：把5看着已经排好
    第二步：把3插入到已经排好的序列5中，即得到35528
    第三步：把5插入到已经排好的序列35中，即得到35528
    第四步，把2插入到已经排好的序列355中，即得到23558
    第五步，把8插入到已经排好的序列2355中，即得到23558

def insertionSort(a):
    for i in range(1,len(a)):       #把第一项当作是已经排好的数，所以只需要把索引1-最后一项遍历，即n-1次
        n = i                       #把索引i项的值当作是要插入的对象。
        for j in range(i):          #遍历已经排好的子序列，即索引i项前的子序列。
            if a[i] < a[n-1]:       #从右到左把要插入的对象与子序列的数比较，直到找到插入对象要插入的位置。
                n -= 1              #变化n的值让插入对象与索引n的前一个数比较。
        a.insert(n,a.pop(i))        #删除插入对象，并把这个值插入到要插入的位置。
    return a

# def insertionSort(arr):
#     for i in range(len(arr)):             #遍历列表
#         preIndex = i-1                    #插入对象的前一项索引值
#         current = arr[i]                  #插入对象的值
#         while preIndex >= 0 and arr[preIndex] > current:  #当插入对象前面有数时，且前面的数大于插入的对象值
#             arr[preIndex+1] = arr[preIndex]       #将前面的数向右移一个位置，此时对比位是preIndex，
#             第一次右移时，要插入的对象被覆盖，没有关系，因为被插入的值已经存储，即current
#             preIndex-=1               #将对比位向左移一个位，即索引-1
#         arr[preIndex+1] = current     #将插入对象插入到此轮最后一次的对比位上
#     return arr

def insertsort(l):
    for i in range(1,len(l)):       #次数
        for j in range(i+1):          #范围
            if l[j] > l[i]:
                l.insert(j,l.pop(i))
                break

对比二者的区别，
方法1：从右到左比较
for i in range(1, len(a)):  # 把第一项当作是已经排好的数，所以只需要把索引1-最后一项遍历，即n-1次
    n = i  # 把索引i项的值当作是要插入的对象。
    for j in range(i):  # 遍历已经排好的子序列，即索引i项前的子序列。
        if a[i] < a[n - 1]:  # 从右到左把要插入的对象与子序列的数比较，直到找到插入对象要插入的位置。
            n -= 1  # 变化n的值让插入对象与索引n的前一个数比较。

方法2：从左到右比较
for i in range(1,len(l)):       #要插入的对象值的索引号为i
    for j in range(i):          #让被插入的对象和已经排好的序列比较
        if l[i] < l[j]:         #找到被插入的位置
            n = j               #n表示要插入的位置

'''



# def insertionSort(arr):
#     for i in range(len(arr)):             #遍历列表
#         preIndex = i-1                    #插入对象的前一项索引值
#         current = arr[i]                  #插入对象的值
#         while preIndex >= 0 and arr[preIndex] > current:  #当插入对象前面有数时，且前面的数大于插入的对象值
#             arr[preIndex+1] = arr[preIndex]       #将前面的数向右移一个位置，此时对比位是preIndex，
#             第一次右移时，要插入的对象被覆盖，没有关系，因为被插入的值已经存储，即current
#             preIndex-=1               #将对比位向左移一个位，即索引-1
#         arr[preIndex+1] = current     #将插入对象插入到此轮最后一次的对比位上
#     return arr

# def insertionSort(list1):
#     for i in range(1,len(list1)):
#         n = i
#         m = 0
#         for j in range(i):
#             if  list1[i] < list1[n-1]:
#                 n -= 1
#             else:
#                 pass
#             m+=1
#             print(m)
#         list1.insert(n,list1.pop(i))
#     return list1

def insertionSort(a):
    for i in range(1,len(a)):       #把第一项当作是已经排好的数，所以只需要把索引1-最后一项遍历，即n-1次
        n = i                       #把索引i项的值当作是要插入的对象。
        for j in range(i):          #遍历已经排好的子序列，即索引i项前的子序列。
            if a[i] < a[n-1]:       #从右到左把要插入的对象与子序列的数比较，直到找到插入对象要插入的位置。
                n -= 1              #变化n的值让插入对象与索引n的前一个数比较。
        a.insert(n,a.pop(i))        #删除插入对象，并把这个值插入到要插入的位置。
    return a




import random
a = []
for i in range(50):
    a.append(random.randint(1,100))
v = insertionSort(a)
print(v)