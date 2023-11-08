# Declarar Diccionarios

d = {'nombre': 'sandra', 'edad': 44}
    # Para declarar un diccionario utilizamos la palabra clave dict() o con una variable que lo almacene despues la iniciamos con {} y en su interior usamos una clave ('nombre') y un valor (44).

    #Recordar usar el mismo tipo de datos para cada clave no se puede hacer asi d = {'nombre':'sandra, 44: 'edad'} y repetir el mismo nombre de la clave en el diccionario.

# Acceder al diccionario.

print(d['nombre']) # Para mostrar el diccionario usamos print identificando como se llama el diccionario (d) y despues usamos la palabra clave para mostrar solo el valor.

print(d.get('nombre','No existente')) #Aqui lo que estamos haciendo es basicamente buscar en los paramentros solo el nombre de la persona.

#Agregar datos a un diccionario.

d.update({"Rosa": 3.7, "German": 4.8}) #Para agregar una nueva clave y valor al diccionario.
print(d)

#Iterar un diccionario

#Existen diferentes tipos de tecnicas para iterar un diccionario.
print('----------------------------------------------------------')

#Esta manera de iterar mostrara solo las llaves del diccionario (nombre,edad,Roda y German)
print("tecnicas por clave")
for i in d.keys():
    print(i)

print('---------------------------------------------------------')

#Esta manera de iterar mostrara solo los valores del diccionario (sandra,44,3.7 y 4.8)
print("Iterar por valor")
for i in d.values():
    print(i)

print('--------------------------------------------------------')

#Operaciones en diccionarios

#En este diccionario lo que hacemos es realizar una potenciacion cuadrada es decir que cualquier numero en el que pase x (2,4,6) lo va a multiplicar las veces en las que este potenciado (2) y usamos un print para mostrar el resultado.
opc = {x: x**2 for x in (2,4,6)}
print(opc)

print('-------------------------------------------------------')

#Eliminar elemento del diccionario

#Eliminamos a rosa del diccionario eliminando su clave(i) y su valor(j) finalmente imprimimos los resultados
del(d["Rosa"])
for i, j in d.items():
    print(i,j)

print('------------------------------------------------------')

#Funciones

#Una funcion se crea con la palabra clabe def el nombre de la funcion y el valor que se le quiere dar a esa funcion.
def saludar():
    print("saludo")

def retornarNumero():
    return 1

#Imprimimos las funciones.
saludar()
retornarNumero()

#Creamos una condicion la cual al detectar que la funcion(retornarNumero) tiene un valor de uno mostrara un mensaje.
if retornarNumero == 1:
    print("Devolvio un uno")
else:
    print("No devolvio un uno")

print('---------------------------------------------------')

#Funciones con parametro()

#Creamos una funcion(raiz) la cual entre sus valores tiene un value el cual al momento de imprimir se escoge que numero desee imprimir.
def raiz(value):
    return value**(1/2)

print(f"La raiz cuadrada de {raiz(4):.0f}")

#En este ejemplo se comprueba si obj vale 1 si vale sera verdadero(True) o falso(False).
def validarSiExiste(obj):
    if obj:
        print(f"{obj} is True")
    else:
        print(f"{obj} is False")
    
validarSiExiste(1)

