from tkinter import *
import matplotlib.pyplot as plt
import socket
import json
from threading import *
from time import *
from math import *
import numpy as np

class Server_Window(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x120+400+100')
        self.resizable(0, 0)
        self.title('Сервер')
        self.var = IntVar()
        self.var.set(3)

        self.lb1 = Label(self, text='Установите ограничения\nна адреса клиента', font='Montserrat 14')
        self.rad0 = Radiobutton(self, text="Любые адреса", variable=self.var, value=0, font='Montserrat 11')
        self.rad1 = Radiobutton(self, text="Конкретные", variable=self.var, value=1, font='Montserrat 11', command=self.enter)
        self.lb2 = Label(self)
        self.rad0.place(x=130, y=60)
        self.rad1.place(x=130, y=85)
        self.lb1.place(x=100, y=10)
        self.lb2.place(x=100, y=170)

        self.host = '127.0.0.1'
        self.client_ip = ''
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, 1997))
        self.server.listen(1)

        recvThread = Thread(target=self.sendr)
        recvThread.daemon = True
        recvThread.start()

    def sendr(self):
        print("Server working...")
        while True:
            try:
                sleep(1)
                if self.var.get() != 3:
                    print('is working')
                    if self.var.get() == 0:
                        while True:
                            print('заход в б цикл для любого айпи')
                            self.client, self.address = self.server.accept()  #  принимаем входящее соединение
                            print('Пизда')
                            self.data = self.client.recv(1024).decode("utf-8")
                            print('пизда 1')
                            self.data_obj = json.loads(self.data)
                            self.func = self.data_obj['function']
                            self.froms = self.data_obj['from']
                            self.to = self.data_obj['to']
                            self.name_x = self.data_obj['name_x']
                            self.name_y = self.data_obj['name_y']
                            self.type_line = self.data_obj['type_line']
                            self.thick_line = self.data_obj['thick_line']
                            self.colour_line = self.data_obj['colour_line']
                            self.drids = self.data_obj['grid']
                            self.x = [i for i in range(int(self.froms), int(self.to) + 1)]
                            self.y = self.func_eval(self.x, self.func)

                            if self.type_line == 'Пунктир':
                                self.type_lines = '--'
                            elif self.type_line == 'Пунктир-точка':
                                self.type_lines = '-.'
                            elif self.type_line == 'Сплошная':
                                self.type_lines = '-'

                            if self.colour_line == 'Черный':
                                self.colour_lines = '#000000'
                            elif self.colour_line == 'Зеленый':
                                self.colour_lines = '#008000'
                            elif self.colour_line == 'Красный':
                                self.colour_lines = '#ff0000'

                            self.fig = plt.figure()
                            plt.plot(self.x, self.y, linestyle=self.type_lines, lw=int(self.thick_line), c=self.colour_lines)
                            plt.xlabel(self.name_x)
                            plt.ylabel(self.name_y)
                            if self.drids == 'Да':
                                plt.grid()
                            plt.savefig('figure.png')


                            self.file = open('figure.png', mode="rb")
                            self.data = self.file.read(2048)
                            while self.data:
                                self.client.send(self.data)
                                self.data = self.file.read(2048)
                            self.file.close()
                            self.client.close()
                            # plt.close()
                            break

                    elif self.var.get() == 1:
                        while '.' not in self.client_ip:
                            # self.client, self.address = self.server.accept()  # принимаем входящее соединение
                            print('хуево')
                        print('заебись, идем дальше')
                        self.client, self.address = self.server.accept()
                        if self.address[0] != self.client_ip:
                            self.client.close()
                            print('Наебатор')
                        else:
                            while True:
                                print('заход в б цикл для конкретного айпи')
                                # self.client, self.address = self.server.accept()  # принимаем входящее соединение
                                print('Пизда')
                                self.data = self.client.recv(1024).decode("utf-8")
                                print('пизда 1')
                                self.data_obj = json.loads(self.data)
                                self.func = self.data_obj['function']
                                self.froms = self.data_obj['from']
                                self.to = self.data_obj['to']
                                self.name_x = self.data_obj['name_x']
                                self.name_y = self.data_obj['name_y']
                                self.type_line = self.data_obj['type_line']
                                self.thick_line = self.data_obj['thick_line']
                                self.colour_line = self.data_obj['colour_line']
                                self.drids = self.data_obj['grid']
                                self.x = [i for i in range(int(self.froms), int(self.to) + 1)]
                                self.y = self.func_eval(self.x, self.func)

                                if self.type_line == 'Пунктир':
                                    self.type_lines = '--'
                                elif self.type_line == 'Пунктир-точка':
                                    self.type_lines = '-.'
                                elif self.type_line == 'Сплошная':
                                    self.type_lines = '-'

                                if self.colour_line == 'Черный':
                                    self.colour_lines = '#000000'
                                elif self.colour_line == 'Зеленый':
                                    self.colour_lines = '#008000'
                                elif self.colour_line == 'Красный':
                                    self.colour_lines = '#ff0000'

                                self.fig = plt.figure()
                                plt.plot(self.x, self.y, linestyle=self.type_lines, lw=int(self.thick_line),
                                         c=self.colour_lines)
                                plt.xlabel(self.name_x)
                                plt.ylabel(self.name_y)
                                if self.drids == 'Да':
                                    plt.grid()
                                plt.savefig('figure.png')

                                self.file = open('figure.png', mode="rb")
                                self.data = self.file.read(2048)
                                while self.data:
                                    self.client.send(self.data)
                                    self.data = self.file.read(2048)
                                self.file.close()
                                self.client.close()
                                # plt.close()
                                break
            except:
                pass

    def enter(self):
        self.baby_root = Toplevel(self)
        self.baby_root.title('Ввод адреса')
        self.baby_root.resizable(0, 0)
        self.baby_root.geometry('300x150+400+200')

        self.lb1 = Label(self.baby_root, text='Введите адрес', font='Montserrat 14')
        self.en1 = Entry(self.baby_root, text='Введите адрес', font='Montserrat 14')
        self.bt1 = Button(self.baby_root, text='Ввести', font='Montserrat 14', command=self.enter_host)

        self.en1.place(x=40, y=70)
        self.lb1.place(x=75, y=30)
        self.bt1.place(x=100, y=100)

    def enter_host(self):
        self.client_ip = self.en1.get()
        self.baby_root.destroy()

    def func_eval(self, spisok, zavisimost):
        y = list()
        for i in range(len(spisok)):
            x = spisok[i]
            y.append(eval(zavisimost))
        return y

s = Server_Window().mainloop()
