#请画一个长方形
import turtle as t
import time

t.tracer(False)         #绘制轨迹，False：关闭效果，

dl=100
while dl>0:
    t.clear()
    #画外框
    t.penup()
    t.goto(-150,250)
    t.pendown()
    t.color('black')
    t.begin_fill()
    for i in range(2):
        t.forward(300)
        t.right(90)
        t.forward(500)
        t.right(90)
    t.end_fill()
    #画内框
    t.penup()
    t.goto(-140,240)
    t.pendown()
    t.color('orange')
    t.begin_fill()
    for i in range(2):
        t.forward(280)
        t.right(90)
        t.forward(440)
        t.right(90)
    t.end_fill()
    #灰色圆圈
    t.penup()
    t.goto(0,-225)
    t.dot(38,'gray')

    #写字
    t.goto(-125,220)
    t.color('black')
    t.write('11月20日   星期日   %d'%dl+'%',font=('黑体',14,'bold'))

    t.goto(-60,-40)
    t.write('欢迎来到\n\nAI人工智能\n\n凤凰机器人\n\npython课堂',font=('黑体',18,'bold'))

    t.goto(-60,150)
    t.write('%s'%time.ctime()[-13:-5],font=('黑体',24,'bold'))
    t.hideturtle()
    time.sleep(1)
    dl -= 1
t.mainloop()
