#segunda ley de Newton (F=ma -Fuerza =masa por aceleración), 
# elaborar un programa que pregunte si se desea calcular la fuerza, masa o aceleración y 
# según la opción seleccionada lea los datos correspondientes y muestre los resultados.

print ("seleccione alguna de las siguientes opciones: ")
print ("calular fuerza = 1 ")
print ("calcular masa = 2 ")
print ("calular aceleracion = 3")
op = float (input ())
if op == 1 :
    print ("Ingrese el valor de la masa")
    m = float (input ())
    print ("Ingrese el valor de la aceleracion")
    a = float (input ())
    f = m * a
    print ("la fuerza calulada es: ", f)
elif op == 2 :
    print ("Ingrese el valor de la fuerza")
    f = float (input ())
    print ("Ingrese el valor de la aceleracion")
    a = float (input ())
    m = f / a
    print ("la masa calulada es: ", m)
elif op == 3:
    print ("Ingrese el valor de la masa")
    m = float (input ())
    print ("Ingrese el valor de la fuerza")
    f = float (input ())
    a = f / m
    print ("la aceleracion es: ", a)