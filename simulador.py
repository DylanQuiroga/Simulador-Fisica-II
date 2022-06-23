from tkinter import Tk, Label, Button, PhotoImage, ttk
from tkinter import *
import tkinter as TK

def Calcular4resistencia(listaDesplegable,listaDesplegable1,listaDesplegable2,listaDesplegable3,nuevaVentana):

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
        tole = '± 1 % '
    elif listaDesplegable3.get() == 'Rojo':
        tole = '± 2 % '
    elif listaDesplegable3.get() == 'Verde':
        tole = '± 0.5 % '
    elif listaDesplegable3.get() == 'Azul':
        tole = '± 0.25 % '
    elif listaDesplegable3.get() == 'Violeta':
        tole = '± 0.1 % '
    elif listaDesplegable3.get() == 'Gris':
        tole = '± 0.05 % '
    elif listaDesplegable3.get() == 'Oro':
        tole = '± 5 % '
    elif listaDesplegable3.get() == 'Plata':
        tole = '± 10 % '

    print(valor)
    print(tole)
    Label(nuevaVentana, text='El valor de la resistencia es: ').place(x=100,y=80)
    Label(nuevaVentana, text=valor).place(x=290,y=80)
    Label(nuevaVentana, text='[Ω]').place(x=380,y=80)
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
    opcionesMult = ('Negro','Marrón','Rojo','Naranja','Amarillo','Verde','Azul','Violeta','Gris','Blanco','Oro','Plata')
    opcionesTole = ('Marrón','Rojo','Verde','Azul','Violeta','Gris','Oro','Plata')

    listaDesplegable['values'] = opciones
    listaDesplegable1['values'] = opciones
    listaDesplegable2['values'] = opcionesMult
    listaDesplegable3['values'] = opcionesTole

    Button(nuevaVentana,text='Aceptar',command=lambda: Calcular4resistencia(listaDesplegable,listaDesplegable1,listaDesplegable2,listaDesplegable3,nuevaVentana)).place(x=20,y=80)


def Calcular5resistencia(listaDesplegable,listaDesplegable1,listaDesplegable2,listaDesplegable3,listaDesplegable4,nuevaVentana):

    Label(nuevaVentana, text='///////////////////////////////////////////////////////////////////////////////////////////').place(x=100,y=80)

    if listaDesplegable.get() == 'Negro':
        valor = 0
    elif listaDesplegable.get() == 'Marrón':
        valor = 100
    elif listaDesplegable.get() == 'Rojo':
        valor = 200
    elif listaDesplegable.get() == 'Naranja':
        valor = 300
    elif listaDesplegable.get() == 'Amarillo':
        valor = 400
    elif listaDesplegable.get() == 'Verde':
        valor = 500
    elif listaDesplegable.get() == 'Azul':
        valor = 600
    elif listaDesplegable.get() == 'Violeta':
        valor = 700
    elif listaDesplegable.get() == 'Gris':
        valor = 800
    elif listaDesplegable.get() == 'Blanco':
        valor = 900
    
    if listaDesplegable1.get() == 'Negro':
        valor = valor + 0
    elif listaDesplegable1.get() == 'Marrón':
        valor = valor + 10
    elif listaDesplegable1.get() == 'Rojo':
        valor = valor + 20
    elif listaDesplegable1.get() == 'Naranja':
        valor = valor + 30
    elif listaDesplegable1.get() == 'Amarillo':
        valor = valor + 40
    elif listaDesplegable1.get() == 'Verde':
        valor = valor + 50
    elif listaDesplegable1.get() == 'Azul':
        valor = valor + 60
    elif listaDesplegable1.get() == 'Violeta':
        valor = valor + 70
    elif listaDesplegable1.get() == 'Gris':
        valor = valor + 80
    elif listaDesplegable1.get() == 'Blanco':
        valor = valor + 90

    if listaDesplegable2.get() == 'Negro':
        valor = valor + 0
    elif listaDesplegable2.get() == 'Marrón':
        valor = valor + 1
    elif listaDesplegable2.get() == 'Rojo':
        valor = valor + 2
    elif listaDesplegable2.get() == 'Naranja':
        valor = valor + 3
    elif listaDesplegable2.get() == 'Amarillo':
        valor = valor + 4
    elif listaDesplegable2.get() == 'Verde':
        valor = valor + 5
    elif listaDesplegable2.get() == 'Azul':
        valor = valor + 6
    elif listaDesplegable2.get() == 'Violeta':
        valor = valor + 7
    elif listaDesplegable2.get() == 'Gris':
        valor = valor + 8
    elif listaDesplegable2.get() == 'Blanco':
        valor = valor + 9

    if listaDesplegable3.get() == 'Negro':
        valor = valor * 1
    elif listaDesplegable3.get() == 'Marrón':
        valor = valor * 10
    elif listaDesplegable3.get() == 'Rojo':
        valor = valor * 100
    elif listaDesplegable3.get() == 'Naranja':
        valor = valor * 1000
    elif listaDesplegable3.get() == 'Amarillo':
        valor = valor * 10000
    elif listaDesplegable3.get() == 'Verde':
        valor = valor * 100000
    elif listaDesplegable3.get() == 'Azul':
        valor = valor * 1000000
    elif listaDesplegable3.get() == 'Violeta':
        valor = valor * 10000000
    elif listaDesplegable3.get() == 'Gris':
        valor = valor * 100000000
    elif listaDesplegable3.get() == 'Blanco':
        valor = valor * 1000000000
    elif listaDesplegable3.get() == 'Oro':
        valor = valor * 0.1
    elif listaDesplegable3.get() == 'Plata':
        valor = valor * 0.01

    if listaDesplegable4.get() == 'Marrón':
        tole = '± 1 % '
    elif listaDesplegable4.get() == 'Rojo':
        tole = '± 2 % '
    elif listaDesplegable4.get() == 'Verde':
        tole = '± 0.5 % '
    elif listaDesplegable4.get() == 'Azul':
        tole = '± 0.25 % '
    elif listaDesplegable4.get() == 'Violeta':
        tole = '± 0.1 % '
    elif listaDesplegable4.get() == 'Gris':
        tole = '± 0.05 % '
    elif listaDesplegable4.get() == 'Oro':
        tole = '± 5 % '
    elif listaDesplegable4.get() == 'Plata':
        tole = '± 10 % '

    print(valor)
    print(tole)
    Label(nuevaVentana, text='El valor de la resistencia es: ').place(x=100,y=80)
    Label(nuevaVentana, text=valor).place(x=290,y=80)
    Label(nuevaVentana, text='[Ω]').place(x=380,y=80)
    Label(nuevaVentana, text=tole).place(x=400,y=80)

