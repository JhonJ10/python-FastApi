## sets ####

my_set = set()
my_other_set= {}
print(type(my_set))
print(type(my_other_set))# inicialmente es un diccionario

my_other_set={"jhon", "galvis", 19}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("rodriguez")
print(my_other_set) # un set no es una estructura ordenada

my_other_set.add("rodriguez")
print(my_other_set) # un set no admite repetidos

print("\n")

print(my_other_set)

print( "jhon" in my_other_set)

print( "jairo" in my_other_set)

print("\n")
my_other_set.remove("jhon")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))
print("\n")
#del my_other_set
#print(my_other_set) NameError: name 'my_other_set' is not defined

my_set={"jhon", "galvis", 19}
my_set=list(my_set)
print(my_set)
print(my_set[0])

my_set = set(my_set)# my_set estaba como una lista y la pase a aun set 
                    # nuevamente para asi poder utilizar el union

print("\n")

my_other_set={"php", "java", "python"}
print(my_other_set)

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"javascript", "c#"}))

print(my_new_set.difference(my_set))