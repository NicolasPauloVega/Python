#Borre el nombre de la instructora de la lista

#Creamos una lista llamada aprendices con unos valores predeterminados y otra vacia llamada edades
aprendices = ["Adriana Lucia Rincon","Juan Diego","Mathew Guarnizo","Maria Fernanda","Melissa","Nicolas Paulo","Miguel Angel","Stiven","Maicol Esteban","Kevin Londoño","Marlon","Maria Jose","Nataly","Camila","Stiwar","Lina Vanesa","Paula Garcia","Maria Paula","Vanesa","Kevin Hernandez","Yency","Matias","Sebastian Tovar","Cristian Peña","Dahiana","Kevin Eduardo","Santiago Tomas","Nicolas Fierro","Laura Benavidez","Willfran"]
edades = [40]

#Importamos el modulo ramdom el cual genera numeros aleatorios
import random

#Creamos un bucle el cual genera un total de 30 iteraciones.
for i in range(30):
    #creamos una variable la cual dara numeros randoms con la funcion "radint" que empiezan del 16 y terminan en el 20
    edad = random.randint(16,20)
    #Agregamos los datos de la variable edad a la lista edades
    edades.append(edad)

print(aprendices) #Imprimimos los resultados de las listas
print(edades)     #y edades

#Creamos una variable la cual pregunte si se desea eliminar a "Adrana Lucia de la lista"
eliminar = input('deseas eliminar a la instructora "Adriana Lucia" de la lista [Dijitar si o no]')

#Si dice que si se procedera a eliminarla de la lista
if eliminar.lower() == "si":
    #Se elimina de las dos listas con remove()
    aprendices.remove("Adriana Lucia")
    edades.remove(0)
    #Se le notifica al usuario que se elimino el valor de las listas mostranto a aprendiz y edades
    print(f"Se elimino a la instructora adriana de la lista aprendices. \n{aprendices}={edades}")
else:
    #Si decide no eliminar el valor se arroja este mensaje
    print(f'No se elimino a la instructora "Adriana Lucia" de la lista. \n{aprendices}={edades}')

# aprendices1 = ["Juan Diego","Mathew Guarnizo","Maria Fernanda","Melissa","Nicolas Paulo","Miguel Angel","Stiven","Maicol Esteban","Kevin Londoño","Marlon","Maria Jose","Nataly","Camila","Stiwar","Lina Vanesa","Paula Garcia","Maria Paula","Vanesa","Kevin Hernandez","Yency","Matias","Sebastian Tovar","Cristian Peña","Dahiana","Kevin Eduardo","Santiago Tomas","Nicolas Fierro","Laura Benavidez","Willfran"]