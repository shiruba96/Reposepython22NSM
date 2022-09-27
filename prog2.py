#calcular e imprimir el precio de venta de un artículo que se calcula añadiéndole al costo 
# de producción el 120% de utilidad y el 16% de impuesto.
#
print ("Ingrese el costo de porduccion del articulo")
a = float (input ())
# calcular utilidad
u = (a * 120) / 100
#calcular impuesto
i = (a * 16) / 100
p = a + u + i
print ("el precio de venta es: ", p, "$")