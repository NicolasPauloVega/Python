#Creamos dos listas las cuales tienen 2 valores predeterminados los cuales son "Adriana Lucia" y 0
aprendices = ["Adriana Lucia"]
edades = [0]

#Creamos un bucle el cual nos permite ingresar mas valores a las listas
for i in range(30):
    registro = input("Ingresa el nombre del aprendiz: ")
    registro1 = int(input("Ingresa la edad del aprendiz: "))

    #Agregamos los valores dado en registro y registro1 a la lista aprendices y edades
    aprendices.append(registro)
    edades.append(registro1)

#Imprmimos cada lista
print(aprendices)
print(edades)

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