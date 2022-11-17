#insertar elemntos de una lista y mostrara el estado de la estructura en orden
tamaño = int(input("cuantos elementos desea en la lista"))
lista = []
def Insertar (t, list):
    cont = 0
    while (cont<t):
        elemento=input("Dame el elemento a insertar")
        list.append(elemento)
        cont+=1
def mostrar (lst):
    print (lst)
    #for i in range (0, len(lista)-1):
def burbuja (lst):
    for i in range (0, len(lst)-1):
        for j in range (0,len(lst)-1):
            if lst([j]>lst[j+1]):
                lst[j],lst[j+1]=list[j+1],lis[j]   
    
Insertar (tamaño, lista)
mostrar  (lista)
burbuja (lista)
mostrar (lista)
        