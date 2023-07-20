import turtle as t
import time
n=eval(input('n?'))
for i in range(n,0,-1):
    t.clear()
    t.write('休息{}秒'.format(str(i)),font=('alril',24,'bold'))
    t.update()
    time.sleep(1)
