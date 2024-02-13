diccionario = {1: "Value 1", 2: "Value 2", 3: "Value 3"}


# desempaqueta las llaves
a, b, c = diccionario
print(a)
print(b)
print(c)

# desempaqueta los valores
a, b, c = diccionario.values()
print(a)
print(b)
print(c)

# asigna una tupla formada por la pareja llave y valor de cada elemento
a, b, c = diccionario.items()
print(a)
print(b)
print(c)
