#programa para abrir el archivo romeo.txt y leerlo línea por línea. Para cada línea, dividir la línea en
#una lista de palabras utilizando la función split. Para cada palabra, revisar si la palabra ya se encuentra
#previamente en la lista. Si la palabra no está en la lista, agregarla a la lista. Cuando el programa termine, ordenar
#e imprimir las palabras resultantes en orden alfabético.

lista = []
i=0
def busca (elem):
    for palabra in lista:
        while(lista.count(palabra) > 1):
            lista.remove(palabra)

with open("EjerciciosTupplas/romeo.txt") as doc:
    for lineas in doc:
        elem = lista.extend(lineas.split())
    print ("lista original: ", lista)
    busca(elem)
print ("lista sin repeticiones: ", lista)
