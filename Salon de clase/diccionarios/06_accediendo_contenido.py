# keys() - Retorna las claves del diccionario, sin sus valores asociados.
# values() - Retorna los valores del diccionario, sin sus claves asociadas.
# items() - Retorna un conjunto de tuplas, una por cada elemento del diccionario e invariablemente dicha tupla estará apegada a la siguiente descripción: (clave, valor)


diccionario = {1: "Value 1", 2: "Value 2", 3: "Value 3"}

# contenido de las llaves
print(list(diccionario.keys()))

# contenido de los valores
print(list(diccionario.values()))

# contenido de los items
print(list(diccionario.items()))
