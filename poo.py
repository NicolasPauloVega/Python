#Consulte un ejemplo donde se declare una clase con atributos y métodos.

#Creamos un clase
class Perro():
    """ Modelo sencillo de un perro. """ #<--- Doc string que sirve para describir los bloques de codigo

    #Se crearan 3 metodos para perro que son para darle nombre y edad,sentarse y rodar.
    def __init__(self, nombre, edad): #<---- __init__ es un nombre predeterminado de python que ayuda a diferenciar de otros metodos
        """ Inicializa atributo de nombre y edad. """
        self.nombre = nombre
        self.edad = edad
    
    def sentarse(self):
        """ Simular sentarse."""
        print(self.nombre.title() + " Se ha sentado ")
    
    def rodar(self):
        """ Simular rodar en el piso. """
        print(self.nombre.title() + " rodó en el piso. ")

mi_perro = Perro("willie", 6) #Se crea una instancia la cual mostrara el nombre y la edad del perro
tu_perro = Perro("Lucy", 3)

print("Mi perro se llama" + mi_perro.nombre.title() + ".")
print("Mi perro tiene " + str(mi_perro.edad) + "años de edad.")

mi_perro.sentarse()
mi_perro.rodar()
print()
print("Tu perro se llama" + tu_perro.nombre.title() + ".")
print("Tu perro tiene " + str(tu_perro.edad) + "años de edad.")

tu_perro.sentarse() 
tu_perro.rodar()

print("---------------------------------------------------------------------------------------------------------------------")

#Crear una herencia

class Coche():
    """Una presentación sencilla de un coche."""
    def __init__(self, marca, modelo, ano):
        """Inicializamos los atributos para describir un coche."""
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.lecturaOdometro = 0 #<--- Con este medimos la velocidad (Km) del coche

    def obtenerNombreDescriptivo(self):
        """Regresa un nombre descriptivo."""
        nombreLargo = str(self.ano) + ' ' + self.marca + ' ' + self.modelo
        return nombreLargo.title() #<--- Pedimos a python que retorne los valores de nombreLargo con las iniciales en mayusculas.
    
    def leerOdometro(self):
        """Muestra el kilometraje del cocehe."""
        print("Este coche ha recorrido " + str(self.lecturaOdometro) + "Km")

    def actualizarOdometro(self, kilometraje):
        """
        Establecer la lectrura del odometro al valor asignado.
        Cancela los cambios en caso de retroceder el valor.
        """
        if kilometraje >= self.lecturaOdometro:
            self.lecturaOdometro = kilometraje
        else:
            print("No puedes retroceder el valor del odómetro.")

    def incrementarOdometro(self, kilometros):
        """Adiciona la cantidad asignada a la lectura del odómetro."""
        self.lecturaOdometro += kilometros

    def llenarTanqueGas(self):
        print("tanque lleno. ")

class CocheElec(Coche):
    """Representar las caracteristicas de un coche, especificamente coches electricos."""
    def __init__(self, marca, modelo, ano):
        """
        Inicializa los atributos de la clase padre.
        """
        super().__init__(marca,modelo,ano) #<--- Super() llama a la super clase en este caso Coche
        self.kwh = 70
    
    def descripcionBateria(self):
        """Imprime una frase describiendo el tamaño de la bateria."""
        print("Este coche tiene una bateria de " + str(self.kwh) + "kwh.")

    def llenarTanqueGas(self):
        """Los coches electricos no necesitan un tanque de gasolina."""
        print("Este coche no necesita un tanque d gasolina.")

miTesla = CocheElec('tesla', 'modelo s', 2022)
print(miTesla.obtenerNombreDescriptivo())
miTesla.descripcionBateria()
miTesla.llenarTanqueGas()

print("---------------------------------------------------------------------------------------------------------------------")


#Polismorfismo en python

class carro():
    """Mostrar el desplazamiento de un carro."""
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas.")
    
class moto():
    """Mostrar el desplazamiento de una moto."""
    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas. ")

class camion():
    """Mostrar el desplazamiento de un camion."""
    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas. ")

"""Cambia de forma el vahiculo para encontrar la clase que necesitemos"""
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo = camion()

desplazamientoVehiculo(miVehiculo)

print("---------------------------------------------------------------------------------------------------------------------")
