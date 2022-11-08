#Elabore un programa que calcule e imprima el factorial de un número dado.
while True:
    try:
        print ("Ingresa un numero:")
        n = int (input ())
        break
    except ValueError:
        print ("no validp, intenta de nuevo")
cont = n
while cont != 1:
    cont -= 1 
    n = (n * cont) 
print("El Factorial es",n)