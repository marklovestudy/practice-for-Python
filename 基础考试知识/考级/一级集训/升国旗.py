import turtle as t
#如何记录坐标
xy = []
for i in range(5):
    xy.append((t.xcor(),t.ycor()))
    t.forward(100)
    t.right(144)
print(xy)

#如何注册图形
s = t.Shape('compound')
s.addcomponent(tuple(xy),'yellow','yellow')
s.addcomponent(((0,0),(100,20),(-50,80)),'red','red')
t.register_shape('xx',s)
print(t.getshapes())
t.shape('xx')
t.forward(100)
t.mainloop()