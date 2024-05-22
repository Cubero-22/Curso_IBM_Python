#COLECCIONES DE DATOS MODIFICABLES, DESORDENADOS, NO ADMITEN VALORES DUPLICADOS
#LAS CLAVES SON INMUTABLES.

dic = {"nombre":"Antonio", "edad":23, "profesion": "arquitecto","nombre":"Antonio"}
print(dic)
#Los sets tampoco admiten valores duplicados, simplemente no lo imprimen.
set = {1,3,3,3,2,8}
print(set)
#Otro dic:
dic2 = {"nombre":"Marcos","edad":33,"profesin":"futbolista"}

print(dic is dic2)
print(dic == dic2)

#print(dic + dic2) , no es posible esta operación
#Podemos quitar valores de un diccionario.
dic.pop("edad")
print(dic)
#Métdos keys() and values()
for clave,valor in dic.items():
    
    print(f"Tu {clave} es {valor}")
for clave in dic.keys():
    print(clave)
for valor in dic.values():
    print(valor)
#OBJETO ZIP QUE CONVERTIREMOS EN UNALISTA con 2 tuplas
dic_keys = ["nombre","edad"]
dic_values = ["Fede",25]
diccionario = dict(zip(dic_keys,dic_values))
lista = dict(zip(dic_keys,dic_values))
print(diccionario)
#Añadiendo campos a un diccionario vacío.
dict = {}
dict["pais"] = "españa"
dict["poblacion"] = 47
dict["lenguas"] = {"cataluña":"catalan", "euskadi":"euskera", "Galicia":"gallego"}
print(dict)
print(f"En Cataluña se hable el {dict["lenguas"]["cataluña"]}")