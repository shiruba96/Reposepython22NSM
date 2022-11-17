lista = []
i=0
j=0

def busca(elem):
    print (elem)
    print (lista)
    for palabra in lista:
      i += 1
      palabra1 = lista [i]
      j =+ i
      print (i)
      print (lista[i])
      print (lista[j])
      palabra2 = lista[j]
      if palabra2 == palabra1:
        print ("si esta ", palabra1, palabra2)
        del lista[j]
        j =+ i
      else:
        j =+ i
        return busca


with open("EjerciciosTupplas/romeo.txt") as doc:
    for lineas in doc:
        elem = lista.extend(lineas.split())
        #print (lista)
        busca (elem)
    