def calculoColorResistencia5Colores():
    print('Boton 5 resitencia')
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
    lbl4 = Label(nuevaVentana,text = 'Quinto color')
    lbl4.place(x=20, y=50)

    #lista desplegable
    listaDesplegable = ttk.Combobox(nuevaVentana,width=10)
    listaDesplegable.place(x=100,y=20)

    listaDesplegable1 = ttk.Combobox(nuevaVentana,width=10)
    listaDesplegable1.place(x=300,y=20)

    listaDesplegable2 = ttk.Combobox(nuevaVentana,width=10)
    listaDesplegable2.place(x=500,y=20)

    listaDesplegable3 = ttk.Combobox(nuevaVentana, width=10)
    listaDesplegable3.place(x=700,y=20)

    listaDesplegable4 = ttk.Combobox(nuevaVentana,width = 10)
    listaDesplegable4.place(x = 100, y = 50)

    #opciones de los colores
    opciones = ('Negro','Marrón','Rojo','Naranja','Amarillo','Verde','Azul','Violeta','Gris','Blanco')
    opcionesMult = ('Negro','Marrón','Rojo','Naranja','Amarillo','Verde','Azul','Violeta','Gris','Blanco','Oro','Plata')
    opcionesTole = ('Marrón','Rojo','Verde','Azul','Violeta','Gris','Oro','Plata')

    listaDesplegable['values'] = opciones
    listaDesplegable1['values'] = opciones
    listaDesplegable2['values'] = opciones
    listaDesplegable3['values'] = opcionesMult
    listaDesplegable4['values'] = opcionesTole

    Button(nuevaVentana,text='Aceptar',command=lambda: Calcular5resistencia(listaDesplegable,listaDesplegable1,listaDesplegable2,listaDesplegable3,listaDesplegable4,nuevaVentana)).place(x=20,y=80)

