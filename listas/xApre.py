aprendices = [] #Creamos una lista vacia llamada aprendices
edades = []     #y otra llamada edades

#Iniciamos un bucle for con una iteracion en un rango de 30.
for i in range(30):
    registro = input("Ingresa el nombre del aprendiz: ") #Creamos una variable la cual almacene el nombre de los aprendices
    registro1 = int(input("Ingresa la edad del aprendiz: ")) #Creamos una variable la cual almacene la edad de los aprendices

    aprendices.append(registro) #Agregamos los valores de la variable registro en la lista de aprendices.
    edades.append(registro1)    #Agregamos los valores de la variable regitro1 en la lista de edades

print(aprendices) #Imprimimos los resultados de las listas
print(edades)     #y edades

x = input("Ingresa el nombre del nuevo aprendiz: ") #Creamos una variable la cual almacene el valor que queremos agregar [nombre]
xE = int(input("Ingresa la edad del nuevo aprendiz: ")) #Creamos una variable la cual almacene el valor que queremos agregar [edad]

aprendices.append(x) #Agregamos el valor de la variable [x(nombre)] a la lista {aprendices}
edades.append(xE) #Agregamos el valor de la variable [xE(edad)] a la lista {edades}

#Finalmente imprimimos todas las listas
print(aprendices)
print(edades)