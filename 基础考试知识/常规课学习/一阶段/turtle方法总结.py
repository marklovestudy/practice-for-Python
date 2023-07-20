"""
一、光标移动和状态信息的设置
(1)、移动和绘制
1、backward()、bk()、back()#后退
import turtle as t      #载入turtle当作t
t.backward(100)         #后退100步
t.bk(100)               #后退100步
t.back(100)             #后退100步

2、goto()、setpos()、setposition()、setx()、sety()、setheading()、seth()#前往，定位，设定
import turtle as t      #载入turtle当作t
t.goto(100,100)         #前往x:100,y:100的点
t.setpos(100,0)         #前往x:100,y:0的点)
t.setposition(0,100)    #前往x:0,y:100的
t.setx(50)              #把x设定为50
t.sety(150)             #把y设定为150
t.setheading(90)        #把方向设定为90方向
t.seth(-90)             #把方向设定为-90方向

3、forward()、fd()        #前进
import turtle as t      #载入turtle当作t
t.forward(100)          #前进100步
t.fd(200)               #前进200步

4、right()、rt()、left()、lt()  #右转和左转
import turtle as t      #载入turtle当作t
t.right(90)             #右转90度
t.rt(90)                #右转90度
t.left(90)              #左转90度
t.lt(90)                #左转90度

5、home()                #返回原点，方向和坐标归0
import turtle as t          #载入turtle当作t
t.goto(90,80)               #前往x:90,y:80
t.right(92)                 #右转92度
t.home()                    #返回原点x:0,y:0
print(t.xcor(),t.ycor())    #打印当前坐标，验证home()方法的功能   输出：0 0
print(t.heading())          #打印当前方向，验证home()方法的方向是否归0   输出0.0

6、circle()              #画圆
#t.circle(r,e,s)        #r:代表圆的半径，e:代表要画的圆的角度，s:代表几步画完
import turtle as t      #载入turtle当作t
t.circle(80)            #画半径为80的圆，半径是正数代表逆时针画，默认画360度，一步画完。
t.circle(-80)           #画半径为80的圆，半径是负数代表顺时针画，默认画360度，一步画完。
t.circle(100,180,4)     #逆时针画半径为100的圆，画180度，4步画完。

7、dot()                 #画一个点
import turtle as t      #载入turtle当作t
t.dot(10,"red")         #画一个点,大小:10，颜色：红色
t.goto(100,50)          #前往x:100,y:50
t.dot(10,"red")         #画一个点,大小:10，颜色：红色

8、stamp()、clearstamp()、clearstamps()    #印章使用
1、stamp()印章
2、clearstamp(5)，消除几号印章，第一个印章代表5，第二个代表6
3、clearstamps(3)  消除几个印章，消除3个印章
import turtle as t
#t.hideturtle()

#添加组合画图
s = t.Shape("compound")
body = ((0,0),(100,100),(-100,100))
head = ((0,0),(50,50),(-50,50))
eye = ((5,30),(5,35),(-5,30),(-5,35))
tail = ((0,100),(50,150),(-50,150))

s.addcomponent(body,"yellow","red")
s.addcomponent(head,"blue","red")
s.addcomponent(eye,"black","red")
s.addcomponent(tail,"yellow","red")

t.register_shape("myshape",s)

t.shape("myshape")

t.up()
for i in range(1,200):
     t.backward(10)
     t.stamp()              #每次印章一次
t.clearstamps(6)            #清除6个印章，分别为1，2，3，4，5，6号印章，如果不写数字就会清除所有印章，clearstamp()清除印章
t.down()

9、undo()                #撤消
import turtle as t      #载入turtle当作t
t.forward(90)           #前进90步
t.right(90)             #右转90度
t.circle(40)            #逆时针画半径为40的圆
t.undo()                #撤消上一步：即撤消圆
t.backward(50)          #后退50步
t.right(30)             #右转30度
t.circle(70)            #画半径为70的圆

10、speed()              #速度
import turtle as t      #载入turtle当作t
t.speed(0)              #速度设定为0，0代表最快无动画效果，1-10代表绘画速度由慢变快。
t.circle(70)            #画半径为70的圆

(2)、获取光标的状态
11、towards()            #目标方向
import turtle as t      #载入turtle当作t
t.goto(0,0)             #前往x:0,y:0
v = t.towards(0,200)    #表示你站在x:0,y:0，你的目标地在x:0,y:200，这个目标地在你的90方向，并赋值给v
print(v)                #输出：90

12、heading()            #面向多少方向
import turtle as t      #载入turtle当作t
t.setheading(0)         #设定方向为0方向
t.lt(12)                #左转12度
v = t.heading()         #把当前面向的方向赋值给v
print(v)                #打印v    输出：12.0
t.left(34)              #左转34度
v = t.heading()         #把当前面向的方向赋值给v
print(v)                #打印v    输出：46.0
t.right(33)             #右转33度
v = t.heading()         #把当前面向的方向赋值给v
print(v)                #打印v    输出：13.0

13、position()           #获取当前位置的坐标
import turtle as t      #载入turtle当作t
t.forward(33)           #前进33步
t.backward(54)          #后退54步
t.forward(-40)          #前进-40步
v1 = t.xcor()           #获取当前位置x坐标，并赋值给v1
v2 = t.ycor()           #获取当前位置y坐标，并赋值给v2
v3 = t.position()       #获取当前位置坐标，并赋值给v3
print(v1,v2,v3)         #打印出v1,v2,v3   输出：-61.0  0.0  (-61.00,0.00)

(3)、设置与度量单位
14、radians()、degrees()      #弧度、角度
import turtle as t          #载入turtle当作t
t.speed(1)                  #画笔速度设定为1
t.radians()                 #把度量单位设定为弧度
t.forward(100)              #前进100步
t.right(1)                  #右转1弧度约等于57.3度
t.forward(100)              #前进100步
t.right(1)                  #右转1弧度约等于57.3度
t.degrees()                 #把度量单位设定为角度
t.forward(100)              #前进100步
t.right(30)                 #右转30度
t.forward(100)              #前进100步

二、画笔的相关设置
1、pendown()、pd()、down()     #画笔落下
   penup()、pu()、up()        #画笔抬起
import turtle as t          #载入turtle当作t
t.pendown()                 #落笔
t.forward(100)              #前进100步
t.right(90)                 #右转90度
t.penup()                   #抬笔

2、pensize()、width()         #画笔粗细设定为
import turtle as t           #载入turtle当作t
t.pensize(5)    #width()    #画笔粗细设定为5
t.forward(100)              #前进100步
t.right(90)                 #右转90度
t.forward(200)              #前进200步

3、pen()                     #画笔，可以用参数来设置画笔  t1 = t.Pen()类
import turtle as t          #载入turtle当作t
t.pen(pensize=5,pencolor="red")     #把画笔粗细设定为5，颜色设定为红色
t.forward(100)              #前进100步
t.right(90)                 #右转90度
t.forward(200)              #前进200步

4、isdown()                  #画笔是否落下
import turtle as t          #载入turtle当作t
t.pen(pensize=5,pencolor="red")     #把画笔粗细设定为5，颜色设定为红色
v = t.isdown()              #是否落笔，如果落笔，返回True,赋值给v,否则：返回False返回给v
print(v)                    #打印v   输出：True

5、color()、pencolor()、fillcolor()   #颜色控制：前：颜色设定为（包括海龟标），中：把画笔颜色设定为，后：把填充色设定为。
import turtle as t          #载入turtle当作t
t.speed(1)                  #将速度设定为1
t.color("blue")             #将颜色设定为蓝色
t.pencolor("red")           #将画笔颜色设定为红色
t.fillcolor("green")        #将填充颜色设定为绿色
t.begin_fill()              #开始填充
for i in range(4):          #for循环4次
    t.forward(100)          #前进100步
    t.right(90)             #右转90度
t.end_fill()                #结束填充

6、绘图控制
reset()、resetscreen()   #重置，把所有设定还原成默认设置
import turtle as t      #载入turtle当作t
t.speed(1)              #速度设为1
t.color("blue")         #将颜色设定为蓝色
t.pencolor("red")       #将画笔颜色设定为红色
t.fillcolor("green")    #将填充颜色设定为绿色
t.begin_fill()          #开始填充
for i in range(4):      #循环4次
    t.forward(100)      #前进100步
    t.right(90)         #右转90度
t.end_fill()            #结束填充
t.reset()               #重置，所有设定包括显示内容还原成默认状态
for i in range(4):      #循环4次
    t.forward(100)      #前进100步
    t.right(90)         #右转90度

clear()、clearscreen()   #清空当前显示内容
import turtle as t      #载入turtle当作t
t.speed(1)              #速度设为1
t.color("blue")         #将颜色设定为蓝色
t.pencolor("red")       #将画笔颜色设定为红色
t.fillcolor("green")    #将填充颜色设定为绿色
t.begin_fill()          #开始填充
for i in range(4):      #循环4次
    t.forward(100)      #前进100步
    t.right(90)         #右转90度
t.end_fill()            #结束填充
t.clear()               #清空显示内容，但不修改设置
for i in range(4):      #循环4次
    t.forward(100)      #前进100步
    t.right(90)         #右转90度
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

三、形状的调整
可见性
1、showturtle()、st()         #显示光标
2、hideturtle()、ht()         #隐藏光标
3、isvisible()               #是否可见，可见返回True,否则返回False。
import turtle as t          #载入turtle当作t
t.speed(1)                  #速度设定为1
for i in range(10):         #循环10次
    t.showturtle()          #显示光标
    t.forward(100)          #前进100步
    t.right(90)             #右转90度
    v = t.isvisible()       #是否可见，把值赋值给v
    print(v)                #打印v，输出：True
    t.hideturtle()          #隐藏光标
    t.forward(100)          #前进100步
    t.right(90)             #右转90度
    v = t.isvisible()       #是否可见，把值赋值给v
    print(v)                #打印v，输出：False

外观
4、shape()           #形状：“arrow”，“turtle”，“circle”，“square”，“triangle”，“classic”。
#“arrow”：等腰直角三角形    “turtle”：小海龟    “circle”：圆
#“square”：正方形           “triangle”：正三角形     “classic”：传统内四角
import turtle as t          #载入turtle当作t
t.speed(1)                  #将速度设定为1
t.shape("turtle")           #将光标设定为小海龟
while True:                 #重复循环
    t.right(90)             #右转90度
    t.forward(50)           #前进50步

5、resizemode()              #形状大小调整模式：“auto”，“user”，“noresize"
如果未提供任何参数，则返回当前的resizemode。
"auto”:根据pensize的值调整 turtle的外观。包含光标和画笔。
import turtle as t          #载入turtle当作t
t.speed(1)                  #将速度设定为1
t.shape("turtle")           #将光标设定为小海龟
t.resizemode("auto")        #根据pensize的值调整 turtle的外观。包含光标和画笔。
t.pensize(20)               #将光标和画笔大小设定为20
while True：                #重复循环
    t.right(90)             #右转90度
    t.forward(50)           #前进50步

“user”:根据shapesize()设置的Stretchfactor和outlinewidth(轮廓)值调整 turtle 的外观
import turtle as t          #载入turtle当作t
t.speed(1)                  #将速度设定为1
t.shape("turtle")           #将光标设定为小海龟
t.resizemode("user")        #根据shapesize(宽，长，轮廓)的值调整 turtle的外观。三个值为浮点型变量。
t.shapesize(1.5,1.6,1)      #将光标大小设定为宽：1.5，长1.6，轮廓：1.0
while True：                #重复循环
    t.right(90)             #右转90度
    t.forward(50)           #前进50步

“noresize”:没有改变 turtle 的外观
import turtle as t          #载入turtle当作t
v = t.resizemode()          #没有改变turtle的外观
print(v)                    #输出：noresize

6、shapesize()、turtlesize()      #光标形状大小
import turtle as t              #载入turtle当作t
t.shapesize(20)#turtlesize()    #光标形状大小设定为20
while True:                     #重复循环
    t.right(90)                 #右转90度
    t.forward(50)               #前进50步

7、shearfactor()                 #剪切因子
import turtle as t              #载入turtle当作t
t.speed(1)                      #将速度设定为1
t.shape("turtle")               #将光标设定为小海龟
t.shearfactor(3)                #外观剪切因子设为3
while True:                     #重复循环
    t.right(90)                 #右转90度
    t.forward(50)               #前进50步

8、settiltangle()、tilt()、tiltangle()   #设置倾角模式
import turtle as t              #载入turtle当作t
t.speed(1)                      #将速度设定为1
t.settiltangle(180)#tilt()      #设置倾角为180度，相当于倒立
v = t.tiltangle()               #获取当前倾角，也可以输入参数：浮点型，进形倾角设定，赋值给v
print(v)                        #打印v,输出180.0
while True:                     #重复循环
    t.right(90)                 #右转90度
    t.forward(50)               #前进50步

9、shapetransform((t11,t12,t21,t22)      #t11，t12，t21，t22(可选)：行列式t11 * t22-t12 * t21不能为零，否则会引起错误。
import turtle as t                      #载入turtle当作t
t.speed(1)                              #将速度设定为1
t.shapetransform((2,0,0,1)              #设置形状：
while True:                             #重复循环
    t.right(90)                         #右转90度
    t.forward(50)                       #前进50步

10、get_shapepoly()
import turtle as t                      #载入turtle当作t
t.speed(1)                              #将速度设定为1
t.shape()                               #设定光标为默认
v=t.get_shapepoly()                     #获取光标顶点坐标并赋值给v
print(v)                                #打印v的值，输出：((0, 0), (-5, -9), (0, -7), (5, -9))
while True:                             #重复循环
    t.right(90)                         #右转90度
    t.forward(50)                       #前进50步

四、窗体相关设置
1、bgcolor()                             #设定背景颜色
import turtle as t                      #载入turtle当作t
t.speed(1)                              #将速度设定为1
t.bgcolor("red")                        #设定背景为红颜色
while True:                             #重复循环
    t.right(90)                         #右转90度
    t.forward(50)                       #前进50步

2、bgpic()                               #将背景图片设定为
import turtle as t                      #载入turtle当作t
t.speed(1)                              #将速度设定为1
t.bgpic("b1.png")                       #将背景图片设定为b1.png，当前目录图片
while True:                             #重复循环
    t.right(90)                         #右转90度
    t.forward(50)                       #前进50步

3、screensize(宽，高，背景色)               #屏幕设置。
import turtle as t                      #载入turtle当作t
t.speed(1)                              #将速度设定为1
t.screensize(800,800,"blue")            #屏幕设置：宽：800，高：800，背景色：蓝
while True:                             #重复循环
    t.right(90)                         #右转90度
    t.forward(50)                       #前进50步

4、setworldcoordinates(-50,-10,50,10)    #设置世界坐标
import turtle as t                      #载入turtle当作t
t.setworldcoordinates(-30,-50,50,30)    #设置世界坐标，由这四个数控制其开始的位置和形状
for i in range(100):                    #循环100次
    t.forward(i)                        #前进i步
    t.right(90)                         #右转90度

5、delay()                               #延时多少毫秒
import turtle as t                      #载入turtle当作t
t.speed(0)                              #速度设定为0
while True:                             #重复循环
    t.right(90)                         #右转90度
    t.forward(50)                       #前进50步
    t.delay(1000)                       #延时1000毫秒

6、tracer()、t.update()                   #追踪，参数为False，无轨迹效果，True为有轨迹效果
当tracer()参数为False时，表示关闭轨迹，但我们需要刷新屏幕才能看到画面效果。True时会返回其值，
如True = 50，相当于50时间内返回一次画面。数字越小相当于返回的频率越高。
t.tracer(3,25)相当于3时间内返回一次画面，然后每次延时25毫秒。
import turtle as t                      #载入turtle当作t
t.speed(1)                              #速度设定为1
t.tracer(0)                             #参数设定为0表示为False
for i in range(4):                      #循环4次
    t.right(90)                         #右转90度
    t.forward(50)                       #前进50步
t.update()                              #更新屏幕

7、listen()                              #监听
8、onkey()、onkeyrelease()                #当按下，松开
9、onkeypress()                          #当按下
10、onclick()、onscreenclick()            #当点击t.onclick()光标被点击，screen.onclick()屏幕被点击
11、ontimer()、press()                    #screen.ontimer(fun,5000)当时间达到5000毫秒后运行fun
12、mainloop()、done()                    #主循环，保持turtle继续运行。只能放在后面。
import turtle as t
screen = t.Screen()
def u():
    print("y+10")
screen.onkey(u,"Up")
screen.listen()

其他设置
1、mode()            #三种模式“standard”、"logo"、"world"
模式‘standard’与turtle.py兼容。
模式‘logo’与大多数Logo-Turtle-Graphics兼容。
模式‘world’使用用户定义的‘worldcoordinates’。

2、colormode()               #颜色模式
import turtle as t
t.colormode(255)            #颜色模式设为255，gbk颜色值在0-255之间
t.pencolor(0,255,255)

3、getcanvas()               #获取画布
getshapes()                 #获取形状，将图标替换成指定的图标['arrow', 'blank', 'circle', 'classic', 'square', 'triangle', 'turtle']

4、register_shape()、addshape()   #添加形状，将准备好的图片转化成gif格式。
再按t.addshape("hand-2-ss.gif")形式将图标替换。

5、textinput()、numinput()    #文本和数字输入
import turtle as t                          #载入库
my_name = t.textinput("name","your name")   #输入文本
t.write(my_name)                            #写文本
t.mainloop()                                #主循环
#t.bye()            #退出
#t.exitonclick()    #当点击时退出
#t.setup(宽，高，X，Y)          #设置，宽，高，起始X，起始Y。
#t.title()                      #标题
"""
# import turtle as t
# t.colormode(255)            #颜色模式设为255，gbk颜色值在0-255之间
# t.pencolor(0,255,255)
#
# for i in range(4):
#     t.forward(100)
#     t.right(90)
#
# v1 = t.getshapes()
# v2 = t.turtles()
# print(v1)
# for i in v2:
#     print(i)
#
# my_name = t.textinput("name","your name")
# t.write(my_name)
# t.mainloop()


#import turtle as t      #载入turtle当作t
# t.goto(100,100)         #前往x:100,y:100的点
# t.setpos(100,0)         #前往x:100,y:0的点)
# t.setposition(0,100)    #前往x:0,y:100的
# t.setx(50)              #把x设定为50
# t.sety(150)             #把y设定为150
# t.setheading(90)        #把方向设定为90方向
# t.seth(-90)             #把方向设定为-90方向

     #t11，t12，t21，t22(可选)：行列式t11 * t22-t12 * t21不能为零，否则会引起错误。
                             #将背景图片设定为

#画一个圆和内切正方形，填充颜色
