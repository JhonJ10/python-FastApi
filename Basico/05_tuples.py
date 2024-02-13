########### TUPLES ####################

my_tuple= tuple()
my_other_tuple=()

my_tuple=(19, 1.68, "jhon", "galvis", "rodriguez", "galvis")
my_other_tuple=("jairo", 34, 50)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) indexErro
#print(my_tuple[-6]) indexError


print(my_tuple.count("galvis"))
print(my_tuple.index("jhon"))
print(my_tuple.index("rodriguez"))

#my_tuple[1]= 1.80 es un error nose puede
sum_tuple=my_tuple + my_other_tuple
print(sum_tuple)

print(sum_tuple[3:6])

my_tuple=list(my_tuple)
print(type(my_tuple))

my_tuple[4]= "fosky"
my_tuple.insert(1, "azul")
print(my_tuple)

my_tuple=tuple(my_tuple)
print(tuple(my_tuple))
print(type(my_tuple))

del my_tuple
print(my_tuple)