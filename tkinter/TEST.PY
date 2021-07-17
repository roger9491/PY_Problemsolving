import tkinter as tk
import time
# 创建Tk对象，Tk代表窗口
root =tk.Tk()
# 设置窗口标题
root.title('入门案例')
# 创建Label对象，第一个参数指定该Label放入root


def gettime():
    var.set(time.strftime("%H:%M:%S"))  # 获取当前时间
    root.after(1000, gettime)  # 每隔1s调用函数 gettime 自身获取时间
var=tk.StringVar()
w =tk.Label(root,textvariable=var,fg='blue',font=("微软雅黑",40))

# 调用pack进行布局
w.pack()
 
#测试用途

#测试用途
goBtn = tk.Button(text="测试",command=gettime,fg='blue',font=("黑体",20))
goBtn.pack()
 
# 启动主窗口的消息循环
root.mainloop()
