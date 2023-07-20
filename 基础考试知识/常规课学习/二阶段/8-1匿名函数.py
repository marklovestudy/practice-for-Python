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
def n(a):
    return a
v = lambda :n('1')
map