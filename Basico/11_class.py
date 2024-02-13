########## Class #################

class MyEmptyPerson:
    pass

print(MyEmptyPerson())
print(MyEmptyPerson)


class Person:
    def __init__(self, name,surname) :
        self.name=name
        self.surname=surname,

my_person= Person("jhon", "galvis")
print(my_person.name)

print("\n")

class Person: # en esta clase defino los valores como nombre y apellido
    def __init__(self) :
        self.name="jhon"
        self.surname="galvis"

my_person= Person()
print(f"{my_person.name}, {my_person.surname}")

print("\n")

class Person: 
    def __init__(self, name, surname, alias="sin alias") :
        self.full_name= f"{name}, {surname} ({alias})"
        self.__name= name
        self.__surname= surname

    def get_name(self):
        return self.__name #propiedad privada
    
    def walk(self):
        print( f"{self.full_name} esta caminando")


my_person= Person("jhon", "galvis")
print(my_person.full_name)

print(my_person.get_name)
my_person.walk()

my_other_person= Person("jhon", "galvis", "jhoncito")# estoy reemplazndo un valor que venia por defecto en el alias
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name="hector de leon (el loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name= 666
print(my_other_person.full_name)



