#Elabore un programa que muestre los números enteros en forma descendente de un número a otro dado los 
# números se pueden dar en cualquier orden.
while True:
    try:
        print ("Ingresa el numero con el que vamos a iniciar")
        ni = int (input ())
        break
    except ValueError:
        print ("no es un numero valido")
while True:
    try:
        print ("Ingresa el numero con el que vamos a finalizar")
        nf = int (input ())
        break
    except ValueError:
        print ("no es un numero valido")
if ni < nf:
    aux = ni 
    ni = nf
    nf = aux
print ("Lista ordenada")
while ni >= nf:
    print (ni)
    ni -= 1
