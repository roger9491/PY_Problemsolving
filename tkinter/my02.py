"""面相對象的寫法"""

from tkinter import*
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master=None):
        pass
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.btn01 = Button(self)
        self.btn01["text"] = "點擊送花"
        self.btn01.pack()
        self.btn01["command"] = self.songhua

        self.btnQuit = Button(self, text="退出", command=root.destroy)
        self.btnQuit.pack()

    def songhua(self):
        messagebox.showinfo("送花", "送你99朵")


root = Tk()
root.geometry("400x100+200+300")
root.title("經典gui程序類測試")
app = Application(master=root)

root.mainloop()
