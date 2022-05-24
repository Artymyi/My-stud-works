from tkinter import *
import socket
from tkinter import ttk
import json
from threading import *
from time import *

class Client_Window(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x330+400+100')
        self.resizable(0, 0)
        self.title('Клиент')
        self.data = dict()

        # зависимость
        # от какого значения
        # до какого значения
        # название оси x
        # название оси y
        # вид линии
        # толщина линии
        # цвет линии
        # наличие сетки

        self.lb1 = Label(self, text='Зависимость', font='Montserrat 10')
        self.en1 = Entry(self, font='Montserrat 14')
        self.lb2 = Label(self, text='От значения', font='Montserrat 10')
        self.en2 = Entry(self, font='Montserrat 14')
        self.lb3 = Label(self, text='До значения', font='Montserrat 10')
        self.en3 = Entry(self, font='Montserrat 14')
        self.lb4 = Label(self, text='Название оси X', font='Montserrat 10')
        self.en4 = Entry(self, font='Montserrat 14')
        self.lb5 = Label(self, text='Название оси Y', font='Montserrat 10')
        self.en5 = Entry(self, font='Montserrat 14')
        self.lb6 = Label(self, text='Вид линии', font='Montserrat 10')
        self.en6 = ttk.Combobox(self, font='Montserrat 14', values=['Пунктир', 'Пунктир-точка', 'Сплошная'], state="readonly")
        self.lb7 = Label(self, text='Толщина линии', font='Montserrat 10')
        self.en7 = Entry(self, font='Montserrat 14')
        self.lb8 = Label(self, text='Цвет линии', font='Montserrat 10')
        self.en8 = ttk.Combobox(self, font='Montserrat 14', values=['Черный', 'Зеленый', 'Красный'], state="readonly")
        self.lb9 = Label(self, text='Наличие сетки', font='Montserrat 10')
        self.en9 = ttk.Combobox(self, font='Montserrat 14', values=['Да', 'Нет'], state="readonly")
        self.bt = Button(self, text='Ввести', font='Montserrat 14', command=self.function1)

        self.en1.place(x=130, y=10)
        self.lb1.place(x=0, y=10)
        self.en2.place(x=130, y=40)
        self.lb2.place(x=0, y=40)
        self.en3.place(x=130, y=70)
        self.lb3.place(x=0, y=70)
        self.en4.place(x=130, y=100)
        self.lb4.place(x=0, y=100)
        self.en5.place(x=130, y=130)
        self.lb5.place(x=0, y=130)
        self.en6.place(x=130, y=160)
        self.lb6.place(x=0, y=160)
        self.en7.place(x=130, y=190)
        self.lb7.place(x=0, y=190)
        self.en8.place(x=130, y=220)
        self.lb8.place(x=0, y=220)
        self.en9.place(x=130, y=250)
        self.lb9.place(x=0, y=250)
        self.bt.place(x=120, y=285)

        recvThread = Thread(target=self.get)
        recvThread.daemon = True
        recvThread.start()

    def function1(self):
        print("Client working")
        self.data['function'] = self.en1.get()
        self.data['from'] = self.en2.get()
        self.data['to'] = self.en3.get()
        self.data['name_x'] = self.en4.get()
        self.data['name_y'] = self.en5.get()
        self.data['type_line'] = self.en6.get()
        self.data['thick_line'] = self.en7.get()
        self.data['colour_line'] = self.en8.get()
        self.data['grid'] = self.en9.get()
        self.client.sendall(bytes(json.dumps(self.data), encoding="utf-8"))

    def get(self):
        while True:
            try:
                print('работает')
                self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client.connect(("127.0.0.1", 1997))
                data = self.client.recv(2048)
                print('Габелла')
                if len(data) != 0:
                    file = open('image.png', mode="wb")
                    while data:
                        file.write(data)
                        data = self.client.recv(2048)
                    file.close()
                    self.root = Toplevel(self)
                    self.photo = PhotoImage(file='image.png')
                    self.label = Label(self.root, image=self.photo)
                    self.label.pack()
                    self.a = 0
                    while self.root.winfo_viewable() == 1:
                        sleep(1)
                    self.root.destroy()
            except:
                pass

s = Client_Window().mainloop()


