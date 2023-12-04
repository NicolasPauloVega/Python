#proyecto 6 de diciembre
from tkinter import * #Importamos todos los valores de la libreria tkinter

ventana = Tk() #Creamos la ventana donde se almacena toda la informacion del programa
ventana.title("Calculadora") #Colocamos un titulo para la ventana.

i = 0 #Creamos una variable global

#Entrada
eTexto = Entry(ventana, font=("calibri 20")) #se crea una caja de texto que almacena la informacion que ingrese el usuario.
eTexto.grid(row=0, column=0, columnspan= 4, padx=5, pady=5) #Se indica como estará ubicada la caja de texto en la ventana.

#Funciones
"""Se crea una funcion que almacene los valores de cada boton y los muestre en la caja de texto"""
def clickBoton(valor):
    global i #Llamamos a esa variable global
    eTexto.insert(i, valor) #Insertamos los valores de los botones en una posicion en especifico
    i += 1 #Ampliamos la posicion para evitar que todos los valores se inserten en la posicion predeterminada

"""Se crea una funcion que elimite absolutamente todos los valores que se encuentra en la caja de texto"""
def borar():
    eTexto.delete(0, END) #Elimina los valores desde la posicion 0 hasta la ultima posicion
    i = 0 #Se resetea la variable global a su valor predeterminado

"""Se crea una funcion que realice las operaciones matematicas"""
def operaciones():
    ecuacion = eTexto.get() #Almacenamos todos los valores de la caja de texto en la variable ecuacion
    resultado = eval(ecuacion) #Creamos una variable la cual realizara las operaciones que se encuentren en la caja de texto.
    eTexto.delete(0, END) #Eliminamos los datos que hay en la caja de texto
    eTexto.insert(0, resultado) #insertamos los valores de la caja de texto
    i = 0 #resetea la variable global a su valor predeterminado

#botones
"""Se crean 10 botones que representaran los numero con su debido tamaño y separacion"""
boton1 = Button(ventana, text="1", width=5, height=2, command= lambda: clickBoton(1))
boton2 = Button(ventana, text="2", width=5, height=2, command= lambda: clickBoton(2))
boton3 = Button(ventana, text="3", width=5, height=2, command= lambda: clickBoton(3))
boton4 = Button(ventana, text="4", width=5, height=2, command= lambda: clickBoton(4))
boton5 = Button(ventana, text="5", width=5, height=2, command= lambda: clickBoton(5))
boton6 = Button(ventana, text="6", width=5, height=2, command= lambda: clickBoton(6))
boton7 = Button(ventana, text="7", width=5, height=2, command= lambda: clickBoton(7))
boton8 = Button(ventana, text="8", width=5, height=2, command= lambda: clickBoton(8))
boton9 = Button(ventana, text="9", width=5, height=2, command= lambda: clickBoton(9))
boton0 = Button(ventana, text="0", width=15, height=2, command= lambda: clickBoton(0))

"""Se crean 4 botones Se agregan los 4 botones de caracteres especiales con su debido tamaño y separacion"""
botonBorrar = Button(ventana, text="AC", width=5, height=2, command= lambda: borar())
botonParentesis1 = Button(ventana, text="(", width=5, height=2, command= lambda: clickBoton("("))
botonParentesis2 = Button(ventana, text=")", width=5, height=2, command= lambda: clickBoton(")"))
botonPunto = Button(ventana, text=".", width=5, height=2, command= lambda: clickBoton("."))

"""Se crean 5 botones que representaran las operaciones y la igualdad con su debido tamaño y separacion"""
botonDiv = Button(ventana, text="÷", width=5, height=2, command= lambda: clickBoton("÷"))
botonMul = Button(ventana, text="x", width=5, height=2, command= lambda: clickBoton("*"))
botonSum = Button(ventana, text="+", width=5, height=2, command= lambda: clickBoton("+"))
botonRes = Button(ventana, text="-", width=5, height=2, command= lambda: clickBoton("-"))
botonIgual = Button(ventana, text="=", width=5, height=2, command= lambda: operaciones())

#agregar botones en pantalla.
"""Se agregan los botones que iran en la primera fila y representaran las columnas"""
botonBorrar.grid(row=1, column=0, padx=5, pady=5)
botonParentesis1.grid(row = 1,column = 1, padx = 5, pady = 5)
botonParentesis2.grid(row = 1,column = 2, padx = 5, pady = 5)
botonDiv.grid(row = 1,column = 3, padx = 5, pady = 5)

"""Se agregan los botones que iran en la segunda fila y representaran las columnas"""
boton7.grid(row = 2,column = 0, padx = 5, pady = 5)
boton8.grid(row = 2,column = 1, padx = 5, pady = 5)
boton9.grid(row = 2,column = 2, padx = 5, pady = 5)
botonMul.grid(row = 2,column = 3, padx = 5, pady = 5)

"""Se agregan los botones que iran en la tercera fila y representaran las columnas"""
boton4.grid(row = 3,column = 0, padx = 5, pady = 5)
boton5.grid(row = 3,column = 1, padx = 5, pady = 5)
boton6.grid(row = 3,column = 2, padx = 5, pady = 5)
botonSum.grid(row = 3,column = 3, padx = 5, pady = 5)

"""Se agregan los botones que iran en la cuarta fila y representaran las columnas"""
boton1.grid(row = 4,column = 0, padx = 5, pady = 5)
boton2.grid(row = 4,column = 1, padx = 5, pady = 5)
boton3.grid(row = 4,column = 2, padx = 5, pady = 5)
botonRes.grid(row = 4,column = 3, padx = 5, pady = 5)

"""Se agregan los botones que iran en la ultima fila y representaran las columnas"""
boton0.grid(row = 5,column = 0, columnspan= 2, padx = 5, pady = 5)
botonPunto.grid(row = 5,column = 2, padx = 5, pady = 5)
botonIgual.grid(row = 5,column = 3, padx = 5, pady = 5)

ventana.mainloop() #reconoce todos los eventos que ocurran en el programa.