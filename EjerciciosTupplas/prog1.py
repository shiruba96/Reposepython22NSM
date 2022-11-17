#Escribe una función llamada recortar que toma una lista y la modifica, removiendo el primer y último
#elemento. Después escribe una función llamada medio que toma una lista y regresa una nueva lista que contiene
#todo excepto el elemento o elementos de la mitad.

import math
lista = []
tamaño = int (input ("cuantos elementos quieres en la lista?"))

def Insertar (t, lst):
    cont = 0
    while (cont <t ):
        elem=input ("Ingresa el elemento ")
        lst.append(elem)
        cont +=1
        
def Mostrar (lst):
    print (lst)
    
def Recortar (lst):
    print ("sin primero y ultimo")
    lst.pop(0)
    lst.pop()
    
def Medios (lst):
    print ("sin medios")
    l=len(lst)
    if (1 % 2 == 0):
        sup = int(1/2)
        inf=sup-1
        del lst [inf:sup+1]
       # lst.pop [l-1:l]
    else: 
        sup = math.floor (l/2)
        del lst[sup]
    listaN=lst
    return listaN
        
Insertar (tamaño, lista)
Mostrar (lista)
Recortar (lista)
Mostrar (lista)
ListaN = Medios(lista)
Mostrar (lista)