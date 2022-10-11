#Elabore un programa que lea n números enteros y determine cuántos de ellos son impares y cuál es su sumatoria.

print ("Hasta que numero vamos a analizar ?")
ni = int (input ())
cont = ni
cont2=0
x = 0
suma = 0
while cont != 0:
  x = cont % 2
  if x == 1:
    suma = cont + suma
    print (cont) #imrime los numeros impares
    cont2 += 1
  cont -=1
print ("la cantidad de numeros impares encontrados fue",cont2)
print ("la sumatoria de los numeros impares es",suma)