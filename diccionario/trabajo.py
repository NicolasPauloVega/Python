#Creamos un diccionario

computadores = {
    1 : {
        "ID": 922610128519,
        "Dispositivos": "Cargador y mouse",
        "Ambiente": 1
    },
    2 : {
        "ID" : 922610128501,
        "Dispositivos" : "cargador",
        "Ambiente": 1
    },
    3 : {
        "ID" : 922610128513,
        "Dispositivos" : "mouse",
        "Ambiente": 1
    },
    4 : {
        "ID" : 922610128492,
        "Dispositivos" : "cargador y mouse",
        "Ambiente": 1
    },
    5 : {
        "ID" : 922610128516,
        "Dispositivos" : "mouse",
        "Ambiente": 1
    },
    6 : {
        "ID" : 922610128515,
        "Dispositivos" : "cargador",
        "Ambiente": 1
    },
    7 : {
        "ID" : 922610128522,
        "Dispositivos" : "cargador y mouse",
        "Ambiente": 1
    },
    8 : {
        "ID" : 922610128514,
        "Dispositivos" : "cargador",
        "Ambiente": 1
    },
    9 : {
        "ID" : 922610128517,
        "Dispositivos" : "mouse",
        "Ambiente": 1
    },
    10 : {
        "ID" : 922610128512,
        "Dispositivos" : "cargador y mause",
        "Ambiente": 1
    },
    11 : {
        "ID" : 922610128510,
        "Dispositivos" : "cargador",
        "Ambiente": 1
    },
    12 : {
        "ID" : 922610128511,
        "Dispositivos" : "mouse",
        "Ambiente": 1
    },
    13 : {
        "ID" : 922610128520,
        "Dispositivos" : "cargador y mouse",
        "Ambiente": 1
    },
    14 : {
        "ID" : 922610128521,
        "Dispositivos" : "cargador",
        "Ambiente": 1
    },
    15 : {
        "ID" : 922610128518,
        "Dispositivos" : "mouse",
        "Ambiente": 1
    },
    16 : {
        "ID" : 922610128540,
        "Dispositivos" : "cargador y mouse",
        "Ambiente": 1
    }
}

#Imprimimos el diccionario
print(f"{computadores}")
#Linea de separacion
print("-------------------------------------------------------------------------------------------------------------------------------------------")
print()

#agregar novedades como fecha y descripcion

#Creamos una funcion
def agregarNovedad():

    #Pedimos el numero del computador para identificar la clave
    num = int(input("Ingrese el numero del computador: "))
    print()

    #Pedimos que nos den la fecha y la descripcion de la novedad
    fecha = input("Ingresa la fecha de la novedad: ")
    descrip = input("Ingrese la descripcion:")

    #Usamos la funcion update para añadir o agregar mas claves y valores a la funcion
    computadores[num].update({"Fecha": fecha, "Descripcion": descrip})

    #Imprimimos el resultado
    print(f"\nSe añadio la fecha y descripcion al diccionario {num}, {computadores[num]}")
    print()

#Llamamos la funcion
agregarNovedad()
print("-------------------------------------------------------------------------------------------------------------------------------------------")
print()

#Buscar un equipo por ID y mostrar informacion

#Creamos una funcion
def busacarEquipo():

    #Pedimos la id a buscar
    numId = int(input("Que equipodeseas encontrar por la ID "))

    #Creamos un bucle que busque en todas las llaves y valores hasta coincidir con el que coloco el usuario.
    for pc, idPc in computadores.items():
        
        #creamos una condicion la cual identifique si la id esta en el diccionario
        if idPc["ID"] == numId:
            print(f"el numero del computador es el {pc}: {computadores[pc]}")
        else:
            continue

#Llamamos la funcion
busacarEquipo()
print("-------------------------------------------------------------------------------------------------------------------------------------------")
print()

#Mostrar reportes de equipo

#Creamos una funcion
def mostrarReportes():

    #Pedimos el numero de la computadora a la cual se le quiere ver el reporte.
    n = int(input("¿Cual equipo deseas ver? "))

    #Imprimimos el resultado del computador.
    print(computadores[n])
    print()

#Llamamos la funcion
mostrarReportes()
print("-------------------------------------------------------------------------------------------------------------------------------------------")
print()

#Funciones agregar, modificar y eliminar.

#Creamos una funcion para agregar
def agregarPC():

    #Pedimos el numero del nuevo computador
    num = int(input("Ingresa el numero del nuevo computador: "))

    #Pedimos que ingrese la nueva id,los nuevos dispositivos y el ambiente
    numId = int(input("Ingresa la id del computador: "))
    dispo = input("¿Qué tiene el computador teclado o mauseo tienen las 2? ")
    amb = input("¿Cual es el numero del ambiente al que pertenece el pc? ")

    #Usamos update para agregar al diccionario el nuevo computador
    computadores.update({num: {"Id": numId, "Dispositivo": dispo, "Ambiente": amb}})
    print(f"\n{computadores}")

#Llamamos a la funcion
agregarPC()
print("-------------------------------------------------------------------------------------------------------------------------------------------")
print()

##Creamos una funcion para modificar
def modificar():
  #Pedimos el numero del computador que se quiere modificar
  num = int(input(f"Ingrese el numero del computador a modificar: "))

  #Creamos una condicion la cual preguntara que desea cambiar
  if num in computadores:
    numID = input("Deseas cambiar el id? (si o no)")
    if numID == 'si':
      n = int(input("Ingresa el nuevo id"))
      computadores[num]["ID"] = n
    else:
      print("No se ha cambiado el ID")
    numDispositivos = input("Deseas cambiar los dispositivos? (si o no)")
    if numDispositivos == 'si':
      n = input("Ingresa los nuevos dispositivos")
      computadores[num]["Dispositivos"] = n
    else:
      print("No se ha cambiado los dispositivos")
    numAmb = (input("Desea cambiar el ambiente (si o no)"))
    if numAmb == 'si':
       n = int(input("Ingresa el numero del nuevo ambiente: "))
       computadores[num]["Ambiente"] = n
    else:
       print("No se cambio el ambiente.")
    print(computadores)
  else:
    print("No existe el computador")

#Llamamos la funcion
modificar()
print("-------------------------------------------------------------------------------------------------------------------------------------------")
print()

#Creamos una funcion para eliminar
def eliminar():
   
   #Pedimos el numero del computador a eliminar
   n = int(input("Ingresa el numero del computador que deseas eliminar (debe estar registrado) "))

   #Usamos la funcion pop para eliminar la informacion del computador
   eliminado = computadores.pop(n)

   #Imprimimos el resultado
   print(f"Se acaba de eliminar el computador numero ({n}) cuyo valor es {eliminado}\n")
   print(computadores)

#Llamamos a la funcion
eliminar()