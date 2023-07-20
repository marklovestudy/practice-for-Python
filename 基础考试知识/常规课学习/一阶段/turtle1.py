'''
write()         #write(arg: object, move: bool = ..., align: str = ..., font: Tuple[str, int, str] = ...) -> None: ...
arg             #绘画文字为字符串格式，要有”“。
move(可选)       #move默认为False。如果move设定为True,则笔将移动到右下角。
align(可选)       #指排列成线，左中右排列，选left即左，center即中，right即右，是字符串格式。
font(可选)：       #字体str为字符格式，int是整数，str是字符格式，分别代表fontname：字体名称，fontsize：字体大小，fonttype：字体类型。
如normal、bold、italic。以元组格式输入
import turtle as t      #载入turtle当作t
t.speed(1)              #速度设定为1
for i in range(4):      #循环4次
    t.pendown()         #落笔
    t.write("mark",True,"center",("黑体",25,"normal"))    #输入内容”mark“，画笔移到右下角，居中，黑体大小25常规
    t.penup()           #抬笔
    t.right(90)         #右转90度
    t.forward(100)      #前进100步

四种颜色确定的方法：
#:1--t.color('green','red')   #t.color(t.pencolor(),t.fillcolor())
#2-- t.pencolor()    t.fillcolor()
#3--t.color((0.1,0.5,0.6))      #t.color((r.random(),r.random(),r.random()))
#4--第一步：修改颜色范围t.colormode(255)  第二步：确定颜色t.color((1,2,3),(255,255,255))

5、textinput()、numinput()    #文本和数字输入
import turtle as t                          #载入库
my_name = t.textinput("name","your name")   #输入文本
t.write(my_name)                            #写文本
t.mainloop()                                #主循环
'''
# import turtle as t
# import random as r
# t.speed(1)
# # name = t.textinput('IQ','你聪明吗：')          #文本输入
# for i in range(10):
#     num1 = r.randint(0,100)
#     num2 = r.randint(0,100)
#     num3 = t.numinput('算术','%s*%s=?'%(num1,num2),0,0,20000)         #数字输入
#     t.color((r.random(),r.random(),r.random()))
#     t.forward(i*50)
#     t.right(90)
#     if num3 == num1*num2:
#         t.write('大聪明',font=("黑体",25,"normal"))
#     else:
#         t.write('sd',font=("黑体",25,"normal"))
# t.mainloop()

# import turtle as t
# #随机颜色，随机大小，随机字体，随机风格。
# zt = ['黑体','宋体','仿宋','楷体','幼圆','Arial','Verdana',
#       'Times New Roman','Sans Serif','Consolas']
# fg = ['normal','bold','italic','bold italic']
# import random as r
# str1='全民制作人员大家好，我是练习时长两年半的个人练习生，蔡徐坤'
# t.goto(-700,0)
# for i in str1:
#       print(i)
#       t.color(r.random(),r.random(),r.random())
#       t.write(i,move=True,font=(r.choice(zt),r.randint(20,50),r.choice(fg)))
# t.mainloop()
# t.write('蔡徐坤')
# t.penup()
# t.sety(50)
# t.resizemode('user')
# with open('1231.jpg','rb') as f:
#       v=f.read()
# print(v)
# with open('cxk.gif','wb') as f:
#       f.write(v)
# t.register_shape('cxk.gif')
# t.shape('cxk.gif')
# t.turtlesize(10.6,10.6,1)
# print(t.resizemode())
# t.mainloop()
import turtle as t
import random as r
t.speed(1)
# name = t.textinput('IQ','你聪明吗：')          #文本输入
for i in range(10):
    num1 = r.randint(0,100)
    num2 = r.randint(0,100)
    num3 = t.numinput('算术','%s*%s=?'%(num1,num2),0,0,20000)         #数字输入
    t.color((r.random(),r.random(),r.random()))
    t.forward(i*50)
    t.right(90)
    if num3 == num1*num2:
        t.write('大聪明',font=("黑体",25,"normal"))
    else:
        t.write('sd',font=("黑体",25,"normal"))
t.mainloop()