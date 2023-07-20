def maopaosort(l):
    sz=len(l)
    for i in range(sz-1):
        for j in range(sz-1-i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
def selectsort(l):
    sz = len(l)
    for i in range(sz - 1):
        for j in range(i+1,sz):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
def insertsort(l):
    sz=len(l)
    for i in range(1,sz):
        for j in range(i):
            if l[j]>l[i]:
                l.insert(j,l.pop(i))
def dg(l):
    ll=l[1:]
    if len(l)==1:
        print(l[0])
    else:
        print(l[0])
        dg(ll)

if __name__ == '__main__':
    import random as r
    ls=[r.randint(0,100) for i in range(25)]
    print(ls)
    #maopaosort(ls)
    #selectsort(ls)
    #insertsort(ls)
    dg(ls)
    print(ls)