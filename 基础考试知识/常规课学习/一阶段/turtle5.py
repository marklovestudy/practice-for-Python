import turtle as t
import random as r

t.tracer(False)  # 关闭绘制效果
print(t.getshapes())  # 打印出能获得的所有图形
t.bgpic('Forest.png')  # 设置背景图片，PNG
htl = t.Turtle(visible=False, shape='turtle')  # 创建一个对象
htl.setheading(180)  # 设置方向为180
htl.penup()  # 抬笔
xh_x_y = []  # 创建记录XH坐标的列表
x_v = 1  # 设定速度为1
for i in range(1, 1001):  # 循环10次
    xh = htl.clone()  # 克隆
    xh.showturtle()  # 显示克隆体
    xh.goto(r.randint(-445, 445), r.randint(-445, 445))  # 移动随机位置
    xh_x_y.append([xh, x_v])  # 向列表添加克隆体坐标。
while True:  # 无限循环
    for xh in xh_x_y:  # 遍历所有克隆体列表
        xh[0].setx(xh[0].xcor() + xh[1])  # 把x坐标设定为当前x坐标-1
        if xh[0].xcor() < -450 or xh[0].xcor() > 450:  # 如果出界，掉头。
            xh[0].right(180)
        if xh[0].heading() == 180:  # 如果面向的是左边，x加-1
            xh[1] = -1
        if xh[0].heading() == 0:  # 如果面向的是右边，x加1
            xh[1] = 1
    t.update()  # 刷新屏幕
