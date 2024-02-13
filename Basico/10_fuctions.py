####### Function #######

def my_fuction():
    print("esto es una funcion")


my_fuction()

def sum_two_values(first_number, second_number):
    print(first_number + second_number)


sum_two_values(5, 7)
sum_two_values(582763, 7235)
sum_two_values("5", "7")# junta los numeros por que los toma como strings
sum_two_values(1.4, 5.2)

def sum_two_values_with_return(first_number, second_number):
    my_sum= first_number + second_number
    return my_sum

my_result =sum_two_values_with_return(10, 5)
print(my_result)


def print_name(name, surname):

    print(f"{name} {surname}")

print_name(surname="jhon", name="jairo")

print("\n")
def print_name(name, surname, alias="sin alias"):

    print(f"{name} {surname} {alias}")

print_name("jhon", "jairo", "jhoncito")



def print_upper_text(*texts):
    for text in texts:
        print(text.upper())

print_upper_text("hola", "python", "moure")
print_upper_text("chao")

print("\n")

def nombre(nombre):

    nombre=input("ongrese su nombre? ")
    return (f" hola "+ nombre)
print(nombre(nombre))