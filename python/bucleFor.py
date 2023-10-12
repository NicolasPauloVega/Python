# Sintaxis:
#--for variable in secuencia:
    # Código a ejecutar en cada iteración

#Ejemplo
for numero in range(1,6):
    print(numero)

#Taller
# Iniciamos con una variable para almacenar la suma
addition = 0

# Usamos un bucle for para recorrer los números del 1 al 10
for number in range(1, 11):
    # En cada iteración, sumamos el número actual al total
    addition += number

# Imprimimos el resultado de la suma
print(f"The sum of the numbers from 1 to 10 is: {addition}")
