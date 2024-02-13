######### Exceptions halding   ##########3

numberOne=5
numberTwo=1
numberTwo="1" #Error, tendria que pasar el string a tipo num: int("1")

try:
    print(numberTwo + numberOne)
    print("nose ha producido un error")
except:
    print("se ha producido un error")

else:#opcional
    #se ejecuta si nose produce una excepcion
    print("la ejecucion continua correctamente")

finally:#opcional
    #se ejecuta siempre
    print("la ejecucion continua")

# excepciones por tipo
try:
    print(numberTwo + numberOne)
    print("nose ha producido un error")
except ValueError as error:
    print(error)



