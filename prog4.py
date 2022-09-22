# calcular el volumen de un cilindro.

print ("Ingrese el valor del radio del cilindro")
r = float (input ())
print ("Ingrese el valor de la altura")
a = float (input ())
#formula para calcular el area de la base
ab = 3.1416 * (r * r)
#formula para obtener el volumen
v = ab * a  
print ("el volumen es del cilindro es", v)
