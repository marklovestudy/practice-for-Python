#第一步：下载一张gif图片：11.gif
# #第二步：注册光标
# t.register_shape('11.gif')
# #第三步：使用光标11.gif
# def p():
# #     print('上')
import turtle as t
screen=t.Screen()
t.penup()
def u(f,d):
    t.setheading(f)
    t.forward(d)
    t.update()
def p(x,y):
    a.clear()
    t.goto(x,y)
    a.goto(t.xcor()+50,t.ycor()+60)
    a.write('我叫:%s,身高：%s'%(name,tall))
    t.update()
t.addshape('11.gif')
print(t.getshapes())
t.shape('11.gif')
t.onkey(lambda :u(90,10),'Up')
t.onkey(lambda :u(270,10),'Down')
t.onkey(lambda :u(180,10),'Left')
t.onkey(lambda :u(0,10),'Right')
v=screen.onscreenclick(p)
a=t.Turtle()
a.penup()
name=t.textinput('your name','name:')
tall=t.numinput('how tall','tall',1.7,0.55,2.8)
t.update()
t.listen()
t.mainloop()
#1 创建一个新的笔a         a=t.Turtle()
#2 用textinput()、numinput()获取输出信息。       name=textinput()   tall=numinput()
#3 a移到角色右上方说：‘我叫什么名字，我的身高是多少。’
# a.goto(t.xcor()+50,t.ycor()+60)   a.write('我叫:%s,身高：%s'%(name,tall))
#要求是：这一句话跟随人物角色。