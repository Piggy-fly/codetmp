import tkinter as tk
from tkinter import ttk
from db import db


class AboutFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        tk.Label(self, text='关于作品：本作品由tkinter制作').pack()
        tk.Label(self, text='关于作者：群里最弱的萌新').pack()
        tk.Label(self, text='版权所有：B站号-群里最弱的萌新').pack()


class ChangeFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.name = tk.StringVar()
        self.math = tk.StringVar()
        self.chinese = tk.StringVar()
        self.english = tk.StringVar()
        self.status = tk.StringVar()
        self.create_page()

    def create_page(self):
        tk.Label(self).grid(row=0, pady=10)

        tk.Label(self, text='姓 名：').grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=1, column=2, pady=10)

        tk.Label(self, text='数 学：').grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.math).grid(row=2, column=2, pady=10)

        tk.Label(self, text='语 文：').grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.chinese).grid(row=3, column=2, pady=10)

        tk.Label(self, text='英 语：').grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.english).grid(row=4, column=2, pady=10)

        tk.Button(self, text='查询', command=self.search_user).grid(row=5, column=1, pady=10)
        tk.Button(self, text='修改', command=self.change_user).grid(row=5, column=2, pady=10)

        tk.Label(self, textvariable=self.status).grid(row=6, column=2, pady=10, stick=tk.E)

    def search_user(self):
        flag, info = db.search_by_username(self.name.get())
        if flag:
            self.name.set(info['name'])
            self.math.set(info['math'])
            self.chinese.set(info['chinese'])
            self.english.set(info['english'])
            self.status.set('数据查询成功')
        else:
            self.status.set(info)

    def change_user(self):
        stu = {"name": self.name.get(), "math": self.math.get(),
               "chinese": self.chinese.get(), "english": self.english.get()}
        self.name.set('')
        self.math.set('')
        self.chinese.set('')
        self.english.set('')
        db.update(stu)
        self.status.set('修改数据成功')


class InsertFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        # tk.Label(self, text='插入页面').pack()
        self.name = tk.StringVar()
        self.math = tk.StringVar()
        self.chinese = tk.StringVar()
        self.english = tk.StringVar()
        self.status = tk.StringVar()
        self.create_page()

    def create_page(self):
        tk.Label(self).grid(row=0, pady=10)

        tk.Label(self, text='姓 名：').grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=1, column=2, pady=10)

        tk.Label(self, text='数 学：').grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.math).grid(row=2, column=2, pady=10)

        tk.Label(self, text='语 文：').grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.chinese).grid(row=3, column=2, pady=10)

        tk.Label(self, text='英 语：').grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.english).grid(row=4, column=2, pady=10)

        tk.Button(self, text='录入', command=self.recode_info).grid(row=5, column=2, pady=10)

        tk.Label(self, textvariable=self.status).grid(row=6, column=2, pady=10, stick=tk.E)

    def recode_info(self):
        stu = {"name": self.name.get(), "math": self.math.get(),
               "chinese": self.chinese.get(), "english": self.english.get()}
        self.name.set('')
        self.math.set('')
        self.chinese.set('')
        self.english.set('')
        db.insert(stu)
        self.status.set('提交数据成功')


class DeleteFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.username = tk.StringVar()
        self.status = tk.StringVar()
        tk.Label(self, text='根据名字删除数据').pack()
        tk.Entry(self, textvariable=self.username).pack()
        tk.Button(self, text='删除', command=self.delete).pack()
        tk.Label(self, textvariable=self.status).pack()

    def delete(self):
        username = self.username.get()
        flag, message = db.delete_by_username(username)
        self.status.set(message)


class SearchFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.table_view = tk.Frame()
        self.table_view.pack()

        self.create_page()

    def create_page(self):
        columns = ("name", "chinese", "math", "english")
        columns_values = ("姓名", "语文", "数学", "英语")
        self.tree_view = ttk.Treeview(self, show='headings', columns=columns)
        self.tree_view.column('name', width=80, anchor='center')
        self.tree_view.column('chinese', width=80, anchor='center')
        self.tree_view.column('math', width=80, anchor='center')
        self.tree_view.column('english', width=80, anchor='center')
        self.tree_view.heading('name', text='姓名')
        self.tree_view.heading('chinese', text='语文')
        self.tree_view.heading('math', text='数学')
        self.tree_view.heading('english', text='英语')
        self.tree_view.pack(fill=tk.BOTH, expand=True)
        self.show_data_frame()

        tk.Button(self, text='刷新数据', command=self.show_data_frame).pack(anchor=tk.E, pady=5)

    def show_data_frame(self):
        # 删除旧的阶段
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass

        students = db.all()
        index = 0
        for stu in students:
            self.tree_view.insert('', index + 1, values=(
                stu['name'], stu['math'], stu['chinese'], stu['english'],
            ))
