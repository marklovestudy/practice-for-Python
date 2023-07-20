def aa(name):           #函数的创建
    print('%s,你吃了吗?'%name)    #函数的功能

def bb(name):
    print(name,'拿来吧你?')

def cc(name,t,n=3):       #参数传递,带默认值
    if n > 10:
        print('call the ',t)
        print(name,'你就像天上的仙女，何时来人间一趟。')
    if n <= 10:
        print('call the ', t)
        print(name, ' 你就不要出来吓人啦。')
def dd(*args):              #多参数传值
    for i in args:
        print('亲爱的%s您好，感谢这些年的关照，最近为了更好的反馈您，'
              '我们这边给您100块的优惠卷，满300可以使用。'%i)
def ee(kwargs):             #关键字传值，字典
    for k,v in kwargs.items():      #遍历字典
        print('call to %s'%v)
        print('亲爱的%s您好，感谢这些年的关照，最近为了更好的反馈您，'
              '我们这边给您100块的优惠卷，满300可以使用。'%k)
names=['王哥','张家霖','郑南','林家冀','mark']
catalog = {'王哥':13612345678,'张家霖':13643218765,'郑南':13888888888,'林家冀':18888888888,'mark':13555556666}
ee(catalog)