'''
专业扩展库
    IPython/Jupyter Notebook
    (交互式前端接口)
    Bokeh 基本扩展库
    (Web可视化扩展)
    Keras/Theano Pandas SymPy
    (机器学习前端接口) (数据处理模块) (符号计算模块)
    TensorFlow(深度学习扩展库)(绘图模块) Matplotlib Python内核
    (机器学习扩展库) Scikit-Learn NumPy/SciPy(数值计算模块)基本1/0內建函数

第三方库的导入方法:
    使用Python进行编程时，有些功能没必须自己实现，可以借助 Python现有的标准库或者其他人提供的第三方库。
    >>>import math>>>math.pi
    >>>math.sin(0.5)
    >>>math.sqrt(144)

第三方库的导入方法:
    其它主要的两种:
    1.import模块名1[as别名1]，模块名2[as别名2]，..
    使用这种语法格式的import语句，会导入指定模块中的所有成员(包括变量、函数、类等)。
    当需要使用模块中的成员时，只需用该模块名(或别名)作为前缀。例如:
    >>>import math asm>>>m.pi
    第三方库的导入方法:
    其它主要的两种:
    2.from模块名import成员名1[as别名11，成员名2[as别名2]，..
    使用这种语法格式的import语句，只会导入模块中指定的成员，而不是全部成员。
    同时，当程序中使用该成员时，无需附加任何前缀，直接使用成员名(或别名)即可。
    注意，用1括起来的部分，可以使用，也可以省略。
    3.from 模块名 import*例如:from math import*
'''