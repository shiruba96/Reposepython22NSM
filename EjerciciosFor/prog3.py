#Elabore un programa que permita la entrada de 100 números enteros y determine cual de ellos es un número primo.
#cambiar el 11 del ramgo por un 101

import random
print("Ingresa una cadena de 100 numeros: ")
cont = 1
primo = ""
for cont in range(1,101):
    
    num = random.randint (1,1000)
    #print ("ingrerese el numero ", cont)
    #num = int (input ())
    x = num
    if x % 2 != 0:
        primo = primo + str(x) + " "
print ("los numero primos son", primo)