import tkinter111 as tk
import mark as m
import pyga,sys
def pg():
    pyga.init()
    screen = pyga.display.set_mode((800, 600))
    my_ball = pyga.image.load("ball.png")
    screen.fill([255,255,255])
    screen.blit(my_ball,(50,50))
    pyga.time.delay(2000)
    screen.blit(my_ball,(200,50))
    pyga.draw.rect(screen, [255, 255, 255], [50, 50, 165, 180], 0)
    pyga.display.update()
    while True:
        for event in pyga.event.get():
            if event.type == pyga.QUIT:
                sys.exit()

def xx():
    pyga.init()
    screen = pyga.display.set_mode((800, 600))
    my_1 = pyga.image.load("rat1.png")
    screen.fill([255, 255, 255])
    x = 50
    y = 50
    screen.blit(my_1, (x, y))
    while True:
        for event in pyga.event.get():
            if event.type == pyga.QUIT:
                sys.exit()
        pyga.time.delay(20)
        pyga.draw.rect(screen, [255, 255, 255], [x, y, 165, 165], 0)
        x += 1
        y += 0
        screen.blit(my_1, (x, y))
        if x > screen.get_width():
            x = -50
        pyga.display.flip()

win = tk.Tk()
win.title('红旗')
win.geometry('100x200+0+0')

l = tk.Label(win,text = 'hello world',bg = 'green',
             fg = 'white',font = ('Arial',12),width = 30,height =2 )
l.pack()

def hit():
    m.sgq(100,5)

b = tk.Button(win,text = '升国旗',fg = 'red',
              font = ('Arial',12),width = 30,height =2,command = hit)
b.pack()
c = tk.Button(win,text = '球',fg = 'red',
              font = ('Arial',12),width = 30,height =2,command = pg)
c.pack()
d = tk.Button(win,text = 'mouse',fg = 'red',
              font = ('Arial',12),width = 30,height =2,command = xx)
d.pack()
win.mainloop()