my_string= "mi string"
my_other_string= "mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_string="este es mi string \n con salto de linea"
print(my_new_string)

my_tab_string="\t este es un string con tabulacion"
print(my_tab_string)

my_scape_string="\t este es un string  \n escapado"
print(my_scape_string)


# Formato
#alguna de estas 2 formass son mas optimza y sencillas 
name, surname, age= "jhon", "galvis", 19
print("mi nombre es {} {} y mi eda es {}". format(name, surname, age) )
print("mi nombre es %s %s y mi eda es %s" %(name, surname, age))

print(f"mi nombre es {name} {surname} y mi eda es {age}")

# esto esta bien pero no es tan optimo
print ("mi nonbre es" + name + " " + surname + " " + "mi edad es " + str(age))

# desempaquetando carcteres

languaje= "pyhton"
a, b, c, d, e, f = languaje
print(a)
print(e)

# division

languaje_slice = languaje[1:3]
print(languaje_slice)

languaje_slice = languaje[1:2:4]
print(languaje_slice)


# reverse

reversed_languaje= languaje[::-1]
print(reversed_languaje)

# funciones

print(languaje.capitalize())
print(languaje.upper())
print(languaje.count("t"))
print(languaje.isnumeric())
print("1".isnumeric())
print(languaje.lower())

print(languaje.upper(). isupper())
