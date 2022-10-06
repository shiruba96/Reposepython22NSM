#distancia euclidea entre dos puntos (x1, y1) y (x2, y2)

import math
print ("Ingrese el valor de x1")
x1 = float (input ())
print ("Ingrese el valor de y1")
y1 = float (input ())
print ("Ingrese el valor de x2")
x2 = float (input ())
print ("Ingrese el valor de y2")
y2 = float (input ())
#Calcular distancia
x = (x2 - x1) ** 2
y = (y2 - y1) ** 2
d = math.sqrt (x + y)
print ("la distancia es ", d)

