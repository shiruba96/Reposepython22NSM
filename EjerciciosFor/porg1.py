#Elabore un programa que dada una cadena de texto, indique el número de vocales que tiene

cadena = input("Ingresa una cadena: ")
cont = 0
letras = ['a','e','i','o','u']
for letra in cadena:
    if letra.lower() in letras:
        cont += 1
print ("la cadena %s" % cadena + " tienen %d " % cont + "letras vocales")