# from tkinter import *
# win = Tk()
# b = Button(win,text = '按钮',font = 14,relief = 'flat',bg='#00f5ff').pack(pady=20)
# win.mainloop()

from tkinter import *
import tkinter.ttk as k
root = Tk()
style = k.Style()
style.configure('TButton',font=14,relief='flat',background='#00f5ff')
b1 = k.Button(text = '按钮1',style='TButton').pack(pady=20)
root.mainloop()