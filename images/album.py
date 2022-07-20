import tkinter as tk
import glob

from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('906x687+100+100')
root.title('图片查看器')

photos = glob.glob('photo/*.jpg')
photos = [ImageTk.PhotoImage(Image.open(photo)) for photo in photos]

current_photo_no = 0
photo_label = tk.Label(root, image=photos[current_photo_no], width=900, height=600)
photo_label.pack()

number_var = tk.StringVar()
number_var.set('1 of 4')
tk.Label(root, textvariable=number_var, bd=1, relief=tk.SUNKEN, anchor=tk.CENTER).pack(fill=tk.X)

button_frame = tk.Frame(root)
button_frame.pack()
prev_photo = tk.Button(button_frame, text='上一页')
next_photo = tk.Button(button_frame, text='下一页')
prev_photo.pack(side=tk.LEFT, anchor=tk.CENTER)
next_photo.pack(side=tk.RIGHT, anchor=tk.CENTER)


def change_photos(next_no):
    global current_photo_no
    current_photo_no += next_no
    if current_photo_no >= len(photos):
        current_photo_no = 0
    if current_photo_no < 0:
        current_photo_no = len(photos) - 1
    number_var.set(f'{current_photo_no + 1} of {len(photos)}')
    photo_label.configure(image=photos[current_photo_no])


prev_photo.config(command=lambda: change_photos(-1))
next_photo.config(command=lambda: change_photos(1))
root.mainloop()
