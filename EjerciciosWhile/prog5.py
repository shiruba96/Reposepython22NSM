#Elabore un programa que imprima las tablas de multiplicar del 1 a un número dado

print ("La tabla de que numero deseas mostrar ?")
num = int (input ())
print ("Hasta que numero vamos a multiplicar ?")
mult = int (input ())
cont = 1
while cont <= mult:
    x = num * cont
    print (num,"x",cont,"=",x)
    cont +=1
