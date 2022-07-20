import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# root = ttk.Window()  # 不指定使用主题（使用默认的 litera 主题）
root = ttk.Window(themename="united")  # 选择使用 united 主题
root.geometry('800x300')

b1 = ttk.Button(root, text="按钮 1", bootstyle=PRIMARY)
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttk.Button(root, text="按钮 2", bootstyle=(INFO, OUTLINE))
b2.pack(side=LEFT, padx=5, pady=10)

# # 显示所有的属性
# print(root.style.colors)  # 默认的样式全部在这里了
# for color in root.style.colors:
#     b = ttk.Button(root, text=color, bootstyle=color)
#     b.pack(side=LEFT, padx=5, pady=5)

"""设置属性的几种方式"""
# ttk.Button(root, text="Button 2", bootstyle=(INFO,)).pack(side=LEFT, padx=5, pady=10)
# ttk.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE)).pack(side=LEFT, padx=5, pady=10)
# ttk.Button(root, text="Button 2", bootstyle=("info", "outline")).pack(side=LEFT, padx=5, pady=10)
# ttk.Button(root, text="Button 2", bootstyle="outline-info").pack(side=LEFT, padx=5, pady=10)
root.mainloop()
