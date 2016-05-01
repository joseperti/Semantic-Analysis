# -*- coding: utf-8 -*-
from tkinter import *
from pymongo import *
import datetime

class Interfaz:
    def __init__(self):
        self.root = Tk()
        self.root.title("Esto es una ventana molona")
        self.mainframe = Frame(master=self.root)
        self.entradaTexto = Text(master = self.root,height=4,width=60)
        Button(master=self.root,text="Cargar datos").pack()
        Text(master = self.root,height=1,width=40).pack()
        self.entradaTexto.pack()
        Button(master=self.root,text="Procesar texto").pack()
        self.root.mainloop()

if __name__ == "__main__":
    print("Hello World")
    interf = Interfaz()
