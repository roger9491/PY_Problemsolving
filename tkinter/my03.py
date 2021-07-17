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
        self.label01 = Label(self, text="百度程序員", width=10,
                             height=2, bg="black", fg="white")
        self.label01.pack()

        self.label02 = Label(self, text="老師1", width=10,
                             height=2, bg="blue", fg="white", font=("黑體", 30))
        self.label02.pack()

        # 顯示圖像
        global photo
        photo = PhotoImage(file="img/2020-03-08.gif")
        self.lable03 = Label(self, image=photo)
        self.lable03.pack()


root = Tk()
root.geometry("400x400+200+300")
root.title("經典gui程序類測試")
app = Application(master=root)

root.mainloop()
