import turtle as t
t.speed(0)
t.pensize(7)            #画笔的粗细设定为7
#蓝blue、黄yellow、黑black、绿green、红red。
#(-110,60)(0,60)(110,60)(-55,5)(55,5)
#蓝色圈
t.penup()               #抬笔
t.goto(-110,60)         #移到坐标（-110，60）
t.pendown()             #落笔
t.color('blue')         #将画笔的颜色设定为：'blue'
t.circle(45)            #画半径为45的圆
#黄色圈
t.penup()
t.goto(0,60)
t.pendown()
t.color('yellow')
t.circle(45)
#黑色圈
t.penup()
t.goto(110,60)
t.pendown()
t.color('black')
t.circle(45)
#绿色圈
t.penup()
t.goto(-55,5)
t.pendown()
t.color('green')
t.circle(45)
#红色圈
t.penup()
t.goto(55,5)
t.pendown()
t.color('red')
t.circle(45)

#彩虹
colors = ['red','orange','yellow','green','blue','indigo','purple']
x = 250                         #设定x坐标为250
for i in colors:                #遍历列表
 t.setheading(90)            #面向90方向
 t.penup()                   #抬笔
 t.goto(x,0)                 #移到坐标（x,0）
 t.pendown()                 #落笔
 t.color(i)                  #颜色
 t.circle(x,180)             #画圆，半径为x,角度为180
 x -= 7                      #将x减少7
pic1=t.getscreen().getcanvas().postscript(file='aa.eps')
t.mainloop()                    #内循环，主循环
