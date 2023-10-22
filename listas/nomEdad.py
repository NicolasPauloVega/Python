aprendices = [] #Creamos una lista vacia llamada aprendices
edades = []     #y otra llamada edades

#Iniciamos un bucle for con una iteracion en un rango de 30.
for i in range(30):
    registro = input("Ingresa el nombre del aprendiz: ") #Creamos una variable la cual almacene el nombre de los aprendices
    registro1 = int(input("Ingresa la edad del aprendiz: ")) #Creamos una variable la cual almacene la edad de los aprendices

    aprendices.append(registro) #Agregamos los valores de la variable registro en la lista de aprendices.
    edades.append(registro1) #Agregamos los valores de la variable regitro1 en la lista de edades

    #Creamos otro bucle for para unir las 2  listas y mostrar a los aprendices con su respectiva edad
    for registro, registro1 in zip(aprendices,edades):
        print(f"El aprendiz {registro} Tiene {registro1} años de edad")