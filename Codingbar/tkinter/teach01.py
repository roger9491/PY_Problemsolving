import tkinter
from tkinter import *
import time
window = tkinter.Tk()

window.title("test")

window.geometry("250x250+500+100")

window.maxsize(500, 500)
window.minsize(100, 100)

window.resizable(1, 1)
entry_1 = Entry(window,font=("微軟正黑體",40))
entry_1.pack()

btn1 = Button(window, text="測試1",command=lambda:lab_n(entry_1.get())).pack(fill=BOTH,expand=1)

def lab_n(string):
    Label(window,text=string).pack()


time_string = time.asctime()

label_1 = Label(window,text=time_string)
label_1.pack()

def gettime():
    global time_string
    print(1)
    time_string = time.asctime()
    window.after(1000, gettime) 
gettime()


window.mainloop()
