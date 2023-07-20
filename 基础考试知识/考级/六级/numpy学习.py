import numpy as np
dt=np.dtype("i1")
v=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
a=np.array(v,dtype=dt,order='C')
print(a)