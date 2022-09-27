import math
cateto_a = 0.0
cateto_o = 0.0
print ("dame la longiud de la hipotenusa")
h= float (input ())
print ("dame el cateto adyacente")
cateto_a = float (input())
x = cateto_a /h
cateto_o=math.sin(math.acos(x))*h
print ("el cateto opuesto es:", cateto_o)