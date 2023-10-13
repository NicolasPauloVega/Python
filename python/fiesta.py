print("-----------------Bienvenido a la noche de brujas-----------------\n")
print("-----Ha llegado el momento de ser un heroe y salvar el mundo-----\n")
print("-Nuestras fiesta esta llena de sorpresas divertidas y deliciosas-\n")

print("Para poder dar ingreso se deben seguir las siguientes instrucciones: \n1.Debe ir disfrasado de algun superheroe de marvel (Deedpool,Iron Man,Hulk,Capitan America)\n2.Debe ser mayor de edad (tener 18 años)\n3.No traer bebidas alcoholicas de lugares externos(realizar requisa)\n4.No traer armas corto punzantes o fuego.\n")

#Numero de persona que quieren ingresar
count = 0

#Numero de personas que no pueden ingresar por no cumplir requisitos.
count1 = 0

guardia = input("Ingresa tu nombre: \n")

def valIngreso():
    ingreso = input("Es hora de comenzar? Digita si\n")
    return ingreso.lower() == "si"


while True:

    #Se arroja un saludo para poder seguir con el bucle.000000000000
    print("Hola porfavor completa el registro de la persona como es debido.\n")

    if valIngreso():
        print("Empazamos.... \n")
        
        print("Para comprobar si esta disfazado de un super heroe de marvel comprueba con una letra si cumple con la condicion: \n 1)Iron Man(I) \n 2)Dedpool(D) \n 3)Capitan America(C) \n 4)Hulk(H) \n 5)Spiderman(S) \n 6)Capitana Marvel(CM) \n 7)Otro(O) \n")

        disfraz = input("Dijita los signos dicho anterior mente: \n")
        
        if disfraz.lower() == "i":
            print("Puede ingresar.\n")
        elif disfraz.lower() == "d":
            print("Puede ingresar.\n")
        elif disfraz.lower() == "c":
            print("Puede ingresar.\n")
        elif disfraz.lower() == "h":
            print("Puede ingresar.\n")
        elif disfraz.lower() == "s":
            print("Puede ingresar.\n")
        elif disfraz.lower() == "cm":
            print("Puede ingresar.\n")
        else:
            print("completa el registro...\n")
            continue

        edad = int(input("Ingresa la edad del usuario: \n"))

        if edad < 18:
            print("No puede ingresar.\n")
        elif edad == 18:
            print("Puede ingresar.\n")
        elif edad > 18:
            print("Puede ingresar\n")
        else:
            print("completa el registro...\n")
            continue

        req = input("Realiza una requisa y en el caso de que el usuario tenga una bebida alcoholica en su posesion no dejarlo entrar y en el caso de no tener dejarlo pasar (Digitar [si o no])\n")

        if req.lower() == "si":
            print("No puede ingresar.\n")
        elif req.lower() == "no":
            print("Puede ingresar.\n")
        else:
            print("completa el registro...\n")

        request = int(input("Realiza una requisa en la cual identifique si el usuario posee un arma cortopunzante o fuego de la siguiente manera:\n1 para armas de fuego\n2 para armas blanca o cortopunzante\n3 para identificar que no posee\n"))

        if request == 1:
            print("No puede ingresar. (en caso de querer ingresar usar la fuerza)\n")
        elif request == 2:
            print("No puede ingresar. (en caso de querer ingresar usar la fuerza)\n")
        else:
            print("Puede ingresar.\n")

        fin = input("Deseas terminar el registro? [si o no]")

        if fin.lower() == "si":
            print("Gracias por terminar el registro.")
            break

