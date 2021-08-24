import tkinter
import time
from tkinter import *
import calendar
from tkinter.filedialog import *

window = tkinter.Tk()
window.title("時間小幫手")
window.geometry("600x600+650+250")

# 建立 帳號 label
label_1 = Label(window, text="帳號", bg="azure2", font=('微軟正黑體', 40))
label_1.pack()

# 建立帳號輸入
entry_1 = Entry(window, bg="snow", bd=0, width=30, font=('微軟正黑體', 20))
entry_1.pack()


# 密碼label
label_2 = Label(window, text="密碼", bg="azure2", font=('微軟正黑體', 40))
label_2.pack()


# 建立密碼輸入
entry_2 = Entry(window, bg="snow", bd=0, width=30,
                font=('微軟正黑體', 20), show="*")
entry_2.pack()

# 建立登入按鈕
btn_1 = Button(window, text="登陸", bg="dodger blue",
               fg="white", font=('微軟正黑體', 20), relief=RAISED, command=lambda: login(entry_1.get(), entry_2.get()))
btn_1.pack(side=BOTTOM, pady=20)

# 登陸函式

def login(account, password):
    if account == "123" and password == "123":
        label_1.pack_forget()
        label_2.pack_forget()
        entry_1.pack_forget()
        entry_2.pack_forget()
        btn_1.pack_forget()
        # 登陸進來的時間小幫手畫面
        btn_time.pack(fill=X, pady=40)
        btn_notebook.pack(fill=X, pady=40)
        btn_countdown.pack(fill=X, pady=40)




##時間小幫手選項
            
btn_time = Button(window, text="時鐘", font=(
    '微軟正黑體', 20), height=3, command=lambda: clock())


btn_notebook = Button(window, text="記事本", font=(
    '微軟正黑體', 20), height=3, command=lambda: notebook())


btn_countdown = Button(window, text="倒數計時器", font=(
    '微軟正黑體', 20), height=3, command=lambda: countdown())

x = StringVar()
x.set(time.asctime())
def gettime():
    global x
    x.set(time.asctime())
    window.after(1000, gettime)  # 每隔1s调用函数 gettime 自身获取时间

def clock():
    gettime()
    time_page = Toplevel()
    time_page.title("時鐘")

    lab1 = Label(time_page, textvariable=x, font=('微軟正黑體', 40))
    lab1.pack()

def notebook():
    notebook_page = Toplevel()
    notebook_page.title("記事本")
    textPad=Text(notebook_page)
    textPad.pack(expand=YES,fill=BOTH)
    btn1 = Button(notebook_page, bd=0,bg="dodger blue",
                text="保存", font=('微軟正黑體', 20),command=lambda :mysaveas()).pack(side=BOTTOM)
   
    def mysaveas():
        f=asksaveasfilename(initialfile="未命名.txt",defaultextension=".txt")
        fh=open(f,'w')
        msg=textPad.get(1.0,END)
        fh.write(msg)
        fh.close()
        

def countdown():
    countdown_page = Toplevel()
    countdown_page.title("倒數計時器")

    text = Label(countdown_page,text="輸入秒數", font=('微軟正黑體', 20)).pack(side=LEFT)
    entry_1 = Entry(countdown_page, bg="snow", bd=0,
                    width=30, font=('微軟正黑體', 20))
    entry_1.pack(side=LEFT)
    
    btn = Button(countdown_page, bd=0,bg="dodger blue",
                text="輸入", font=('微軟正黑體', 20),command=lambda :check())
    btn.pack(side=LEFT)
    var = StringVar()
    var.set("秒數")
    text = Label(countdown_page,textvariable=var, font=('微軟正黑體', 20)).pack()
    second = 0
    def check():
        global second
        if entry_1.get().isdigit():
            second = int(entry_1.get())
            start()
        else:
            var.set("輸入錯誤秒數")

    def start():
        global second
        if second < 0:
            var.set("time's up!")
        else:
            var.set(str(second))
            second -= 1
            countdown_page.after(1000, start)





window.mainloop()
