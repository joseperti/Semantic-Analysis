# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.filedialog import *
from pymongo import *
import datetime

class Interfaz:
    def __init__(self):
        self.root = Tk()
        self.root.title("Herramienta de clasificación")
        self.root.geometry("1080x640")
        self.mainframe = Frame(master=self.root)
        self.cargarMenu()
        self.cargarColumnas()
        self.root.mainloop()

    def cargarMenu(self):
        self.menuBar = Menu(self.root)

        #Menú de Archivo
        self.filemenu = Menu(self.menuBar, tearoff=0)
        self.filemenu.add_command(label="Abrir", command=self.hello)
        self.filemenu.add_command(label="Guardar", command=self.guardarArchivo)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Importar", command=self.importarArchivo)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.root.quit)
        self.menuBar.add_cascade(label="File", menu=self.filemenu)

        #Menú de Clasificación
        self.clasifMenu = Menu(self.menuBar, tearoff=0)
        self.clasifMenu.add_command(label="Test de clasificación", command=self.ejemplosTextos)
        self.clasifMenu.add_command(label="Clasificar Todos", command=self.hello)
        self.menuBar.add_cascade(label="Clasificación", menu=self.clasifMenu)

        self.root.config(menu = self.menuBar)

    def cargarColumnas(self):

        self.listaIzq = Listbox(self.root)

        self.menuListaIzq = Menu(self.root, tearoff=0)
        self.menuListaIzq.add_command(label="Positivo", command=self.mandarPositivo)
        self.menuListaIzq.add_command(label="Negativo", command=self.mandarNegativo)
        self.listaIzq.bind('<Button-3>',self.popupListaIzq)
        self.listaIzq.pack(side=LEFT,fill=BOTH,expand=1)

        self.listaDer = Listbox(self.root)
        self.listaDer.pack(side=RIGHT,fill=BOTH,expand=1)

    def popupListaIzq(self,event):
        self.seleccionIzq = self.listaIzq.curselection()
        #print(self.seleccion)
        if len(self.seleccionIzq)>0:
            self.menuListaIzq.post(event.x_root, event.y_root)

    def eliminarElmListaIzq(self,el):
        self.listaIzq.delete(el)

    def mandarPositivo(self):
        for k in self.seleccionIzq:
            valor = str(self.listaIzq.get(k, k)[0])
            # print("Negativo: "+valor)
            self.listaDer.insert(END, valor)
            self.listaDer.itemconfig(END, background="pale green")
            self.eliminarElmListaIzq(k)

    def mandarNegativo(self):
        for k in self.seleccionIzq:
            valor = str(self.listaIzq.get(k,k)[0])
            #print("Negativo: "+valor)
            self.listaDer.insert(END,valor)
            self.listaDer.itemconfig(END,background="coral1")
            self.eliminarElmListaIzq(k)

    def hello(self):
        print("Hello!!")

    def ejemplosTextos(self):
        for k in range(100):
            self.listaIzq.insert(END,str(k))

    def importarArchivo(self):
        nombreArchivo = askopenfile()
        for line in nombreArchivo.readlines():
            #print(line)
            if (line!=""):
                self.listaIzq.insert(END,line)

    def guardarArchivo(self):
        self.archivoSalida = asksaveasfile(mode='w',defaultextension='.xml')
        if self.archivoSalida is None:
            return


if __name__ == "__main__":
    print("Hello World")
    interf = Interfaz()
