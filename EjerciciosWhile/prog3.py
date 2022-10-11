#Elabore un programa que calcule e imprima el factorial de un número dado.

print ("Ingresa un numero:")
n = int (input ())
cont = n
while cont != 1:
    cont -= 1 
    n = (n * cont) 
print("El Factorial es",n)