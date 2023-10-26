#Añadir a la instructora a la lista

aprendices = ["Juan Diego","Mathew Guarnizo","Maria Fernanda","Melissa","Nicolas Paulo","Miguel Angel","Stiven","Maicol Esteban","Kevin Londoño","Marlon","Maria Jose","Nataly","Camila","Stiwar","Lina Vanesa","Paula Garcia","Maria Paula","Vanesa","Kevin Hernandez","Yency","Matias","Sebastian Tovar","Cristian Peña","Dahiana","Kevin Eduardo","Santiago Tomas","Nicolas Fierro","Laura Benavidez","Willfran"]
edades = []

import ramdom

for i in range(30):
    edad = ramdom.radit(16,20)
    edades.append(edad)

print(aprendices)
print(edades)

aprendices.insert(1, "Adriana Lucia")
print(aprendices)
print(edades)