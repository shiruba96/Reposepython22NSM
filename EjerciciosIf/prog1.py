# calcular el sueldo de un empleado con base a las horas trabajadas y se le otorga un
# incentivo del 5% si trabajó más de 40 horas.

print ("Ingrese la paga por hora: ")
ph = float (input ())
print ("Ingrese las horas trabajada a la semana")
hs = float (input ())
if hs <= 40:
    salario = ph * hs
    print ("el salario a pagar es: ", salario)
else :
    salario = ph * hs
    extra = (salario * 5)/100
    salario = salario + extra
    print ("el salario a pagar es: ", salario)