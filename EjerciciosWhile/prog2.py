#Elabore un programa que calcule y muestre la sumatoria de los números enteros múltiplos de 5, 
#comprendidos entre el 1 y n, es decir, 5 + 10 + 15 +.... + n.

print ("Ingresa la cantidad de multiplos a mostrar")
m = int (input ())
cont = m
num = 5
i = 1
x = num
suma = 0
print ("Los multiplos son: ")
while cont > 0:
#aqui comenzamos hace la sumatoria 
    suma = suma + x
    print (x)
    cont -= 1
    i += 1
    num = num * i
    x = num
    num= 5
print("y la sumatoria es",suma)
    
