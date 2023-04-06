import ctypes as cty
from tkinter import *
from tkinter.messagebox import *
from PIL import Image, ImageTk

u32 = cty.windll.user32


def go():
    b_back = u32.GetParent(b.winfo_id())
    win_back = u32.GetParent(l1.winfo_id())
    u32.SetParent(b_back, win_back)

win = Tk()
win.geometry('%sx%s'%(win.winfo_screenwidth(), win.winfo_screenheight()))
win.overrideredirect(True)
win.attributes("-topmost",2)
win.title('嵌套窗口测试')
# win.bind('<Escape>', lambda e: quit())
b = Toplevel()
b.title('未知错误')
b.geometry('300x150+100+100')
b.protocol('WM_DELETE_WINDOW', lambda: showerror('错误', '未知报错'))
Label(b, text='你的电脑被霸占了！！！').pack()
Button(b, text='重启', command=lambda: showerror('重启失败', '未知错误')).pack()
win.bind('<Control-Shift-Alt-F1>', lambda e: quit())


img = Image.open('蓝屏报错.jpg')
img = img.resize((win.winfo_screenwidth(), win.winfo_screenheight()), Image.LANCZOS)
img = ImageTk.PhotoImage(img)
l1 = Label(win, image=img)
l1.pack()
win.after(1, go)
b.attributes("-topmost", 1)
win.mainloop()


