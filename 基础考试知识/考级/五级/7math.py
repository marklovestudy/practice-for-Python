'''
概念：
math 模块提供了大量与数学计算有关的对象，包括对数函数、指数函数、三角函数、误差计算及一些常用的数学常数。
(1）常数 pi 和 e
>>> import math
>>> math . pi
3141592653589793
>>> math.e
2718281828459045

(2) ceil ( x ）向上取整，返回大于等于 x 的最小整数 floor ( x ）下取整，返回小于等于 x 的最大整数。
>>> math.ceil(3.14)
4
>>> math.ceil(-3.14)
-3
>>> math.floor(3.99)
3
>>> math.floor(-3.14)
-4

(3) factorial ( x ）返回 x 的阶乘，要求 x 必须为正整数。
>>> math.factorial(5)
120

(4) log ( x [. b ]）若不提供参数 b ，则返回 x 的自然对数值；若提供参数 b ，则返回 x 以 b 为底的对数值。
>>> math.log(256,2)
8.0
>>> math.log(100)
4.605170185988092

(5) cos ( x )、 sin ( x )、 tan ( x )，返回 x 的余弦、正弦和正切函数值，
 x 的单位为弧度。
 acos ( x )、 asin ( x )、 atarnlx )，返回 x 的反余弦、反正弦和反正切函数值，结果为弧度。
>>> math.sin(math.pi)
1.2246467991473532e-16
>>> math.cos(1)
0.5403023058681397
>>> math.asin(0.707)
0.785247163395153

(6) gcd ( x . y )返回整数 x 和 y 的最大公约数。
>>> math.gcd(12,18)
6
(7) sqrt ()返回正数 x 的根，功能等价于 x **05，但不能对负数求平方根，不如幂运算符＊*05功能强大。
>>> math.sqrt(9)
3.0
>> mathsqrt (-9)
 Traceback ( most recent call last :
 File "< pyshel #75>", line l , in < module > mathsqrt (9)
 ValueError : math domain error
>>> (-9)**0.5
(1.8369701987210297e-16+3j)

注：abs(x)绝对值
max(x1,x2,...)返回最大值
min(x1,x2,...)返回最小值
round(x,n)四舍五入到n位小数
atan2(y,x)返回坐标x,y的正切值
hypot(x,y)返回殴几里德范数，相当于sqrt(x*x+y*y),即求距离
degrees(x)转角度
radians(x)转弧度
'''


