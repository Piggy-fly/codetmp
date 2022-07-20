import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('网络调试工具 v0.0.2')
root.geometry('650x500+100+100')
"""左边布局"""
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, anchor=tk.N, padx=5, pady=5)

"""左边布局 网络设置"""
net_frame = tk.LabelFrame(left_frame, text='网络设置', padx=5, pady=5)
net_frame.pack()

tk.Label(net_frame, text='(1)协议类型').pack(anchor=tk.W)
socket_type = ttk.Combobox(net_frame)
socket_type['values'] = ['TCP 服务器', 'TCP 客户端']
socket_type.current(0)
socket_type.pack(anchor=tk.W)

tk.Label(net_frame, text='(2)本地主机地址').pack(anchor=tk.W)
socket_host = ttk.Combobox(net_frame)
socket_host['values'] = ['127.0.0.1', '192.168.0.53']
socket_host.current(0)
socket_host.pack(anchor=tk.W)

tk.Label(net_frame, text='(3)本地端口').pack(anchor=tk.W)
entry_port = ttk.Entry(net_frame)
entry_port.pack(fill=tk.X)

# 按钮
button_frame = tk.Frame(net_frame)
button_frame.pack()

open_button = tk.Button(button_frame, text='打开')
close_button = tk.Button(button_frame, text='关闭')
open_button.pack(side=tk.LEFT)
close_button.pack(side=tk.RIGHT)

"""左边布局 接受设置"""
recv_frame = tk.LabelFrame(left_frame, text='接受设置', padx=5, pady=5)
recv_frame.pack(side=tk.TOP, anchor=tk.N, fill=tk.X)
tk.Radiobutton(recv_frame, text='UTF-8').pack(anchor=tk.W)
tk.Radiobutton(recv_frame, text='GBK').pack(anchor=tk.W)

tk.Checkbutton(recv_frame, text='解析为JSON').pack(anchor=tk.W)
tk.Checkbutton(recv_frame, text='自动换行').pack(anchor=tk.W)

"""左边布局 发送设置"""
recv_frame = tk.LabelFrame(left_frame, text='发送设置', padx=5, pady=5)
recv_frame.pack(side=tk.TOP, anchor=tk.N, fill=tk.X)
tk.Radiobutton(recv_frame, text='UTF-8').pack(anchor=tk.W)
tk.Radiobutton(recv_frame, text='GBK').pack(anchor=tk.W)

tk.Checkbutton(recv_frame, text='数据加密').pack(anchor=tk.W)
tk.Checkbutton(recv_frame, text='信息接受').pack(anchor=tk.W)

"""右边布局"""
right_frame = tk.Frame(root)
right_frame.pack(side=tk.TOP, padx=5, pady=5)

info_frame = tk.Frame(right_frame)
info_frame.pack()
tk.Label(info_frame, text='数据日志').pack(anchor=tk.W)

text_pad = tk.Text(info_frame, width=62)
text_pad.pack(side=tk.LEFT, fill=tk.X)

send_text_bar = tk.Scrollbar(info_frame)
send_text_bar.pack(side=tk.RIGHT, fill=tk.Y)
tk.Label(right_frame, text='信息发送').pack(anchor=tk.W)

send_frame = tk.Frame(right_frame)
send_frame.pack()

send_area = tk.Text(send_frame, width=58, height=6)
send_area.pack(side=tk.LEFT)
send_button = tk.Button(send_frame, text='发送', width=5)
send_button.pack(side=tk.RIGHT, fill=tk.Y)
root.mainloop()
