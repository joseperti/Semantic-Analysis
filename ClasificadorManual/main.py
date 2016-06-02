from tkinter import *
import codecs

root = Tk()

positivos = []
negativos = []
textoActual = ""

def key(event):
    print("pressed", repr(event.char))
    if (event.char == '4'):
        positivo()
    elif (event.char == '6'):
        negativo()
    elif (event.char == '9'):
        cambiarTexto()
    elif (event.char == '0'):
        guardarPositivos()
        guardarNegativos()

def guardarPositivos():
    ruta = "positivos.txt"
    archivoPositivos = codecs.open(ruta,"w","utf8")
    archivoPositivos.write(repr(positivos))
    archivoPositivos.close()
    print("Guardados los positivos")


def guardarNegativos():
    ruta = "negativos.txt"
    archivoNegativos = codecs.open(ruta,"w","utf8")
    archivoNegativos.write(repr(negativos))
    archivoNegativos.close()
    print("Guardados los negativos")

def positivo():
    print("Es positivo: "+textoActual)
    positivos.append([textoActual,'positive'])
    cambiarTexto()

def negativo():
    print("Es negativo: " + textoActual)
    negativos.append([textoActual, 'negative'])
    cambiarTexto()

def cambiarTexto():
    global textoActual
    try:
        nuevoTexto = iterador.__next__()
        label1.config(text=str(nuevoTexto).encode("utf-8"))
        textoActual = str(nuevoTexto)
    except StopIteration:
        label1.config(text="No quedan documentos")


def callback(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)

def guardar():
    guardarNegativos()
    guardarPositivos()

archivo = codecs.open("documentos.txt","r","utf8")
iterador = iter(archivo.readlines())
frame = Frame(root, width=100, height=100)
Button(master=root,text="4-Positive",command=positivo).grid(row=0,column=1)
Button(master=root,text="0-Guardar",command=guardar).grid(row=0,column=2)
Button(master=root,text="6-Negative",command=negativo).grid(row=0,column=3)
Button(master=root,text="9-Nada",command=cambiarTexto).grid(row=0,column=4)
label1 = Label(master = root,text="Nada")
label1.grid(row=1,column=0,columnspan=5)
root.bind("<Key>", key)
root.bind("<Button-1>", callback)
cambiarTexto()
root.mainloop()