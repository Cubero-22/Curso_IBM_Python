#Permite crear listas a partir de unos valores que tenemos almacenados.
#Es una expresión con una notación particular que genera una lista.
mi_lista = [1,2,3,4,5,6,7]

mi_lista2 = [2*elemento for elemento in mi_lista]
#Mientras las listas de compresión devuelven son otra lista a partir de una primera
#Hacemos operaciones con los valores de la lista original.
print(mi_lista2)

listas_pares = [elemento for elemento in mi_lista if elemento%2 == 0]
print(f"Los numeros pares de la lista son: {listas_pares}")
for l in listas_pares:
    print(f"Números par: {l}")

for l in mi_lista:
    print(l * 2)
