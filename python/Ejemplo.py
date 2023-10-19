#Creamos dos variables.

numbre1 = int(input("Ingresa un numero: "))
numbre2 = int(input("Ingresa otro numero: "))

#Creamos una nueva variable para seleccion lo que se hara con los numeros

eleccion = 0

#Creamos un bucle while

while eleccion != 6:

    #Mostrara un grafico de las opciones que tendra el usuario

    print("""
    Indique la operacion a realizar:
    
    1) Suma.
    2) Resta.
    3) Multiplicacion.
    4) Division.
    5) Cambio de valores.
    6) salir
    """)

    eleccion = int(input())

    #Ahora Vamos a crear unas condiciones en donde si se cumplen arrojaran un resultado.

    if eleccion == 1:
        print(" ")
        print("Resultado: ", numbre1,"+",numbre2,"=",numbre1+numbre2)

    if eleccion == 2:
        print(" ")
        print("Resultado: ", numbre1,"-",numbre2,"=",numbre1-numbre2)

    if eleccion == 3:
        print(" ")
        print("Resultado: ", numbre1,"x",numbre2,"=",numbre1*numbre2)

    if eleccion == 4:
        print(" ")
        print("Resultado: ", numbre1,"/",numbre2,"=",numbre1/numbre2)

    if eleccion == 5:
        numbre1 = int(input("Ingresa un numero: "))
        numbre2 = int(input("Ingresa otro numero: "))

    if eleccion == 6:
        print("Gracias por tu participacion :).")