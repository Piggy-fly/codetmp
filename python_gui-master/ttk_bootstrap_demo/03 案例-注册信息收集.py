import ttkbootstrap as tk
import ttkbootstrap.constants as tkc

root = tk.Window(themename='litera')
root.geometry('350x500+500+500')
root.title('萌新-注册页面')
root.wm_attributes('-topmost', 1)

username_str_var = tk.StringVar()
password_str_var = tk.StringVar()

# 0 女 1 男 -1 保密
gender_str_var = tk.IntVar()
# 兴趣爱好
hobby_list = [
    [tk.IntVar(), '吃'],
    [tk.IntVar(), '喝'],
    [tk.IntVar(), '玩'],
    [tk.IntVar(), '乐'],
]

# 账户信息
tk.Label(root, width=10).grid()
tk.Label(root, text='用户名：').grid(row=1, column=1, sticky=tk.W, pady=10)
tk.Entry(root, textvariable=username_str_var).grid(row=1, column=2, sticky=tk.W)
tk.Label(root, text='密  码：').grid(row=2, column=1, sticky=tk.W, pady=10)
tk.Entry(root, textvariable=password_str_var).grid(row=2, column=2, sticky=tk.W)

# 性别 单选框
tk.Label(root, text='性别：').grid(row=4, column=1, sticky=tk.W, pady=10)
radio_frame = tk.Frame()
radio_frame.grid(row=4, column=2, sticky=tk.W)
tk.Radiobutton(radio_frame, text='男', variable=gender_str_var, value=1).pack(side=tk.LEFT, padx=5)
tk.Radiobutton(radio_frame, text='女', variable=gender_str_var, value=0).pack(side=tk.LEFT, padx=5)
tk.Radiobutton(radio_frame, text='保密', variable=gender_str_var, value=-1).pack(side=tk.LEFT, padx=5)

# 兴趣爱好
tk.Label(root, text='兴趣：').grid(row=6, column=1, sticky=tk.W, pady=10)
check_frame = tk.Frame()
check_frame.grid(row=6, column=2, sticky=tk.W)
tk.Checkbutton(check_frame, text=hobby_list[0][1], variable=hobby_list[0][0]).pack(side=tk.LEFT, padx=5)
tk.Checkbutton(check_frame, text=hobby_list[1][1], variable=hobby_list[1][0], bootstyle="square-toggle").pack(
    side=tk.LEFT, padx=5)
tk.Checkbutton(check_frame, text=hobby_list[2][1], variable=hobby_list[2][0], bootstyle="round-toggle").pack(
    side=tk.LEFT, padx=5)
tk.Checkbutton(check_frame, text=hobby_list[3][1], variable=hobby_list[3][0]).pack(side=tk.LEFT, padx=5)

# 生日
tk.Label(root, text='生日：').grid(row=7, column=1, sticky=tk.W, pady=10)
data_entry = tk.DateEntry()
data_entry.grid(row=7, column=2, sticky=tk.W, pady=10)
print(data_entry.entry.get())

# print(birth_day.get())

tk.Label(root, text="").grid(row=9, column=2, sticky=tk.W)
button = tk.Button(root, text='提交', width=20)
button.grid(row=10, column=2, sticky=tk.W)


def get_info():
    data = {
        'username': username_str_var.get(),
        'password': password_str_var.get(),
        'gender': gender_str_var.get(),
        'hobby': [h for v, h in hobby_list if v.get()],
        'birth': data_entry.entry.get()
    }
    print(data)


button.config(command=get_info)
root.mainloop()
