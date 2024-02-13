# Un conjunto o set en Python se refiere a una secuencia de valores únicos dentro de dicha estructura.
# los elementos a almacenar dentro de un set deben ser valores inmutables.

# Los conjuntos son estructuras muy útiles mediante las cuales podemos aplicar las operaciones clásicas de lógica de conjuntos, tales como:

# UNIÓN
# INTERSECCIÓN
# DIFERENCIA
# DIFERENCIA SIMÉTRICA

# no se muestra el str                                        [      ]
conjunto_prueba = {"Miguel", "Alejandro", "Angel", "Nicolas"}

print(conjunto_prueba)

conjunto_1 = {"Juan", "Carlos", "Jaso"}
conjunto_2 = {"Luis", "Marco", "Jaso"}

print("UNION")
print(conjunto_1 | conjunto_2)

print("INTERSECCION")
print(conjunto_1 & conjunto_2)

print("DIFERENCIA")
print(conjunto_1 - conjunto_2)

print("DIFERENCIA SIMËTRICA")
print(conjunto_1 ^ conjunto_2)
