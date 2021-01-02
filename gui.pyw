import tkinter
import tkinter.messagebox
import random

menu =  ["二楼广东米饭","关中面","愣娃","鸡公煲","蜀香园炒菜米饭","二楼东北饺子","一楼清真","二楼"]

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("吃啥")

        self.label = tkinter.Label(master, text="人生难题解决器", font=("黑体", 32))
        self.label.pack()

        self.generate_button = tkinter.Button(master, text="生成", command=self.generate, font=("黑体", 12), width = 10, height = 2)
        self.generate_button.place(x=100, y=100)

        self.close_button = tkinter.Button(master, text="关闭窗口", command=master.destroy, font=("黑体", 12), width = 10, height = 2)
        self.close_button.place(x=310, y=100)

    def generate(self):
        tkinter.messagebox.showinfo(title = "最终决定", message = random.choice(menu))

if __name__ == '__main__':

	root = tkinter.Tk()
	screen_w = root.winfo_screenwidth()/2-250
	screen_h = root.winfo_screenheight()/2-200
	my_gui = MyFirstGUI(root)
	root.geometry("500x400+%d+%d" % (screen_w,screen_h))
	root.resizable(width=False, height=False)
	root.mainloop()