def Calcular6resistencia(listaDesplegable,listaDesplegable1,listaDesplegable2,listaDesplegable3,listaDesplegable4,listaDesplegable5,nuevaVentana):

    Label(nuevaVentana, text='///////////////////////////////////////////////////////////////////////////////////////////').place(x=100,y=80)

    if listaDesplegable.get() == 'Negro':
        valor = 0
    elif listaDesplegable.get() == 'Marrón':
        valor = 100
    elif listaDesplegable.get() == 'Rojo':
        valor = 200
    elif listaDesplegable.get() == 'Naranja':
        valor = 300
    elif listaDesplegable.get() == 'Amarillo':
        valor = 400
    elif listaDesplegable.get() == 'Verde':
        valor = 500
    elif listaDesplegable.get() == 'Azul':
        valor = 600
    elif listaDesplegable.get() == 'Violeta':
        valor = 700
    elif listaDesplegable.get() == 'Gris':
        valor = 800
    elif listaDesplegable.get() == 'Blanco':
        valor = 900
    
    if listaDesplegable1.get() == 'Negro':
        valor = valor + 0
    elif listaDesplegable1.get() == 'Marrón':
        valor = valor + 10
    elif listaDesplegable1.get() == 'Rojo':
        valor = valor + 20
    elif listaDesplegable1.get() == 'Naranja':
        valor = valor + 30
    elif listaDesplegable1.get() == 'Amarillo':
        valor = valor + 40
    elif listaDesplegable1.get() == 'Verde':
        valor = valor + 50
    elif listaDesplegable1.get() == 'Azul':
        valor = valor + 60
    elif listaDesplegable1.get() == 'Violeta':
        valor = valor + 70
    elif listaDesplegable1.get() == 'Gris':
        valor = valor + 80
    elif listaDesplegable1.get() == 'Blanco':
        valor = valor + 90

    if listaDesplegable2.get() == 'Negro':
        valor = valor + 0
    elif listaDesplegable2.get() == 'Marrón':
        valor = valor + 1
    elif listaDesplegable2.get() == 'Rojo':
        valor = valor + 2
    elif listaDesplegable2.get() == 'Naranja':
        valor = valor + 3
    elif listaDesplegable2.get() == 'Amarillo':
        valor = valor + 4
    elif listaDesplegable2.get() == 'Verde':
        valor = valor + 5
    elif listaDesplegable2.get() == 'Azul':
        valor = valor + 6
    elif listaDesplegable2.get() == 'Violeta':
        valor = valor + 7
    elif listaDesplegable2.get() == 'Gris':
        valor = valor + 8
    elif listaDesplegable2.get() == 'Blanco':
        valor = valor + 9

    if listaDesplegable3.get() == 'Negro':
        valor = valor * 1
    elif listaDesplegable3.get() == 'Marrón':
        valor = valor * 10
    elif listaDesplegable3.get() == 'Rojo':
        valor = valor * 100
    elif listaDesplegable3.get() == 'Naranja':
        valor = valor * 1000
    elif listaDesplegable3.get() == 'Amarillo':
        valor = valor * 10000
    elif listaDesplegable3.get() == 'Verde':
        valor = valor * 100000
    elif listaDesplegable3.get() == 'Azul':
        valor = valor * 1000000
    elif listaDesplegable3.get() == 'Violeta':
        valor = valor * 10000000
    elif listaDesplegable3.get() == 'Gris':
        valor = valor * 100000000
    elif listaDesplegable3.get() == 'Blanco':
        valor = valor * 1000000000
    elif listaDesplegable3.get() == 'Oro':
        valor = valor * 0.1
    elif listaDesplegable3.get() == 'Plata':
        valor = valor * 0.01

    if listaDesplegable4.get() == 'Marrón':
        tole = '± 1 % '
    elif listaDesplegable4.get() == 'Rojo':
        tole = '± 2 % '
    elif listaDesplegable4.get() == 'Verde':
        tole = '± 0.5 % '
    elif listaDesplegable4.get() == 'Azul':
        tole = '± 0.25 % '
    elif listaDesplegable4.get() == 'Violeta':
        tole = '± 0.1 % '
    elif listaDesplegable4.get() == 'Gris':
        tole = '± 0.05 % '
    elif listaDesplegable4.get() == 'Oro':
        tole = '± 5 % '
    elif listaDesplegable4.get() == 'Plata':
        tole = '± 10 % '

    if listaDesplegable5.get() == 'Marrón':
        ppm = '100 ppm'
    elif listaDesplegable5.get() == 'Rojo':
        ppm = '50 ppm'
    elif listaDesplegable5.get() == 'Naranja':
        ppm = '15 ppm'
    elif listaDesplegable5.get() == 'Amarillo':
        ppm = '25 ppm'
    elif listaDesplegable5.get() == 'Azul':
        ppm = '10 ppm'
    elif listaDesplegable5.get() == 'Violeta':
        ppm = '5 ppm'

    print(valor)
    print(tole)
    print(ppm)
    Label(nuevaVentana, text= 'El valor de la resistencia es: ').place(x=100,y=80)
    Label(nuevaVentana, text= valor).place(x=290,y=80)
    Label(nuevaVentana, text= '[Ω]').place(x=380,y=80)
    Label(nuevaVentana, text= tole).place(x=400,y=80)
    Label(nuevaVentana, text= ppm).place(x=450,y=80)

