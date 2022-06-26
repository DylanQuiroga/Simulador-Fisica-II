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

def CalcularRSerie(Resistencia1,Resistencia2,Resistencia3,Resistencia4,Resistencia5,Resistencia6,Resistencia7,Resistencia8,Resistencia9,Resistencia10, nuevaVentana):
    Label(nuevaVentana, text='///////////////////////////////////////////////////////////////////////////////////////////').place(x=80,y=180)
    Resultado = int(Resistencia1.get())+int(Resistencia2.get())+int(Resistencia3.get())+int(Resistencia4.get())+int(Resistencia5.get())+int(Resistencia6.get())+int(Resistencia7.get())+int(Resistencia8.get())+int(Resistencia9.get())+int(Resistencia10.get())
    print(Resultado)
    Label(nuevaVentana,text="El valor de la resistencia es").place(x=100,y=180)
    Label(nuevaVentana,text=Resultado).place(x=300,y=180)
    Label(nuevaVentana,text="[Ω]").place(x=400,y=180)

def CalculoRSerie():
    print('Boton 1')
    
    nuevaVentana = TK.Toplevel(ventana)
    nuevaVentana.geometry('640x480')
    nuevaVentana.title('Calculo de resistencia en serie/paralelo')

    R1 = TK.IntVar()
    R2 = TK.IntVar()
    R3 = TK.IntVar()
    R4 = TK.IntVar()
    R5 = TK.IntVar()
    R6 = TK.IntVar()
    R7 = TK.IntVar()
    R8 = TK.IntVar()
    R9 = TK.IntVar()
    R10 = TK.IntVar()

    Label(nuevaVentana, text = "Resistencia 1").place(x=20,y=20)
    TK.Entry(nuevaVentana, textvariable=R1).place(x=100,y=20)
    Label(nuevaVentana, text= "Resistencia 2").place(x=320,y=20)
    TK.Entry(nuevaVentana, textvariable=R2).place(x=400,y=20)
    Label(nuevaVentana, text= "Resistencia 3").place(x=20, y=50)
    TK.Entry(nuevaVentana, textvariable=R3).place(x=100,y=50)
    Label(nuevaVentana, text="Resistencia 4").place(x=320,y=50)
    TK.Entry(nuevaVentana, textvariable=R4).place(x=400,y=50)
    Label(nuevaVentana, text="Resistencia 5").place(x=20,y=80)
    TK.Entry(nuevaVentana, textvariable=R5).place(x=100,y=80)
    Label(nuevaVentana, text="Resistencia 6").place(x=320,y=80)
    TK.Entry(nuevaVentana, textvariable=R6).place(x=400,y=80)
    Label(nuevaVentana, text="Resistencia 7").place(x=20,y=110)
    TK.Entry(nuevaVentana, textvariable=R7).place(x=100,y=110)
    Label(nuevaVentana, text="Resistencia 8").place(x=320,y=110)
    TK.Entry(nuevaVentana, textvariable=R8).place(x=400,y=110)
    Label(nuevaVentana, text="Resistencia 9").place(x=20,y=140)
    TK.Entry(nuevaVentana, textvariable=R9).place(x=100,y=140)
    Label(nuevaVentana, text="Resistencia 10").place(x=320,y=140)
    TK.Entry(nuevaVentana, textvariable=R10).place(x=400,y=140)

    Button(nuevaVentana, text="Calcular", command=lambda:CalcularRSerie(R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,nuevaVentana)).place(x=20,y=180)

