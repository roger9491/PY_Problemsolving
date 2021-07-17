from tkinter import *
from tkinter import messagebox


root = Tk()  # 建立窗口對象

root.title("教學")
root.geometry("500x300+800+400")

lb1 = Listbox(root,bd=2,width=40,font=("Courier",14))
lb1.insert(END,"PY")
lb1.insert(END,"java")
lb1.insert(END,"c")
lb1.pack()



btn01 = Button(root)
btn01["text"] = "點我就送花"
btn01.pack()


def songhua(e):  # e 就是事件對象
    messagebox.showinfo("Message", "送你一朵花")
    print("99朵")


btn01.bind("<Button-1>", songhua)


root.mainloop()  # 調用該對象的mainloop() 方法,進入事件循環
