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

