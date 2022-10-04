#Elaborar un programa que solicite al usuario como dato de entrada una calificación y muestre una leyenda
# 10 Excelente, 9 Muy bien, 8 Bien, 7 Regular, 6 Mal, 5 a 0 Muy mal

print ("Ingrese tu calificacion: ")
cal = float (input ())
if cal <= 5:
    message = "Muy mal"
    print (message)
elif cal == 6:
    message = "Mal"
    print (message)
elif cal == 7:
    message = "Regular"
    print (message)
elif cal == 8:
    message = "Bien"
    print (message)
elif cal == 9:
    message = "Muy bien"
    print (message)
else :
    message = "Excelente"
    print (message)


