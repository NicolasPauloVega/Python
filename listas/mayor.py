aprendices = [] #Creamos una lista vacia llamada aprendices
edades = []     #y otra llamada edades

#Iniciamos un bucle for con una iteracion en un rango de 30.
for i in range(30):
    registro = input("Ingresa el nombre del aprendiz: ")    #Creamos una variable la cual almacene el nombre de los aprendices
    registro1 = int(input("Ingresa la edad del aprendiz: "))    #Creamos una variable la cual almacene la edad de los aprendices

    aprendices.append(registro) #Agregamos los valores de la variable registro en la lista de aprendices.
    edades.append(registro1)    #Agregamos los valores de la variable regitro1 en la lista de edades.

    print(aprendices) #Imprimimos los resultados de las listas
    print(edades)     #y edades

conteo = 0 #Creamos una variable la cual valla contando desde 0

#Iniciamos un bucle que al momento de detectar que una persona tiene 18 años cuente de 1 en uno
for registro1 in edades:
    if registro1 == 18:
        conteo+=1

print(conteo)