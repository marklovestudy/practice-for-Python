import turtle
import mark
t = turtle.Turtle(shape='turtle')
t.forward(100)

b = turtle.Turtle()
b.right(90)
b.forward(100)

c = turtle.Pen()
c.circle(50)

d = turtle.Pen()
d.left(90)
d.forward(100)
mark.wxhq(200, 100, 0)

v = turtle.getshapes()
print(v)
turtle.mainloop()