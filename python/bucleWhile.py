# 'Sintaxis Del Bucle While'

# #Se crea una variable:
# variable = 'Valor'

# #Definimos una condicion para crear el ciclo:
# while variable == 'Valor':
#     #Se ejecuta si se cumple la condicion (Verdadera).
#     print("El codigo es verdadero")
# #Se ejecuta si no se cumple la condicio (falsa)
# print("Fin del bucle")

#Ejemplo
contador = 0

while contador < 10:
    print('LLegamos al final', contador )
    contador += 1

print('No cumple con la condicion dada')

#Ejercicio:
# Iniciamos con una variable llamada Name con una cadena vacía
name = ""

# Si la variable 'name' no es igual a "salir" sigue el bucle
while name.lower() != "exit":
    # Solicitamos al usuario que ingrese su nombre
    name = input("Please enter your name (type 'exit' if you want the loop to end): ")
    
    # Se analiza si el usuario no escribio salir
    if name.lower() != "exit":
        # Se envia un mensaje al usuario si se comprueba que no digito salir.
        print(f"Hello, {name}!")

# Si el usuario ingresa salir se muestra este mensaje
print("An end was given to the While loop :)")

x= 0
counter = 1

while counter <= 10:
    x += counter
    counter+=1
print(x)

