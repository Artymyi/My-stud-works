from tkinter import *
import matplotlib.pyplot as plt

# languages = [("Python", 1), ("JavaScript", 2), ("C#", 3), ("Java", 4)]
#
#
# def select():
#     l = language.get()
#     if l == 1:
#         sel.config(text="Выбран Python")
#     elif l == 2:
#         sel.config(text="Выбран JavaScript")
#     elif l == 3:
#         sel.config(text="Выбран C#")
#     elif l == 4:
#         sel.config(text="Выбран Java")
#
#
# root = Tk()
# root.title("GUI на Python")
# root.geometry("300x280")
#
# header = Label(text="Выберите курс", padx=15, pady=10)
# header.grid(row=0, column=0, sticky=W)
#
# language = IntVar()
#
# row = 1
# for txt, val in languages:
#     Radiobutton(text=txt, value=val, variable=language, padx=15, pady=10, command=select).grid(row=row, sticky=W)
#     row += 1
#
# sel = Label(padx=15, pady=10)
# sel.grid(row=row, sticky=W)
#
# root.mainloop()
#
# a = 'x**2'
#
# y = [x**2 for x in range(3)]
# print(y)
# x = [1, 3, 4, 5]
# f = 'x ** 2'
# def func(a, f):
#     y = list()
#     for i in range(len(a)):
#         x = a[i]
#         y.append(eval(f))
#     return y
# y = func(x, f)
# name_x = 'хуй'
# name_y = 'жопа'
# drids = 'Да'
# fig = plt.figure()
# plt.plot(x, y, linestyle='-')
# plt.xlabel(name_x)
# plt.ylabel(name_y)
# if drids == 'Да':
#     plt.grid()
# plt.show()
#
# import socket
# host = '192.168.43.225'
# port = 2000
# sock = socket.socket()
# sock.connect((host, port))
# sock.send('hello, world!'.encode('utf-8'))
#
# sock.close()
import numpy as np
import matplotlib.pyplot as plt
from math import *
x = np.linspace(-10, 10, 1000)
y = x**3

fig, ax = plt.subplots()                        # будет 1 график, на нем:
ax.plot(x, y, color="blue", label="y(x)")      # функция y1(x), синий, надпись y(x)
ax.set_xlabel("x")                              # подпись у горизонтальной оси х
ax.set_ylabel("y")                              # подпись у вертикальной оси y
ax.legend()                                     # показывать условные обозначения

plt.show()                                      # показать рисунок
fig.savefig('1.png')

# for i in range(0, 10):
#     print(i)
# print([i for i in range(float(-10), float(10) + 1)])