from tkinter import Tk, Label, Button, PhotoImage, ttk
from tkinter import *
import tkinter as TK

def calculoColorResistencia4Colores():
    print("Boton")
    nuevaVentana = TK.Toplevel(ventana)
    nuevaVentana.geometry("860x480")
    nuevaVentana.title("Calculo de los colores de la resistencia")

    #texto
    lbl = Label(nuevaVentana, text="Primer color")
    lbl.place(x=20,y=20)
    lbl1 = Label(nuevaVentana, text="Segundo color")
    lbl1.place(x=200,y=20)
    lbl2= Label(nuevaVentana, text="Tercer color")
    lbl2.place(x=400,y=20)
    lbl3 = Label(nuevaVentana, text="Cuarto color")
    lbl3.place(x=600,y=20)

    #lista desplegable
    listaDesplegable = ttk.Combobox(nuevaVentana,width=10)
    listaDesplegable.place(x=100,y=20)
    listaDesplegable1 = ttk.Combobox(nuevaVentana,width=10)
    listaDesplegable1.place(x=300,y=20)
    listaDesplegable2 = ttk.Combobox(nuevaVentana,width=10)
    listaDesplegable2.place(x=500,y=20)
    listaDesplegable3 = ttk.Combobox(nuevaVentana, width=10)
    listaDesplegable3.place(x=700,y=20)

    #opciones de los colores
    opciones = ["Negro","Marrón","Rojo","Naranja","Amarillo","Verde","Azul","Violeta","Gris","Blanco"]
    opcionesMult = ["Negro","Marrón","Rojo","Naranja","Amarillo","Verde","Azul","Violeta","Gris","Blanco","Oro","Plata"]
    opcionesTole = ["Marrón","Rojo","Verde","Azul","Violeta","Gris","Oro","Plata"]

    listaDesplegable['values'] = opciones
    listaDesplegable1['values'] = opciones
    listaDesplegable2['values'] = opcionesMult
    listaDesplegable3['values'] = opcionesTole

def calculoColorResistencia5Colores():
    print("Boton 5 resitencia")

def calculoColorResistencia6Colores():
    print("Boton 6 resitencia")

def CalculoRSerieParalelo():
    print("Boton 1")
    nuevaVentana = TK.Toplevel(ventana)
    nuevaVentana.geometry("640x480")
    nuevaVentana.title("Calculo de resistencia en serie/paralelo")

def ResistividadMaterial():
    print("Boton 2")
    nuevaVentana = TK.Toplevel(ventana)
    nuevaVentana.geometry("640x480")
    nuevaVentana.title("Calculo de la resistividad de un material")

def CapacitorSerieParalelo():
    print("Boton 3")
    nuevaVentana = TK.Toplevel(ventana)
    nuevaVentana.geometry("640x480")
    nuevaVentana.title("Calculo de capacitor en serie/paralelo")


def Opcion1():
    nuevaVentana = TK.Toplevel(ventana)
    nuevaVentana.geometry("300x200")
    nuevaVentana.title("Seleccione una opción")

    btn = Button(nuevaVentana, text="Cuatro colores", command=calculoColorResistencia4Colores).pack(pady=15)
    btn1 = Button(nuevaVentana, text="Cinco colores", command=calculoColorResistencia5Colores).pack(pady=15)
    btn2 = Button(nuevaVentana, text="Seis colores", command=calculoColorResistencia6Colores).pack(pady=15)


# Inicio del programa -> creacion de la ventana
ventana = Tk()
ventana.geometry("640x480")
ventana.title("Simulador Circuito")

lbl = Label(ventana, text="Menu")
lbl.pack()

#creacion de los botones
btn = Button(ventana, text="Calculo de los colores de la resistencia", command=Opcion1)
btn.pack(pady=20)
btn1 = Button(ventana, text="Calculo de resistencia en serio/paralelo",command=CalculoRSerieParalelo)
btn1.pack(pady=20)
btn2= Button(ventana, text="Calculo de la resistividad de un material", command= ResistividadMaterial)
btn2.pack(pady=20)
btn3 = Button(ventana, text= "Calculo de capacitor serie/paralelo", command=CapacitorSerieParalelo)
btn3.pack(pady=20)

#importa el logo del dep. de fisica
img = PhotoImage(file="dfuls-logo.png")
lbl_img = Label(ventana, image = img)
lbl_img.pack()

ventana.mainloop()