def CalcularRParalelo(Resistencia1,Resistencia2,Resistencia3,Resistencia4,Resistencia5,Resistencia6,Resistencia7,Resistencia8,Resistencia9,Resistencia10, nuevaVentana):

    if int(Resistencia1.get()) == 0:
        res1 = 0
    else:
        res1 = 1/int(Resistencia1.get())

    if int(Resistencia2.get()) == 0:
        res2 = 0
    else:
        res2 = 1/int(Resistencia2.get())

    if int(Resistencia3.get()) == 0:
        res3 = 0
    else:
        res3 = 1/int(Resistencia3.get())

    if int(Resistencia4.get()) == 0:
        res4 = 0
    else:
        res4 = 1/int(Resistencia4.get())

    if int(Resistencia5.get()) == 0:
        res5 = 0
    else:
        res5 = 1/int(Resistencia5.get())

    if int(Resistencia6.get()) == 0:
        res6 = 0
    else:
        res6 = 1/int(Resistencia6.get())

    if int(Resistencia7.get()) == 0:
        res7 = 0
    else:
        res7 = 1/int(Resistencia7.get())

    if int(Resistencia8.get()) == 0:
        res8 = 0
    else:
        res8 = 1/int(Resistencia8.get())

    if int(Resistencia9.get()) == 0:
        res9 = 0
    else:
        res9 = 1/int(Resistencia9.get())

    if int(Resistencia10.get()) == 0:
        res10 = 0
    else:
        res10 = 1/int(Resistencia10.get())

    Label(nuevaVentana, text='///////////////////////////////////////////////////////////////////////////////////////////').place(x=80,y=180)
    Resultado = 1/(res1+res2+res3+res4+res5+res6+res7+res8+res9+res10)
    print(Resultado)
    Label(nuevaVentana,text="El valor de la resistencia es").place(x=100,y=180)
    Label(nuevaVentana,text=Resultado).place(x=300,y=180)
    Label(nuevaVentana,text="[Ω]").place(x=400,y=180)

def CalculoRParalelo():
    print("Boton 1.5")
    nuevaVentana = TK.Toplevel(ventana)
    nuevaVentana.geometry('640x480')
    nuevaVentana.title('Calculo de resistencia en serie/paralelo')

    R1 = TK.IntVar()
    R2 = TK.IntVar()
    R3 = TK.IntVar()
    R4 = TK.IntVar()
    R5 = TK.IntVar()
    R6 = TK.IntVar()
    R7 = TK.IntVar()
    R8 = TK.IntVar()
    R9 = TK.IntVar()
    R10 = TK.IntVar()

    Label(nuevaVentana, text = "Resistencia 1").place(x=20,y=20)
    TK.Entry(nuevaVentana, textvariable=R1).place(x=100,y=20)
    Label(nuevaVentana, text= "Resistencia 2").place(x=320,y=20)
    TK.Entry(nuevaVentana, textvariable=R2).place(x=400,y=20)
    Label(nuevaVentana, text= "Resistencia 3").place(x=20, y=50)
    TK.Entry(nuevaVentana, textvariable=R3).place(x=100,y=50)
    Label(nuevaVentana, text="Resistencia 4").place(x=320,y=50)
    TK.Entry(nuevaVentana, textvariable=R4).place(x=400,y=50)
    Label(nuevaVentana, text="Resistencia 5").place(x=20,y=80)
    TK.Entry(nuevaVentana, textvariable=R5).place(x=100,y=80)
    Label(nuevaVentana, text="Resistencia 6").place(x=320,y=80)
    TK.Entry(nuevaVentana, textvariable=R6).place(x=400,y=80)
    Label(nuevaVentana, text="Resistencia 7").place(x=20,y=110)
    TK.Entry(nuevaVentana, textvariable=R7).place(x=100,y=110)
    Label(nuevaVentana, text="Resistencia 8").place(x=320,y=110)
    TK.Entry(nuevaVentana, textvariable=R8).place(x=400,y=110)
    Label(nuevaVentana, text="Resistencia 9").place(x=20,y=140)
    TK.Entry(nuevaVentana, textvariable=R9).place(x=100,y=140)
    Label(nuevaVentana, text="Resistencia 10").place(x=320,y=140)
    TK.Entry(nuevaVentana, textvariable=R10).place(x=400,y=140)

    Button(nuevaVentana, text="Calcular", command=lambda:CalcularRParalelo(R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,nuevaVentana)).place(x=20,y=180)

