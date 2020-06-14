import tkinter as tk
import RPi.GPIO as GPIO
from SimpleMFRC522 import *
import RPi.GPIO as GPIO


ventana = tk.Tk()
ventana.title("Menú desplegable")

image = tk.PhotoImage(file = "EAFIT.png")
image = image.subsample(4,4)
label = tk.Label(image = image)
label.pack(side = 'left')

ventana.geometry('680x500+600+100')
ventana.configure(background = 'midnight blue')

reader = SimpleMFRC522()

try:
        id, text = reader.read()
        print(id)
finally:
        GPIO.cleanup()
        
def confirmar_cant():
    cant = int (entrada.get())
    return cont.set(cant)

def confirmar_prestamo():
    elemen = var.get() 
    cantidad = cont.get()
    r = cantidad, elemen
    Final = str(id) + " "+ cantidad + " " + elemen+'\n'
    archivo = open("Data.txt", "a")
    archivo.write(Final)
    print(str(id) + " "+ cantidad + " " + elemen+'\n')
    return  prestamo.set(r)

def Final():
    elemen = var.get() 
    cantidad = cont.get()
    final = elemen + " " + cantidad
    return final

prestamo = tk.StringVar(ventana)
cont = tk.StringVar(ventana)
var = tk.StringVar(ventana)
string1 = tk.StringVar(ventana)
string1.set(str(id))
e3 = tk.Label(ventana, textvariable = string1, padx = 5, pady = 5, width = 50)
e3.pack()

var.set('Elementos disponibles')
opciones = ['Motor DC', 'Arduino', 'Raspberry', 'Sensor de Temperatura', 'Caja de Herramientas', 'Potenciometro']
opcion = tk.OptionMenu(ventana, var, *opciones)
opcion.config(width = 20)
opcion.pack(side = 'left', padx = 40, pady = 40)
e1 = tk.Label(ventana, text = "Elemento a prestar: ", bg = "slate gray", fg = "white")
e1.pack(padx = 5, pady = 5, ipadx = 5, ipady = 5, fill = tk.X)
elemento = tk.Label(ventana, bg = "dark slate gray", textvariable = var, padx = 5, pady = 5, width = 50)
elemento.pack()

e2 = tk.Label(ventana, text = "Cantidad a prestar: ", bg = "slate gray", fg = "white")
e2.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)
entrada = tk.Entry(ventana)
entrada.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

botonconfirmar_cant = tk.Button(ventana, text = "Confirmar cantidad ", fg = "slate gray", command = confirmar_cant)
botonconfirmar_cant.pack(side = tk.TOP)

res = tk.Label(ventana, bg = "white", textvariable = cont, padx = 5, pady = 5, width = 50)
res.pack()

botonconfirmar_prestamo = tk.Button(ventana, text = "Confirmar elementos ", fg = "slate gray", command = confirmar_prestamo)
botonconfirmar_prestamo.pack(side = tk.TOP)

final = tk.Label(ventana, bg = "white", textvariable = prestamo, padx = 5, pady = 5, width = 50)
final.pack()

#prestamoTotal = str(confirmar_prestamo()) + " " + str(confirmar_cant())
#print(prestamoTotal)
ventana.mainloop()

