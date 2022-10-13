#Elabore un programa que permita la entrada de 100 números enteros y determine cual de ellos es un número primo.
#cambiar el 11 del ramgo por un 101

print("Ingresa una cadena de 100 numeros: ")
cont = 1
primo = 0
for cont in range(1,11):
    print ("ingrerese el numero ", cont)
    num = int (input ())
    x = num
    cont +=1
    if x % 2 != 0:
        primo = x
    print (primo, "es un numero primo")
#    else :
#        primo = 0