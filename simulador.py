from tkinter import Tk, Label, Button, PhotoImage, ttk
from tkinter import *
import tkinter as TK

def Calcular(listaDesplegable,listaDesplegable1,listaDesplegable2,listaDesplegable3,nuevaVentana):

    Label(nuevaVentana, text='///////////////////////////////////////////////////////////////////////////////////////////').place(x=100,y=80)

    if listaDesplegable.get() == 'Negro':
        valor = 0
    elif listaDesplegable.get() == 'Marrón':
        valor = 10
    elif listaDesplegable.get() == 'Rojo':
        valor = 20
    elif listaDesplegable.get() == 'Naranja':
        valor = 30
    elif listaDesplegable.get() == 'Amarillo':
        valor = 40
    elif listaDesplegable.get() == 'Verde':
        valor = 50
    elif listaDesplegable.get() == 'Azul':
        valor = 60
    elif listaDesplegable.get() == 'Violeta':
        valor = 70
    elif listaDesplegable.get() == 'Gris':
        valor = 80
    elif listaDesplegable.get() == 'Blanco':
        valor = 90
    
    if listaDesplegable1.get() == 'Negro':
        valor = valor + 0
    elif listaDesplegable1.get() == 'Marrón':
        valor = valor + 1
    elif listaDesplegable1.get() == 'Rojo':
        valor = valor + 2
    elif listaDesplegable1.get() == 'Naranja':
        valor = valor + 3
    elif listaDesplegable1.get() == 'Amarillo':
        valor = valor + 4
    elif listaDesplegable1.get() == 'Verde':
        valor = valor + 5
    elif listaDesplegable1.get() == 'Azul':
        valor = valor + 6
    elif listaDesplegable1.get() == 'Violeta':
        valor = valor + 7
    elif listaDesplegable1.get() == 'Gris':
        valor = valor + 8
    elif listaDesplegable1.get() == 'Blanco':
        valor = valor + 9

    if listaDesplegable2.get() == 'Negro':
        valor = valor * 1
    elif listaDesplegable2.get() == 'Marrón':
        valor = valor * 10
    elif listaDesplegable2.get() == 'Rojo':
        valor = valor * 100
    elif listaDesplegable2.get() == 'Naranja':
        valor = valor * 1000
    elif listaDesplegable2.get() == 'Amarillo':
        valor = valor * 10000
    elif listaDesplegable2.get() == 'Verde':
        valor = valor * 100000
    elif listaDesplegable2.get() == 'Azul':
        valor = valor * 1000000
    elif listaDesplegable2.get() == 'Violeta':
        valor = valor * 10000000
    elif listaDesplegable2.get() == 'Gris':
        valor = valor * 100000000
    elif listaDesplegable2.get() == 'Blanco':
        valor = valor * 1000000000
    elif listaDesplegable2.get() == 'Oro':
        valor = valor * 0.1
    elif listaDesplegable2.get() == 'Plata':
        valor = valor * 0.01

    if listaDesplegable3.get() == 'Marrón':
        tole = '± 1 % [Ω]'
    elif listaDesplegable3.get() == 'Rojo':
        tole = '± 2 % [Ω]'
    elif listaDesplegable3.get() == 'Verde':
        tole = '± 0.5 % [Ω]'
    elif listaDesplegable3.get() == 'Azul':
        tole = '± 0.25 % [Ω]'
    elif listaDesplegable3.get() == 'Violeta':
        tole = '± 0.1 % [Ω]'
    elif listaDesplegable3.get() == 'Gris':
        tole = '± 0.05 % [Ω]'
    elif listaDesplegable3.get() == 'Oro':
        tole = '± 5 % [Ω]'
    elif listaDesplegable3.get() == 'Plata':
        tole = '± 10 % [Ω]'

    print(valor)
    print(tole)
    Label(nuevaVentana, text='El valor de la resistencia es: ').place(x=100,y=80)
    Label(nuevaVentana, text=valor).place(x=290,y=80)
    Label(nuevaVentana, text=tole).place(x=400,y=80)

