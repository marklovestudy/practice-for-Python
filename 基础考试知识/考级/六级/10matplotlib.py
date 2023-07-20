'''
概念：
Matplotlib 是 Python 的绘图库。 它可与 NumPy 一起使用，也可以和图形工具包一起使用，如 PyQt 和 wxPython。
pip3 安装：pip3 install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple
实例1
import numpy as np
from matplotlib import pyplot as plt
x = np.arange(1,11)
y =  2  * x +  5
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x,y)
plt.show()

以上实例中，np.arange() 函数创建 x 轴上的值。y 轴上的对应值存储在另一个数组对象 y 中。
 这些值使用 matplotlib 软件包的 pyplot 子模块的 plot() 函数绘制。

图形由 show() 函数显示。

实例2：
要显示圆来代表点，而不是上面示例中的线，请使用 ob 作为 plot() 函数中的格式字符串。实例：
import numpy as np
from matplotlib import pyplot as plt
x = np.arange(1,11)
y =  2  * x +  5
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x,y,"ob")
plt.show()

实例3：
使用 matplotlib 生成正弦波图。
import numpy as np
import matplotlib.pyplot as plt
# 计算正弦曲线上点的 x 和 y 坐标
x = np.arange(0,  3  * np.pi,  0.1)
y = np.sin(x)
plt.title("sine wave form")
# 使用 matplotlib 来绘制点
plt.plot(x, y)
plt.show()

实例4：subplot() 函数在同一图中绘制不同的东西
绘制正弦和余弦值:
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,  3  * np.pi,  0.1) # 计算正弦和余弦曲线上的点的 x 和 y 坐标
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.subplot(2,  1,  1)  #建立subplot网格高为2，宽为1。激活第一个 subplot
plt.plot(x, y_sin) # 绘制第一个图像
plt.title('Sine')
plt.subplot(2,  1,  2) # 将第二个 subplot 激活，并绘制第二个图像
plt.plot(x, y_cos)
plt.title('Cosine')
plt.show()# 展示图像

实例5：bar() pyplot子模块提供bar()函数来生成条形图
以下实例生成两组 x 和 y 数组的条形图。
from matplotlib import pyplot as plt
x =  [5,8,10]
y =  [12,16,6]
x2 =  [6,9,11]
y2 =  [6,15,7]
plt.bar(x, y, align =  'center')
plt.bar(x2, y2, color =  'g', align =  'center')
plt.title('Bar graph')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()

实例6：绘制函数          在区间 [-3, 3] 上的图像。
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-3, 3, 100)   # 创建x轴数据
y = 9 - x**2                  # 计算对应的y轴坐标
plt.xlim(-3, 3)                # 设置x轴坐标范围
plt.xticks(list(range(-3, 4))) # 设置x轴刻度
plt.ylim(0.0, 9.0)             # 设置y轴坐标范围
plt.plot(x, y)                 # 绘制图像
ax = plt.gca()                 # 获取当前轴
ax.set_aspect('equal')         # 设置纵横比相等
ax.grid(True)                  # 显示网格
plt.show()

'''
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,  3  * np.pi,  0.1) # 计算正弦和余弦曲线上的点的 x 和 y 坐标
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.subplot(2,  2,  1)  #建立subplot网格高为2，宽为1。激活第一个 subplot
plt.plot(x, y_sin) # 绘制第一个图像
plt.title('Sinx')
plt.subplot(2,  2,  2) # 将第二个 subplot 激活，并绘制第二个图像
plt.plot(x, y_cos)
plt.title('Cosx')
plt.subplot(2,  2,  3) # 将第三个 subplot 激活，并绘制第二个图像
ls1=[1,2,3,4,5]
ls2=[3,5,15,8,6]
plt.plot(ls1,ls2)
plt.show()# 展示图像