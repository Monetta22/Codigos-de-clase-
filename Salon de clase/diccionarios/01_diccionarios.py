# claves deben ser inmutables y no se pueden repetir
# "clave" y "valor"
# en python los diccionarios ordenan los valores mediatnte HASH TABLE

diccionario = {20: "Manzana", 40: "Gato", 60: "Dinero"}

# para acceder a un valor se accede siempre atravez del valor de la llave
print(diccionario[20])

# accediendo a las claves
print(diccionario.keys())

# accediendo a los valores
print(diccionario.values())

# no es la forma eficiente de buscar claves
if 25 in diccionario.keys():
    print(diccionario[25])
else:
    print("No existe esa clave")

# la manera correcta de bucar claves con la funcion get()
#                    [  ] clave
#   [ ] clave             [          ] else
print(diccionario.get(40, "NO EXISTE"))

# para crear un diciconario vacio
diccionario = dict()
print(type(diccionario))
print(diccionario)

# crear claves
# datos [8] = "Domitila"
