# Variables

my_variable = "mi primera variable"
print(my_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_variable=str(my_int_variable)
print(my_int_to_variable)
print(type(my_int_to_variable))

my_bool_variable =True
print(my_bool_variable)

# Concatenacion de variables
print(my_variable, my_int_variable, my_bool_variable)
print("este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_variable))

# Variables en una sola linea, cuidado por uqe se pued confundir
name, surname, alias, age= "jhon", "galvis", 'jhoncito', 35
print("me llamo", name, surname, ". mi edad es:", age, ". y mi alias es", alias)

"""
name=input('whta is your name?')
age= input('how  old are you?')
print(name)
print(age)
"""

#cambiamo su tipo
name=19
age='oscar'

print(name)
print(age)

#  ¿forzamos el tipo?
address: str = "mi direccion"
address= True
print(type(address))