import math

lista = []
tamaño = int (input ("cuantos elementos quieres en la lista"))

def Insertar (t, lst):
    cont = 0
    while (cont <t ):
        elem=input ("dame el elemento")
        lst.append(elem)
        cont +=1
        
def Mostrar (lst):
    print (lst)
    
def Recortar (lst):
    lst.pop(0)
    lst.pop()
    
def Medios (lst):
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
ListaN=Medios(lista)
Mostrar (lista)