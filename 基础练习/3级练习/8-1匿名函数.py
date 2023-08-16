"""
1、lambda x:x+1
print(lambda x:x+1)     #<function <lambda> at 0x00000000028915E0>
func = lambda x:x+1
print(func(10))         #11

2、name = "mark"                                 #name = "mark_nb"
func = lambda x:x + "_nb"
print(func(name))                               #mark_nb
print((lambda x:x + "_nb")(name))               #mark_nb
print((lambda x:"_".join(x))(name))             #m_a_r_k
print((lambda x:x.startswith("m"))(name))       #True

3、
func = lambda x,y,z :x+y+z
print(func(1,2,3))                              #6

4、
func = lambda x,y,z:(x+1,y+1,z+1)
print(func(1,2,3))                              #(2, 3, 4)
"""
# def n(a):
#     return a
# v = lambda :n('1')
# def add1(a,b):
# #     return a+b
# #
# # print(lambda x:x+1)     #<function <lambda> at 0x00000000028915E0>
# # func = lambda a,b:add1(a,b)
# # print(func(1,5))

#lambda 参数:代码块(返回结果)   得到的结果是一个函数地址
#请用lambda写一个把字符串后面加'ok'字符串的函数地址
#用lambda写一个把数字变量加2的函数地址
#请用lambda写一个打印hello world的函数地址
#请用lambda写一个打印1,2,3,4,5..n的函数地址
