#RANGO DE ÍNDICES NEGATIVOS
frutas = ["manzana","pera","naranja","limon"]
resultado = frutas[-4:-1]
print(resultado)#RESULTADO SERÍA ['manzana','pera','naranja']

#PALABRA RESERVADA IN PARA SABER SI UN ELEMENTO ESTA O NO EN UNA LIST
if "pera" in frutas:
    print("pera si está en la lista")

if "platano" not in frutas:
    print("platano no está en la lista")

#COPIAR UNA LISTA.
frutas2 = frutas#Cuidado!, estamos copiando por referencia.
#Los cambios que realicemos en frutas2 también se harán en frutas
print(frutas2)
frutas[0] = "platano"
print(frutas2)
print(frutas)#Cambian amnbas, y el primer elemento ahora es platano para las 2 listas

'''Utilizaremos 2 maneras para hacer copias de listas'''
frutas2 = frutas.copy()#Método copi() de las listas
frutas3 = list(frutas)#Método list incorporado.

#UNIR 2 LISTAS
#1.Utilizando el operador +
lista1 = [1,3,3,4]
lista2 = [5,6,7,8]
lista_unica = lista1 + lista2
print(lista_unica)
#2.Agregando todos los elementos de lista2 a lista1, uno por uno
for item in lista2:
    lista1.append(item)

print(lista1)
#3.Utilizando el método extend()
lista1.extend(lista2)
print(lista1)

#EL CONSTRUCTOR list()
lista = list(("manzana","pera","melon"))
for l in lista:
    print(l)