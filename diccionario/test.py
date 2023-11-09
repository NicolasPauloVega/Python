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

def eliminar():
   
   #Pedimos el numero del computador a eliminar
   n = int(input("Ingresa el numero del computador que deseas eliminar (debe estar registrado) "))

   #Usamos la funcion pop para eliminar la informacion del computador
   eliminado = computadores.pop(n)

   print(eliminado)
   print(computadores)

eliminar()