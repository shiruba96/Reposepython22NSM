#Elaborar un programa que permita leer el tamaño de los tres ángulos de un triángulo e imprima qué tipo
#de triángulo es.

print ("Ingresa el Angulo A del triangulo: ")
aa = float (input ())
print ("Ingresa el Angulo B del triangulo: ")
ab = float (input ())
print ("Ingresa el Angulo C del triangulo: ")
ac = float (input ())
if aa == 90 or ab ==90 or ac == 90:
    message = "es un triangulo rectangulo"
    print (message)
elif aa < 180 and aa > 90 or ab < 180 and ab > 90 or ac < 180 and ac > 90  :
    message = "es un triangulo obtusángulo"
    print (message)
else :
    message = "es un triangulo Acutángulo"
    print (message)