def CalcularCapacidadSerie(Capacidad1,Capacidad2, Capacidad3, Capacidad4, Capacidad5, Capacidad6, Capacidad7, Capacidad8, Capacidad9, Capacidad10, nuevaVentana):
    
    if int(Capacidad1.get()) == 0:
        Cap1 = 0
    else:
        Cap1 = 1/int(Capacidad1.get())

    if int(Capacidad2.get()) == 0:
        Cap2 = 0
    else:
        Cap2 = 1/int(Capacidad2.get())

    if int(Capacidad3.get()) == 0:
        Cap3 = 0
    else:
        Cap3 = 1/int(Capacidad3.get())

    if int(Capacidad4.get()) == 0:
        Cap4 = 0
    else:
        Cap4 = 1/int(Capacidad4.get())

    if int(Capacidad5.get()) == 0:
        Cap5 = 0
    else:
        Cap5 = 1/int(Capacidad5.get())

    if int(Capacidad6.get()) == 0:
        Cap6 = 0
    else:
        Cap6 = 1/int(Capacidad6.get())

    if int(Capacidad7.get()) == 0:
        Cap7 = 0
    else:
        Cap7 = 1/int(Capacidad7.get())

    if int(Capacidad8.get()) == 0:
        Cap8 = 0
    else:
        Cap8 = 1/int(Capacidad8.get())

    if int(Capacidad9.get()) == 0:
        Cap9 = 0
    else:
        Cap9 = 1/int(Capacidad9.get())

    if int(Capacidad10.get()) == 0:
        Cap10 = 0
    else:
        Cap10 = 1/int(Capacidad10.get())

    Label(nuevaVentana, text='///////////////////////////////////////////////////////////////////////////////////////////').place(x=80,y=180)
    Resultado = 1/(Cap1+Cap2+Cap3+Cap4+Cap5+Cap6+Cap7+Cap8+Cap9+Cap10)
    print(Resultado)
    Label(nuevaVentana,text="La capacidad equivalente es").place(x=100,y=180)
    Label(nuevaVentana,text=Resultado).place(x=300,y=180)
    Label(nuevaVentana,text="[μF]").place(x=400,y=180)

def CalculoCapacidadSerie():
    
    print("Boton 1.5")
    nuevaVentana = TK.Toplevel(ventana)
    nuevaVentana.geometry('640x480')
    nuevaVentana.title('Calculo de capacidad equivalente condensadores en serie')

    C1 = TK.IntVar()
    C2 = TK.IntVar()
    C3 = TK.IntVar()
    C4 = TK.IntVar()
    C5 = TK.IntVar()
    C6 = TK.IntVar()
    C7 = TK.IntVar()
    C8 = TK.IntVar()
    C9 = TK.IntVar()
    C10 = TK.IntVar()

    Label(nuevaVentana, text = "Capacidad 1").place(x=20,y=20)
    TK.Entry(nuevaVentana, textvariable=C1).place(x=100,y=20)
    Label(nuevaVentana, text= "Capacidad 2").place(x=320,y=20)
    TK.Entry(nuevaVentana, textvariable=C2).place(x=400,y=20)
    Label(nuevaVentana, text= "Capacidad 3").place(x=20, y=50)
    TK.Entry(nuevaVentana, textvariable=C3).place(x=100,y=50)
    Label(nuevaVentana, text="Capacidad 4").place(x=320,y=50)
    TK.Entry(nuevaVentana, textvariable=C4).place(x=400,y=50)
    Label(nuevaVentana, text="Capacidad 5").place(x=20,y=80)
    TK.Entry(nuevaVentana, textvariable=C5).place(x=100,y=80)
    Label(nuevaVentana, text="Capacidad 6").place(x=320,y=80)
    TK.Entry(nuevaVentana, textvariable=C6).place(x=400,y=80)
    Label(nuevaVentana, text="Capacidad 7").place(x=20,y=110)
    TK.Entry(nuevaVentana, textvariable=C7).place(x=100,y=110)
    Label(nuevaVentana, text="Capacidad 8").place(x=320,y=110)
    TK.Entry(nuevaVentana, textvariable=C8).place(x=400,y=110)
    Label(nuevaVentana, text="Capacidad 9").place(x=20,y=140)
    TK.Entry(nuevaVentana, textvariable=C9).place(x=100,y=140)
    Label(nuevaVentana, text="Capacidad 10").place(x=320,y=140)
    TK.Entry(nuevaVentana, textvariable=C10).place(x=400,y=140)

    Button(nuevaVentana, text="Calcular", command=lambda:CalcularCapacidadSerie(C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,nuevaVentana)).place(x=20,y=180)
    

def CalcularCapacidadParalelo(Capacidad1,Capacidad2, Capacidad3, Capacidad4, Capacidad5, Capacidad6, Capacidad7, Capacidad8, Capacidad9, Capacidad10, nuevaVentana):
    Label(nuevaVentana, text='///////////////////////////////////////////////////////////////////////////////////////////').place(x=80,y=180)
    Resultado = int(Capacidad1.get())+int(Capacidad2.get())+int(Capacidad3.get())+int(Capacidad4.get())+int(Capacidad5.get())+int(Capacidad6.get())+int(Capacidad7.get())+int(Capacidad8.get())+int(Capacidad9.get())+int(Capacidad10.get())
    print(Resultado)
    Label(nuevaVentana,text="El capacidad equivalente es").place(x=100,y=180)
    Label(nuevaVentana,text=Resultado).place(x=300,y=180)
    Label(nuevaVentana,text="[μF]").place(x=400,y=180)

