'''
1.哈希表和哈希函数
    key_s=[i for i in range(11)]            槽号
    value_s=[None for i in range(11)]       槽号对应的值

2.除留余数法：
    数据%槽数=哈希值

3.折叠法：
    52 05 21 13 14,两两分组再进行相加=105
    1，奇数反转
    2，偶数反转
    其目的都是为了得到一个哈希值，然后对值进行存储。

4.平方取中法
    54,26,93,17,77,31
    步骤1：平方得到：
    54**2=2916
    26**2=676
    93**2=8649
    17**2=289
    77**2=5929
    31**2=961
    步骤2：取中，即取十位和百位，得到：91，67，64，28，92，96
    步骤3：若设置11个槽位，对步骤2的数取余数，得到哈希值分别为：
    3，1，9，6，4，8

碰撞与溢出问题
class HashTable:
    def __init__(self,size):
        self.size=size
        self.throw=[None]*self.size
        self.data=[None]*self.size

    def put(self,key,value):
        hashvalue=self.hashfunction(key,len(self.throw))
        if self.throw[hashvalue] is None:
            self.throw[hashvalue] = key
            self.data[hashvalue] = value
        else:
            if self.throw[hashvalue] == key:
                self.data[hashvalue] = value
            else:
                nextslot=self.rehash(hashvalue,len(self.throw))
                while self.throw[nextslot] is not None and self.throw[nextslot] != key:
                    nextslot=self.rehash(nextslot,len(self.throw))

                if self.throw[nextslot] is None:
                    self.throw[nextslot] = key
                    self.data[nextslot] = value
                else:
                    self.data[nextslot]=value

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def hashfunction(self,key,size):
        return key%size

    def get(self,key):
        startslot=self.hashfunction(key,len(self.throw))
        data=None
        found=False
        stop=False
        pos=startslot
        while pos is not None and not found and not stop:
            if self.throw[pos]==key:
                found=True
                data=self.data[pos]
            else:
                pos=self.rehash(pos,len(self.throw))
            if pos == startslot:
                stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.put(key,value)

H=HashTable(11)
H[16]='红'
H[28]='橙'
H[32]='黄'
H[14]='绿'
H[56]='青'
H[36]='蓝'
H[71]='紫'
print('key:',H.throw)
print('value:',H.data)
print(H[28])
print(H[71])
print(H[93])
'''


