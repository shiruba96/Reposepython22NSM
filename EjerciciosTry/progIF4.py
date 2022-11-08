#Elaborar un programa para que lea tres números diferentes y diga cuál es el mayor de los tres.
while True:
    try:
        print ("Ingresa el primer numero: ")
        p = float (input ())
        break
    except ValueError:
        print ("no es un numero")
while True:
    try:
        print ("Ingresa el segundo numero: ")
        s = float (input ())
        break
    except ValueError:
        print ("no es un numero")
while True:
    try:
        print ("Ingresa el tercer numero: ")
        t = float (input ())
        break
    except ValueError:
        print ("no es un numero")
        
if p > s and p > t :
    print ("el numero mayor es: ", p)
elif s > p and s > t :
    print ("el numero mayor es: ", s)
else :
    print ("el numero mayor es: ", t)