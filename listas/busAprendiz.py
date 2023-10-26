#Indique un dato a buscar en la lista de aprendices

#Creamos una lista llamada aprendices con unos valores predeterminados y otra vacia llamada edades
aprendices = ["Juan Diego","Mathew Guarnizo","Maria Fernanda","Melissa","Nicolas Paulo","Miguel Angel","Stiven","Maicol Esteban","Kevin Londoño","Marlon","Maria Jose","Nataly","Camila","Stiwar","Lina Vanesa","Paula Garcia","Maria Paula","Vanesa","Kevin Hernandez","Yency","Matias","Sebastian Tovar","Cristian Peña","Dahiana","Kevin Eduardo","Santiago Tomas","Nicolas Fierro","Laura Benavidez","Willfran"]
edades = []

#Importamos el modulo ramdom el cual genera numeros aleatorios
import random

#Creamos un bucle el cual genera un total de 30 iteraciones.
for i in range(31):
    #creamos una variable la cual dara numeros randoms con la funcion "radint" que empiezan del 16 y terminan en el 20
    edad = random.randint(16,20)
    #Agregamos los datos de la variable edad a la lista edades
    edades.append(edad)

print(aprendices) #Imprimimos los resultados de las listas
print(edades)     #y edades

#Creamos una variable la cual pregunte si desea buscar un aprendiz o por el nombre o por la edad
entrar = input("Deseas buscar por nombre [n] o por edades[e] ")

#creamos unas condiciones las cuales busque al aprendiz ya sea por el nombre [n] o por la edad [e]
if entrar.lower() == "n":
    #Creamos una variable la cual pregunta a quien desea buscar.
    buscar = input("Digita el nombre del aprendiz que desea buscar: ").title()
    #Creamos una condicion la cual busca entre todos los aprendices el nombre que digito el usuario.
    if buscar in aprendices:
        #Creamos dos variables una que busca el nombre del aprendiz que digito el usuario y otra que busca en la misma posicion la edad del aprendiz.
        encN = aprendices.index(buscar)
        edad = edades[encN]
        #Se imprime un mensaje del nombre del aprendiz y la edad.
        print(f"La persona que buscas se llama {buscar} y tiene {edad} años de edad")
    else:
        #Se manda un mensaje de error si no se encuentra al aprendiz.
        print("La persona a la que buscas no esta en las lista que posee el programa.")
#Se crea otra condicion por si el usuario no quiere buscar al aprendiz por el nombre sino por la edad
elif entrar.upper() == "E":
    #Creamos una variable la cual pregunta la edad del aprendiz desea buscar.
    buscar = int(input("Digita la edad del aprendiz que desea buscar: "))
    #Creamos una condicion la cual buscara al aprendiz por la edad que digito el usuario.
    if buscar in edades:
        #Se crean dos variables las cuales son "encE" que se encarga de buscar la edad que coloco el usuario y otra llamdad "name" que busca el nombre del usuario por la posicion en la que se encuentre.
        encE = edades.index(buscar)
        name = aprendices[encE]
        #Se imprime un mensaje de la edad y el nombre del aprendiz.
        print(f"El aprendiz que buscas tiene {buscar} años de edad y se llama {name}")
    else:
        #Se manda un mensaje de error si no se encuentra al aprendiz.
        print("La persona a la que buscas no esta en las lista que posee el programa.")
else:
    #Se manda un mensaje de error si no se digita las letras solicitados.
    print("Error...")

# aprendices1 = ["Juan Diego","Mathew Guarnizo","Maria Fernanda","Melissa","Nicolas Paulo","Miguel Angel","Stiven","Maicol Esteban","Kevin Londoño","Marlon","Maria Jose","Nataly","Camila","Stiwar","Lina Vanesa","Paula Garcia","Maria Paula","Vanesa","Kevin Hernandez","Yency","Matias","Sebastian Tovar","Cristian Peña","Dahiana","Kevin Eduardo","Santiago Tomas","Nicolas Fierro","Laura Benavidez","Willfran"]