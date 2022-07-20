import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# root = tk.Tk()  # 使用 tkinter 创建窗口对象
root = ttk.Window()  # 使用 ttkbootstrap 创建窗口对象

root.geometry('500x300')

b1 = ttk.Button(root, text="按钮 1", bootstyle=SUCCESS)  # bootstyle 属性用于设置按钮的样式
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttk.Button(root, text="按钮 2", bootstyle=(SUCCESS, OUTLINE))  # OUTLINE 属性用于按钮的边框线
b2.pack(side=LEFT, padx=5, pady=10)

root.mainloop()
