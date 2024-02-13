###########  Conditionals ############


my_condition= False

if my_condition:
    print("se ejecuta la condicion del if")

print("la ejecuacion continua")
print("\n")
my_condition=5*3

if my_condition ==10:
    print("se ejecuta la cocndicon del if")

elif my_condition > 10 and my_condition < 20 :
    print("es mayor que 10 y menor que 20")

elif my_condition == 25:
    print("es numero es igual 25")

else :
    print("es  menor o igual a 10 o mayor o igual que 20 o distinto")

print("la ejecuacion continua")

my_string= ""

if not my_string:
    print("mi cadena de texto  es vacia")

if my_string == "mi cadena de textooo":
    print("mi cadena de texto coinciden")




print("\n")


#Escribir un programa que pregunte al usuario su edad
# y muestre por pantalla si es mayor de edad o no.
'''
edad = int(input("Escriba su edad? "))

if edad >=18:
    print("¡en horabuena es mayor de edad!")
else: 
    print(f"no es mayor de edad{edad}")
'''

#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''   
contraseña= 1234 

pregunta= input("ingrese la contarseña?")

if pregunta == contraseña:
    print("la contraseña es correcta, bienvenido!!")

elif pregunta != contraseña:
    print("la contraseña es incorrecta, por favor ingrese la contraseña!!")

else:
    print("ingrese la contraseña")
'''

#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

name = input("¿Cómo te llamas? ")
gender = input("¿Cuál es tu sexo (M o H)? ")
if gender == "M":
    if name.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if name.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)