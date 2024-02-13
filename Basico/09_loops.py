############# Loops  #########################

# While

my_condition = 0

while my_condition <10:
    print(my_condition)
    my_condition +=2
else:# es opcional
    print("mi condicion es mayor o igual a 10")   


while my_condition <20:
    my_condition +=1

    if my_condition==15:
        print("se detiene la ejecuacion")
        break

    print(my_condition)

print("\n")
# For
my_list=[35, 24, 62, 50, 30, 30, 17]

for element in  my_list:
    print(element)
print("\n")
my_tuple=(19, 1.68, "jhon", "galvis", "rodriguez", "galvis")
for element in  my_tuple:
    print(element)
print("\n")
my_set={"jhon", "galvis", 19}
for element in  my_set:
    print(element)
print("\n")
my_dict={
    "nombre":"jhon",
    "apellido":"galvis",
    "edad":35,
    "lenjuages": {"python", "java", "php"},
    1:1.68}

for element in  my_dict:
    print(element)

    if element == "edad":
        break

else:
    print("el bucle for para diccionario he finalizado")

print("la ejecucion continua")


for element in  my_dict:
    print(element)

    if element == "edad":
        continue
    print("se eejcuta")
else:
    print("el bucle for para diccionario he finalizado")

print("la ejecucion continua")


