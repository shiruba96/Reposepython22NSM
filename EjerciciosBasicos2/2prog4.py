# futuro valor de una cantidad de dinero, a partir del capital iniciall, 
# tipo de interes y el numero de años

print ("Ingrese el capital inicial")
ci = float (input ())
print ("Ingrese el tipo de interes que se manejar")
i = float (input ())
print ("Ingrese la cantidad de años a calcular")
a = int (input ())
vf = ci * pow ((1 + i/100), a)


print ("el total es ", vf)