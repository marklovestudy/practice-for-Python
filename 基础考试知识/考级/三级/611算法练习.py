import random as r  # 载入随机库


def maopaosort(ls):
    sz = len(ls)
    for i in range(sz - 1):
        for j in range(sz - 1 - i):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]


def slectsort(l):
    sz = len(l)
    for i in range(sz - 1):
        for j in range(i + 1, sz):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]


def dg(n):
    if n == 1:
        return 1
    return dg(n - 1) + n


def dgx(n):
    if n == 1:
        return 1
    return dg(n - 1) * n


def insertsort(l):
    sz = len(l)
    for i in range(1, sz):
        for j in range(i):
            if l[j] > l[i]:
                l.insert(j, l.pop(i))


def instsst(l):
    sz = len(l)
    for i in range(-2, -sz, -1):
        for j in range(-1, i - 1, -1):
            if l[i] < l[j]:
                v = l.pop(i)
                l.insert(j - 1, v)
            # else:
            #     l.append(l.pop(i))


if __name__ == '__main__':
    ls = [r.randint(0, 100) for i in range(25)]
    print(ls)
    # maopaosort(ls)
    # slectsort(ls)
    # re=dg(100)
    # insertsort(ls)
    instsst(ls)
    print(ls)

# 请输入一个数，把这个按从小到大排序
# 如输入：15432   输出：12345           int
