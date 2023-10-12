print("-----------------Bienvenido a la noche de brujas-----------------")
print("-----Ha llegado el momento de ser un heroe y salvar el mundo-----")
print("-Nuestras fiesta esta llena de sorpresas divertidas y deliciosas-")

print("Para poder dar ingreso se deben seguir las siguientes instrucciones: \n1.Debe ir disfrasado de alfun superheroe de marvel (Deedpool,Iron Man,Hulk,Capitan America)\n2.Debe ser mayor de edad (tener 18 años)\n3.No traer bebidas alcoholicas de lugares externos(realizar requisa)\n4.No traer armas corto punzantes o fuego.")

#Numero de persona que quieren ingresar
count = 0

#Numero de personas que no pueden ingresar por no cumplir requisitos.
count1 = 0

#Numero de personas que pueden ingresar ya que cumplen los requisitos.
count2 = 0

while True:
    #Se crea una variable la cual almacene el nombre del guardia designado al ingreso.
    guardia = input("Ingrese su nombre: ")

    #Se arroja un saludo para poder seguir con el bucle.000000000000
    print("Hola {guardia} porfavor completa el registro de la persona como es debido.")

