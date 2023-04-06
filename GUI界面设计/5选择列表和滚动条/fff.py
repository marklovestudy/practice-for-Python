from tkinter import *
win = Tk()
text = Listbox(win)
text.insert(INSERT,'I love pthon')
text.pack()
print(text.get())
win.mainloop()