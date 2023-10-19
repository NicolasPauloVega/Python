#Imprimimos mensajes los cuales dan la bienvenida a la fiesta
print("-----------------Bienvenido a la noche de brujas-----------------\n")
print("-----Ha llegado el momento de ser un heroe y salvar el mundo-----\n")
print("-Nuestras fiesta esta llena de sorpresas divertidas y deliciosas-\n")

#Imprimimos las reglas de ingreso
print("Para poder dar ingreso se deben seguir las siguientes instrucciones: \n1.Debe ir disfrasado de algun superheroe de marvel (Deedpool,Iron Man,Hulk,Capitan America)\n2.Debe ser mayor de edad (tener 18 años)\n3.No traer bebidas alcoholicas de lugares externos(realizar requisa)\n4.No traer armas corto punzantes o fuego.\n")


s = 0

n = 0

#Le pedimos al usuario que digite su nombre
guardia = input("Ingresa tu nombre: \n")

#creamos una funcion llamada valInreso() la cual se encargara de ejecutar el codigo
def valIngreso():
    ingreso = input("Es hora de comenzar? Digita si\n")
    return ingreso.lower() == "si"


while True:

    #Se arroja un saludo para poder seguir con el bucle.
    print(f"\nSr.{guardia} porfavor revisa las condiciones de ingreso y vuelvalo a intentar.\n")

    #Validamos si el usuario digito si para ejecutar el registro
    if valIngreso():
        #Iniciamos el registro
        print("Empazamos.... \n")
        
        #Se arroja un mensale el cual tendra todas las condiciones que debe cumplir un usuario para ingresar a la fiesta
        print("Para comprobar si esta disfazado de un super heroe de marvel comprueba con una letra si cumple con la condicion: \n 1)Iron Man(I) \n 2)Dedpool(D) \n 3)Capitan America(C) \n 4)Hulk(H) \n 5)Spiderman(S) \n 6)Capitana Marvel(CM) \n 7)Otro(O) \n")

        #Le pedimos que digite una letra la cual pertenece a una funcion y comprobar si se cumple
        disfraz = input("Dijita los signos dicho anterior mente: \n")
        
        if disfraz.lower() == "i":
            print("Puede ingresar.\n")
            s = s+1
        elif disfraz.lower() == "d":
            print("Puede ingresar.\n")
            s = s+1
        elif disfraz.lower() == "c":
            print("Puede ingresar.\n")
            s = s+1
        elif disfraz.lower() == "h":
            print("Puede ingresar.\n")
            s = s+1
        elif disfraz.lower() == "s":
            print("Puede ingresar.\n")
            s = s+1
        elif disfraz.lower() == "cm":
            print("Puede ingresar.\n")
            s = s+1
        else:
            print("No completo el registro...\n")
            n = n+1
            continue
        
        #Le pedimos al usuario que digite la edad del usuario para determinar si es mayor de edad o menor (el mayor puede ingresar)
        edad = int(input("Ingresa la edad del usuario: \n"))

        if edad < 18:
            print("No puede ingresar.\n")
            s = s+1
            continue
        elif edad == 18:
            print("Puede ingresar.\n")
            s = s+1
        elif edad > 18:
            print("Puede ingresar\n")
            s = s+1
        else:
            print("No completo el registro...\n")
            n = n+1
            continue

        #Se pide al guardia que digite si el usuario trajo alguna bebida que no pertenezca a la discoteca y la quiere ingresar (no puede entrar)
        req = input("Realiza una requisa y en el caso de que el usuario tenga una bebida alcoholica en su posesion no dejarlo entrar y en el caso de no tener dejarlo pasar (Digitar [si o no])\n")

        if req.lower() == "si":
            print("No completo el registro...\n")
            s = s+1
            continue
        elif req.lower() == "no":
            print("Puede ingresar.\n")
            s = s+1            
        else:
            print("No completo el registro...\n")
            n = n+1
            continue

        #Se pide al guardia que digite si el usuario trajo algun tipo de arma y quiera ingresar (no puede entrar).
        request = int(input("Realiza una requisa en la cual identifique si el usuario posee un arma cortopunzante o fuego de la siguiente manera:\n1 para armas de fuego\n2 para armas blanca o cortopunzante\n3 para identificar que no posee\n"))

        if request == 1:
            print("No puede ingresar. (en caso de querer ingresar usar la fuerza)\n")
            n = n+1
            continue
        elif request == 2:
            print("No puede ingresar. (en caso de querer ingresar usar la fuerza)\n")
            n = n+1
            continue
        else:
            print("Puede ingresar.\n")
            s = s+1

        #aqui le damos fin al bucle y la encuesta en caso de no dijitar si el bucle se repite.
        fin = input("Deseas terminar el registro? [si o no]")

        if fin.lower() == "si":
            print("Gracias por terminar el registro.\n")
            break

# conTotalSi = contadorSi-3
# conTotalNo = contadorNo-3

# print(f"Ingresaron: {contadorSi}\n")
# print(f"No Ingresaron: {contadorNo}")

if s >= 4:
    s += 1
else:
    print("No cumplio la funcion")

if n >= 4:
    n+1
else:
    print("No cumplio la funcion")

print(f"Ingresaron: {s}")
print(f"No ingresaron: {n}")