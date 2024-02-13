############  Diccionarios ##########

my_dict = dict()
my_other_dict={}

print(type(my_dict))
print(type(my_other_dict))

print("\n")

my_other_dict = {"nombre":"jhon", "apellido":"galvis", "edad":35, 1:"python"}
print(my_other_dict)

my_dict={
    "nombre":"jhon",
    "apellido":"galvis",
    "edad":35,
    "lenjuages": {"python", "java", "php"},
    1:1.68}

print(my_dict)

print("\n")
print(len(my_dict))

print(my_dict["nombre"])

my_dict["nombre"] = "pedro"
print(my_dict["nombre"])

print(my_dict[1])

my_dict["calle"] = "calle stret"
print(my_dict)

del my_dict["calle"]
print(my_dict)


print("jhon" in my_dict)
print("apellido" in my_dict)

print(my_dict.items())#muestra todos los items del diccionario
print(my_dict.keys())# muestra la llave
print(my_dict.values())#muestra el valor de lo que dentro dela llave

my_list =["nombre", 1, "piso"]


my_new_dict=dict.fromkeys((my_list))# fromkeys crea un dicciona pero sin valores
print(my_new_dict)

my_new_dict=dict.fromkeys(("nombre", 1, "piso"))# fromkeys crea un dicciona pero sin valores
print(my_new_dict)


my_new_dict=dict.fromkeys(my_dict)# fromkeys me muestra los valores de my_dict pero solo muestra la clave mas no los valores del diccionario my_list
print(my_new_dict)


my_new_dict=dict.fromkeys(my_dict, "jairo")# 
print(my_new_dict)
