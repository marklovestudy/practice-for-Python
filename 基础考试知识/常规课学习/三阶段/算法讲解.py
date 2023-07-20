import random as r
def maopao(ls):
    sz=len(ls)
    for i in range(sz-1):
        for j in range(sz-1-i):
            if ls[j]>ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]
def selectsort(ls):
    sz = len(ls)
    for i in range(sz - 1):
        k=i             #记录最小值的索引下标
        for j in range(i,sz):
            if ls[k] > ls[j]:
                k=j
        ls[i],ls[k]=ls[k],ls[i]

if __name__ == '__main__':
    ls=[r.randint(0,100) for i in range(25)]
    print(ls)
    #maopao(ls)
    selectsort(ls)
    #insertsort(ls)
    print(ls)
