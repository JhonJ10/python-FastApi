########## List ########

my_list =list()
my_other_list=[]

print(len(my_list))

my_list=[35,15,87,8,8,49]
print(len(my_list))

print("\n")
my_other_list=[25, 1.68, "jhon", "galvis"]
print(type(my_other_list))
print(type(my_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(8))


age, height, name, surname = my_other_list
print(name)

age, height, name, surname = my_other_list[2],  my_other_list[1],  my_other_list[0],  my_other_list[3]
print(surname)

print(my_list + my_other_list)

print("\n")
my_other_list.append("rodriguez")
print(my_other_list)

my_other_list.insert(1, "rojo")
print(my_other_list)

my_other_list[1]= "azul"
print(my_other_list)




#el remove elimina por nombre
my_other_list.remove("azul")
print(my_other_list)

print(my_list)
print(my_list.pop())
print(my_list)

my_pop_element=my_list.pop(2)
print(my_pop_element)
print(my_list)

# el DEL elimina por indice (pocision)
del my_list[2]
print(my_list)

my_new_list=my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

#pone los valores de atras hacia adelante
my_new_list.reverse()
print(my_new_list)

#ordena por orden
my_new_list.sort()
print(my_new_list)

print(my_new_list[1:2])

print("\n")

my_list= ["hola python"]
print(my_list)
print(type(my_list))