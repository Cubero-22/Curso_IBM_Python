#COLECCIONES DESORDENADAS, NO INDEXADAS, NO PERMITEN VALORES DUPLICADOS, MODIFICABLES.
frutas = {"platano","manzana","pera","melon"}
print(frutas)
for fruta in frutas:
    print(fruta)
#en el out salen de manera desordenada. cambiando en cada ejecución del script.

#MÉTDO ADD() , SIMILAR A APPEND() EN LAS LISTAS
frutas.add("sandia")
print(frutas)
#MÉTODO UPATE() PARA AÑADIR VARIOS ELEMENTOS O INSETAR UN CONJUNTO EN OTRO
frutas.update({"piña","ciruela"})
print(frutas)
frutas4 = {"mango","cereza"}
frutas.update(frutas4)
print(f"Hemos utilizado el método update() para insertar un conjunto en otro: {frutas}")

#No existen los valores duplicados, como en los diccionarios
#Si unimos 2 sets con valores iguales, solo aparecerá uno de los valores
frutas2 = {"limon","naranja","ciruela","platano"}
frutas3 = frutas | frutas2#Unión con símbolo |
print(frutas3)
#UNIÓN CON MÉTODO UNION()
union_frutas = frutas.union(frutas2)
print(f"Unimos dos sets utilizando el método union(): {union_frutas}")

#Intersección de sets o conjuntos.
interseccion = frutas & frutas2
print(interseccion)#Imprime los elementos comunes

#Diferencia para mostrar los no duplicados para 2 conjuntos.
diferencia = frutas - frutas2
print(diferencia)

#Castear un string para elimninar duplicados de una forma rápida y sencilla
string = 'aabbbffxxxhhhh'
print(set(string))#imprime los elementos SIN DUPLICAR
#Podríamos ordenar el set.
print(sorted(set(string)))#Devuelve una lista

#TEST DE MEMBRESÍA.
print('th' in 'python')

#Comprobar que un elemento está en el set
print("manzana" in frutas)
#Comprobar que un elemento está en dos sets
print("platano" in frutas & frutas2)
#Comprobar que un elemento está en alguno de los conjuntos
boolean = "tomate" in (frutas | frutas2)
print(boolean)

#Eliminar un elemento del set
frutas.remove("manzana")#O discard(), que si no existe un elemento no genera un error
print(frutas)

#Método pop(), al ser una colección desordenada, no sabemos que elemento eliminará.
fruta_almacenada = frutas.pop()
print(fruta_almacenada)

#Método clear(), que vacía el set.
frutas.clear()
print(frutas)
print(type(frutas))

#Palabra clave del , que borra totalmente el conjunto
del frutas
print(frutas)#Nos da error tipo nameerror