def calculoColorResistencia6Colores():
    print('Boton 6 resitencia')
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
    lbl4 = Label(nuevaVentana,text = 'Quinto color')
    lbl4.place(x=20, y=50)
    lbl5 = Label(nuevaVentana, text= 'Sexto color')
    lbl5.place(x=200, y=50)

    #lista desplegable
    listaDesplegable = ttk.Combobox(nuevaVentana,width=10)
    listaDesplegable.place(x=100,y=20)

    listaDesplegable1 = ttk.Combobox(nuevaVentana,width=10)
    listaDesplegable1.place(x=300,y=20)

    listaDesplegable2 = ttk.Combobox(nuevaVentana,width=10)
    listaDesplegable2.place(x=500,y=20)

    listaDesplegable3 = ttk.Combobox(nuevaVentana, width=10)
    listaDesplegable3.place(x=700,y=20)

    listaDesplegable4 = ttk.Combobox(nuevaVentana,width = 10)
    listaDesplegable4.place(x = 100, y = 50)

    listaDesplegable5 = ttk.Combobox(nuevaVentana, width= 10)
    listaDesplegable5.place(x=300,y=50)

    #opciones de los colores
    opciones = ('Negro','Marrón','Rojo','Naranja','Amarillo','Verde','Azul','Violeta','Gris','Blanco')
    opcionesMult = ('Negro','Marrón','Rojo','Naranja','Amarillo','Verde','Azul','Violeta','Gris','Blanco','Oro','Plata')
    opcionesTole = ('Marrón','Rojo','Verde','Azul','Violeta','Gris','Oro','Plata')
    opcionesPPM = ('Marrón','Rojo','Naranja','Amarillo','Azul','Violeta')

    listaDesplegable['values'] = opciones
    listaDesplegable1['values'] = opciones
    listaDesplegable2['values'] = opciones
    listaDesplegable3['values'] = opcionesMult
    listaDesplegable4['values'] = opcionesTole
    listaDesplegable5['values'] = opcionesPPM

    Button(nuevaVentana,text='Aceptar',command=lambda: Calcular6resistencia(listaDesplegable,listaDesplegable1,listaDesplegable2,listaDesplegable3,listaDesplegable4,listaDesplegable5,nuevaVentana)).place(x=20,y=80)


def CalculoRSerie():
    print('Boton 1')
    nuevaVentana = TK.Toplevel(ventana)
    nuevaVentana.geometry('640x480')
    nuevaVentana.title('Calculo de resistencia en serie/paralelo')

    Label(nuevaVentana, text = "Resistencia 1").place(x=20,y=20)
    Resistencia1 = ttk.Entry(nuevaVentana)
    Resistencia1.place(x=100,y=20)
    Label(nuevaVentana, text= "Resistencia 2").place(x=320,y=20)
    Resistencia2 = ttk.Entry(nuevaVentana)
    Resistencia2.place(x=400,y=20)

def CalculoRParalelo():
    print("Boton 1.5")

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

def Opcion2():
    nuevaVentana = TK.Toplevel(ventana)
    nuevaVentana.geometry('300x200')
    nuevaVentana.title('Seleccione una opción')

    Button(nuevaVentana, text='Resistencia en serie', command=CalculoRSerie).pack(pady=15)
    Button(nuevaVentana, text='Resistencia en paralelo', command=CalculoRParalelo).pack(pady=15)

# Inicio del programa -> creacion de la ventana
ventana = Tk()
ventana.geometry('640x480')
ventana.title('Simulador Circuito')

lbl = Label(ventana, text='Menu')
lbl.pack()

#creacion de los botones
btn = Button(ventana, text='Calculo de los colores de la resistencia', command=Opcion1)
btn.pack(pady=20)
btn1 = Button(ventana, text='Calculo de resistencia en serio/paralelo',command=Opcion2)
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