def calculoColorResistencia4Colores():
    print('Boton')

    nuevaVentana = TK.Toplevel(ventana)
    nuevaVentana.geometry('860x480')
    nuevaVentana.title('Calculo de los colores de la resistencia')

    #texto
    lbl = Label(nuevaVentana, text='Primer color')
    lbl.place(x=20,y=20)
    lbl1 = Label(nuevaVentana, text='Segundo color')
    lbl1.place(x=200,y=20)
    lbl2= Label(nuevaVentana, text='Tercer color')
    lbl2.place(x=400,y=20)
    lbl3 = Label(nuevaVentana, text='Cuarto color')
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
    opciones = ('Negro','Marrón','Rojo','Naranja','Amarillo','Verde','Azul','Violeta','Gris','Blanco')
    opciones1 = ('Negro','Marrón','Rojo','Naranja','Amarillo','Verde','Azul','Violeta','Gris','Blanco')
    opcionesMult = ('Negro','Marrón','Rojo','Naranja','Amarillo','Verde','Azul','Violeta','Gris','Blanco','Oro','Plata')
    opcionesTole = ('Marrón','Rojo','Verde','Azul','Violeta','Gris','Oro','Plata')

    listaDesplegable['values'] = opciones
    listaDesplegable1['values'] = opciones1
    listaDesplegable2['values'] = opcionesMult
    listaDesplegable3['values'] = opcionesTole

    Button(nuevaVentana,text='Aceptar',command=lambda: Calcular(listaDesplegable,listaDesplegable1,listaDesplegable2,listaDesplegable3,nuevaVentana)).place(x=20,y=80)


def calculoColorResistencia5Colores():
    print('Boton 5 resitencia')

def calculoColorResistencia6Colores():
    print('Boton 6 resitencia')

def CalculoRSerieParalelo():
    print('Boton 1')
    nuevaVentana = TK.Toplevel(ventana)
    nuevaVentana.geometry('640x480')
    nuevaVentana.title('Calculo de resistencia en serie/paralelo')

def ResistividadMaterial():
    print('Boton 2')
    nuevaVentana = TK.Toplevel(ventana)
    nuevaVentana.geometry('640x480')
    nuevaVentana.title('Calculo de la resistividad de un material')

def CapacitorSerieParalelo():
    print('Boton 3')
    nuevaVentana = TK.Toplevel(ventana)
    nuevaVentana.geometry('640x480')
    nuevaVentana.title('Calculo de capacitor en serie/paralelo')


def Opcion1():
    nuevaVentana = TK.Toplevel(ventana)
    nuevaVentana.geometry('300x200')
    nuevaVentana.title('Seleccione una opción')

    Button(nuevaVentana, text='Cuatro colores', command=calculoColorResistencia4Colores).pack(pady=15)
    Button(nuevaVentana, text='Cinco colores', command=calculoColorResistencia5Colores).pack(pady=15)
    Button(nuevaVentana, text='Seis colores', command=calculoColorResistencia6Colores).pack(pady=15)


# Inicio del programa -> creacion de la ventana
ventana = Tk()
ventana.geometry('640x480')
ventana.title('Simulador Circuito')

lbl = Label(ventana, text='Menu')
lbl.pack()

#creacion de los botones
btn = Button(ventana, text='Calculo de los colores de la resistencia', command=Opcion1)
btn.pack(pady=20)
btn1 = Button(ventana, text='Calculo de resistencia en serio/paralelo',command=CalculoRSerieParalelo)
btn1.pack(pady=20)
btn2= Button(ventana, text='Calculo de la resistividad de un material', command= ResistividadMaterial)
btn2.pack(pady=20)
btn3 = Button(ventana, text= 'Calculo de capacitor serie/paralelo', command=CapacitorSerieParalelo)
btn3.pack(pady=20)

#importa el logo del dep. de fisica
img = PhotoImage(file='dfuls-logo.png')
lbl_img = Label(ventana, image = img)
lbl_img.pack()

ventana.mainloop()
