'''
键值索引计算：
    middle=left+(target-data[left])/(data[right]-data[left])*(right-left)
    middle:所求的边界索引。
    left:最左侧的数据索引
    target:键值(目标数据)
    dada[left]:最左侧数据值。
    dada[right]:最右侧数据值
    right:最右侧数据的索引

实例：34，53，57，68，72，81，89，93，99。要查找的数据是53，使用插补查找法步骤如下：
    步骤1：将数据列出来并利用公式找到边界索引：
    middle=0+(53-34)/(99-34)*(8-0)=2.3
    取整索引为2，对应的数据是57，
    步骤2：将目标数据53与57比较。53小于57，所以找左半边的数据。即：
    middle=0+(53-34)/(57-34)*(2-0)=1.6
    步骤3：取整索引是1，对应的数据是53，把53和53进行比较。
    53和53数据相等，查找完成。
    注：如果多次查找之后，没有找到相等的值，表示这个键值没有在这个数列中。

插补查找算法函数：
'''
def insert_seach(l,n):
    low=0
    hi=len(l)-1
    print('正在查找数据：',n)
    while low <= hi and n != -1:
        middle=int(low+(n-l[low])/(l[hi]-l[low])*(hi-low))
        if n == l[middle]:
            return middle
        elif n < l[middle]:
            hi=middle-1
        else:
            low=middle+1
    return -1

l=[i+2 for i in range(25)]
print(l)
n=eval(input('n?'))
v=insert_seach(l,n)
if v == -1:
    print('not find it')
else:
    print(l[v],' it is at %s'%v)