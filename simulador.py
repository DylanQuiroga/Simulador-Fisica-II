from tkinter import Tk, Label, Button, PhotoImage

def calculoColorResistencia():
    print("Boton")

def CalculoRSerieParalelo():
    print("Boton 1")

def ResistividadMaterial():
    print("Boton 2")

def CapacitorSerieParalelo():
    print("Boton 3")

def menu():
    #creacion de la ventana
    ventana = Tk()
    ventana.geometry("640x480")
    ventana.title("Simulador Circuito")

    lbl = Label(ventana, text="Menu")
    lbl.pack()

    #creacion de los botones
    btn = Button(ventana, text="Calculo de los colores de la resistencia", command=calculoColorResistencia)
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

#inicio del programa
menu()