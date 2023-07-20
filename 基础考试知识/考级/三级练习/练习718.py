import random as r

def insertsort(l):
    sz=len(l)
    for i in range(1,sz):
        for j in range(i):
            if l[j]>l[i]:
                l.insert(j,l.pop(i))

if __name__ == '__main__':
    ls=[r.randint(0,100) for i in range(25)]
    print(ls)
    insertsort(ls)
    print(ls)