def CalculoCapacidadParalelo():
    print("Boton 1")
    nuevaVentana = TK.Toplevel(ventana)
    nuevaVentana.geometry('640x480')
    nuevaVentana.title('Calculo de capacidad equivalente condensadores en paralelo')

    C1 = TK.IntVar()
    C2 = TK.IntVar()
    C3 = TK.IntVar()
    C4 = TK.IntVar()
    C5 = TK.IntVar()
    C6 = TK.IntVar()
    C7 = TK.IntVar()
    C8 = TK.IntVar()
    C9 = TK.IntVar()
    C10 = TK.IntVar()

    Label(nuevaVentana, text = "Capacidad 1").place(x=20,y=20)
    TK.Entry(nuevaVentana, textvariable=C1).place(x=100,y=20)
    Label(nuevaVentana, text= "Capacidad 2").place(x=320,y=20)
    TK.Entry(nuevaVentana, textvariable=C2).place(x=400,y=20)
    Label(nuevaVentana, text= "Capacidad 3").place(x=20, y=50)
    TK.Entry(nuevaVentana, textvariable=C3).place(x=100,y=50)
    Label(nuevaVentana, text="Capacidad 4").place(x=320,y=50)
    TK.Entry(nuevaVentana, textvariable=C4).place(x=400,y=50)
    Label(nuevaVentana, text="Capacidad 5").place(x=20,y=80)
    TK.Entry(nuevaVentana, textvariable=C5).place(x=100,y=80)
    Label(nuevaVentana, text="Capacidad 6").place(x=320,y=80)
    TK.Entry(nuevaVentana, textvariable=C6).place(x=400,y=80)
    Label(nuevaVentana, text="Capacidad 7").place(x=20,y=110)
    TK.Entry(nuevaVentana, textvariable=C7).place(x=100,y=110)
    Label(nuevaVentana, text="Capacidad 8").place(x=320,y=110)
    TK.Entry(nuevaVentana, textvariable=C8).place(x=400,y=110)
    Label(nuevaVentana, text="Capacidad 9").place(x=20,y=140)
    TK.Entry(nuevaVentana, textvariable=C9).place(x=100,y=140)
    Label(nuevaVentana, text="Capacidad 10").place(x=320,y=140)
    TK.Entry(nuevaVentana, textvariable=C10).place(x=400,y=140)

    Button(nuevaVentana, text="Calcular", command=lambda:CalcularCapacidadParalelo(C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,nuevaVentana)).place(x=20,y=180)
       
def ResistividadMaterial():
    print('Boton 2')
    nuevaVentana = TK.Toplevel(ventana)
    nuevaVentana.geometry('640x480')
    nuevaVentana.title('Calculo de la resistividad de un material')

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

def Opcion4():
    nuevaVentana = TK.Toplevel(ventana)
    nuevaVentana.geometry('300x200')
    nuevaVentana.title('Seleccione una opción')

    Button(nuevaVentana, text='Condensadores en serie', command=CalculoCapacidadSerie).pack(pady=15)
    Button(nuevaVentana, text='Condensadores en paralelo', command=CalculoCapacidadParalelo).pack(pady=15)

# Inicio del programa -> creacion de la ventana
ventana = Tk()
ventana.geometry('640x480')
ventana.title('Simulador Circuito')

lbl = Label(ventana, text='Menu')
lbl.pack()

#creacion de los botones
btn = Button(ventana, text='Calculo de los colores de la resistencia', command=Opcion1)
btn.pack(pady=20)
btn1 = Button(ventana, text='Calculo de resistencia equivalente en serio/paralelo',command=Opcion2)
btn1.pack(pady=20)
btn2= Button(ventana, text='Calculo de la resistividad de un material', command= ResistividadMaterial)
btn2.pack(pady=20)
btn3 = Button(ventana, text= 'Calculo de capacidad equivalente condensador', command=Opcion4)
btn3.pack(pady=20)

#importa el logo del dep. de fisica
img = PhotoImage(file='dfuls-logo.png')
lbl_img = Label(ventana, image = img)
lbl_img.pack()

ventana.mainloop()
