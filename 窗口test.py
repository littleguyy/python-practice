# python 3.6.3

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        #print(self.hi_there.config())
        self.hi_there["height"]=3
        self.hi_there["width"]=10
        self.hi_there["text"] = "你好世界\n(点我)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="退出", fg="red", height=2, width=10, command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("这是一个python3.6版本的窗口程序测试！")

root = tk.Tk()
root.geometry('{}x{}'.format(300, 150))
#root.resizable(0, 0)
app = Application(master=root)
app.master.title("我的python3.6窗口程序")

#app.master.minsize(700, 300)
#app.master.maxsize(700, 300)

app.mainloop()
