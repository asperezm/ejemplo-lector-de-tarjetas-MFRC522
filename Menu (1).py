import tkinter as tk

ventana = tk.Tk()
ventana.title("Sistema de prestamos")
e0 = tk.Label(ventana, text = "Bienvenidx ¿Qué elementos deseas prestar?", bg = "slate gray", fg = "white")
e0.pack(padx = 5, pady = 5, ipadx = 5, ipady = 5, fill = tk.X)

numId = tk.StringVar(ventana)
numId.set("12345")

num = tk.Label(ventana, bg = "dark slate gray", textvariable = numId, padx = 5, pady = 5, width = 50)
num.pack()

image = tk.PhotoImage(file = "EAFIT.png")
image = image.subsample(4,4)
label = tk.Label(image = image)
label.pack(side = 'left')

ventana.geometry('480x400+600+100')
ventana.configure(background = 'midnight blue')

def confirmar_cant():
    cant = int (entrada.get())
    return cont.set(cant)

def confirmar_prestamo():
    elemen = var.get() 
    cantidad = cont.get()
    r = cantidad, elemen
    print(r)
    return  prestamo.set(r)  
 
def abrirVentana2():
    ventana.withdraw()
    win = tk.Toplevel()
    win.geometry('480x400+600+100')
    win.configure(background = 'dark olive green')

    def confirmar_cant2():
        cant = int (entrada2.get())
        return cont2.set(cant)

    def confirmar_devolucion():
        elemen = var.get() 
        cantidad = cont.get()
        r = cantidad, elemen
        print(r)
        return  devolucion.set(r)      
    
    cont2 = tk.StringVar(win)
    devolucion = tk.StringVar(win)

    win.title("Sistema de devoluciones")
    e3 = tk.Label(win, text = "Bienvenidx ¿Qué elementos deseas devolver?", bg = "dark khaki", fg = "white")
    e3.pack(padx = 5, pady = 5, ipadx = 5, ipady = 5, fill = tk.X)
    
    numId = tk.StringVar(win)
    numId.set("12345")
    num = tk.Label(win, bg = "pale green", textvariable = numId, padx = 5, pady = 5, width = 50)
    num.pack()

    var2 = tk.StringVar(win)
    var2.set('Elementos')
    elementosDevol = ['Motor DC', 'Arduino', 'Raspberry', 'Sensor de Temperatura', 'Caja de Herramientas', 'Potenciometro']
    opcion = tk.OptionMenu(win, var2, *elementosDevol)
    opcion.config(width = 20)
    opcion.pack(side = 'left', padx = 40, pady = 40)
    elemento = tk.Label(win, bg = "dark sea green", textvariable = var2, padx = 5, pady = 5, width = 50)
    elemento.pack()  
    e4 = tk.Label(win, text = "Cantidad a devolver: ", bg = "dark khaki", fg = "white")
    e4.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)

    entrada2 = tk.Entry(win)
    entrada2.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)
    botonconfirmar = tk.Button(win, text = "Confirmar cantidad ", fg = "dark khaki", command = confirmar_cant2)
    botonconfirmar.pack(side = tk.TOP)
    res = tk.Label(win, bg = "white", textvariable = cont2, padx = 5, pady = 5, width = 50)
    res.pack()
    
    botonconfirmar_devolucion = tk.Button(win, text = "Confirmar elementos ", fg = "dark khaki", command = confirmar_devolucion)
    botonconfirmar_devolucion.pack(side = tk.TOP)

    final2 = tk.Label(win, bg = "white", textvariable = devolucion, padx = 5, pady = 5, width = 50)
    final2.pack()


    botonCerrar2 = tk.Button(win, text = "Finalizar", command = win.destroy)
    botonCerrar2.pack(side = tk.TOP)  

#Ventana 1

prestamo = tk.StringVar(ventana)
cont = tk.StringVar(ventana)
var = tk.StringVar(ventana)
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

botonCerrar = tk.Button(ventana, text = "Finalizar", command = ventana.destroy)
botonCerrar.pack(side = tk.TOP)
botonDevolver = tk.Button(ventana, text = "Devolver elementos", fg = "black", command = abrirVentana2)
botonDevolver.pack(side = tk.TOP)

ventana.mainloop()

