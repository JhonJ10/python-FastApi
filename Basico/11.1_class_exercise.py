'''
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_datos(self):
        print("Hola, mi nombre es", self.nombre, "y tengo", self.edad, "años.")

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
persona = Persona(nombre, edad)
persona.imprimir_datos()


print("\n")
#utilizando unn poco de poo
class Persona:
    def __init__(self):
        self.nombre = input("Ingresa tu nombre: ")
        self.edad = input("Ingresa tu edad: ")

    def imprimir_datos(self):
        print("Hola, mi nombre es", self.nombre, "y tengo", self.edad, "años.")
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

persona = Persona()
persona.imprimir_datos()

'''
class coche:
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.arrancado=False

    def arrancar(self):
        self.arrancado=True
        print("el", self.marca, self.modelo,"se ha arrancado")
    
    def parar(self):
        print("el", self.marca, self.modelo, "se ha parado")

laguna=coche("renault", "laguna")
tesla=coche("tesla", "model 3")

print(type(laguna))
print(type(tesla))

print(laguna.marca,laguna.modelo)
print(tesla.marca, tesla.modelo)

laguna.arrancar()
tesla.arrancar()
print(laguna.arrancado)
print(tesla.arrancado)

laguna.parar()
tesla.parar()