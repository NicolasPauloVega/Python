aprendices = ["Juan Diego","Mathew Guarnizo","Maria Fernanda","Melissa","Nicolas Paulo","Miguel Angel","Stiven","Maicol Esteban","Kevin Londoño","Marlon","Maria Jose","Nataly","Camila","Stiwar","Lina Vanesa","Paula Garcia","Maria Paula","Vanesa","Kevin Hernandez","Yency","Matias","Sebastian Tovar","Cristian Peña","Dahiana","Kevin Eduardo","Santiago Tomas","Nicolas Fierro","Laura Benavidez","Willfran"]
edades = []

import random

for _ in range(30):
    edad = random.randint(16,20)
    edades.append(edad)

print(aprendices) #Imprimimos los resultados de las listas
print(edades)     #y edades

#Creamos una variable la cual preguntara si el usuario desea ver del 10 al 20 aprendiz
mostrar = input("Deseas ver del 10 al 20 aprendiz de la lista? [si o no] ")

#Creamos unas condiciones las cuales si el usuario desea ver del decimo aprendiz hasta el venteavo aprendiz se los mostrar y si no lo desea se los mostrara completa
if mostrar.lower() == "si":
    print(aprendices[9:21])
    print(edades[9:21])
else:
    print(aprendices)
    print(edades)