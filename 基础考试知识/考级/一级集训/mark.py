import turtle as t
t.penup()
t.hideturtle()
v1=[]
v2=[]
v3=[]
v4=[]
v5=[]
v6=[]
def xing(d,h,v):
    t.pendown()
    t.color('yellow')
    t.setheading(h)
    t.begin_fill()
    for i in range(5):
        v.append((t.xcor(),t.ycor()))
        t.forward(d)
        t.right(144)
    t.end_fill()
    t.penup()

def bu(a,v):
    t.pendown()
    t.color('red')
    t.setheading(0)
    t.begin_fill()
    for i in range(2):
        v.append((t.xcor(),t.ycor()))
        t.forward(1.5*a)
        t.right(90)
        v.append((t.xcor(), t.ycor()))
        t.forward(a)
        t.right(90)
    t.end_fill()
    t.penup()

def wxhq(b,x,y):
    t.goto(x,y)
    t.pendown()
    bu(b,v6)
    t.goto(x+0.1*b,y-0.25*b)
    xing(0.25*b,0,v1)
    t.goto(x + 0.42 * b, y - 1/7 * b)
    xing(0.09 * b, 60,v2)
    t.goto(x + 0.51 * b, y - 1.5 / 7 * b)
    xing(0.09 * b, 30,v3)
    t.goto(x + 0.51 * b, y - 2.4 / 7 * b)
    xing(0.09 * b, 0,v4)
    t.goto(x + 0.42 * b, y - 2.9 / 7 * b)
    xing(0.09 * b, -30,v5)
    t.penup()

def square(a,s,v):
    t.pendown()
    t.fillcolor(s)
    t.begin_fill()
    for i in range(4):
        v.append((t.xcor(), t.ycor()))
        t.forward(a)
        t.right(90)
    t.end_fill()
    t.penup()

def sgq(a,n):
    wxhq(a,0,0)
    s = t.Shape('compound')
    s.addcomponent(tuple(v6),'red','red')
    s.addcomponent(tuple(v1),'yellow','yellow')
    s.addcomponent(tuple(v2),'yellow','yellow')
    s.addcomponent(tuple(v3),'yellow','yellow')
    s.addcomponent(tuple(v4),'yellow','yellow')
    s.addcomponent(tuple(v5),'yellow','yellow')
    t.register_shape('flag',s)
    t.clear()

    t.shape('flag')
    t.speed(0)
    t.setheading(90)
    t.goto(0,-100)
    t.showturtle()
    v = t.getscreen()
    v.getcanvas().postscript(file='cc.eps')
    from PIL import Image
    im=Image.open('cc.eps')
    im.save('cc.png')
    for i in range(n):
        t.goto(-100, -50)
        for i in range(3000):
            t.sety(t.ycor()+0.1)

sgq(50,300)
