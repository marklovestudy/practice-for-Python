'''
import turtle
turtle.forward(100)
turtle.backward(100)
turtle.left(90)
turtle.right(90)

#正方形：
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)

三角形：
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)

import turtle as t
t.screensize(400,300,'yellow')
t.setup(1200,800,0,0)

'''
import turtle as t
t.circle(40)
t.circle(-40)
t.forward(80)
t.circle(40)
t.circle(-40)
t.mainloop()
