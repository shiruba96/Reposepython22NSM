#Elabore un programa que lea 100 números y diga cual es el mayor
#le puse 11 para hacer la prueba pero solo hay que cambiarlo por 101

print("Ingresa una cadena de 100 numeros: ")
cont = 1
mayor = 0
for cont in range(1,11):
    print ("ingrerese el numero ", cont)
    num = int (input ())
    x = num
    cont +=1
    if x > mayor:
        mayor = x
    else :
        mayor=mayor
print ("el numero mayor es", mayor)