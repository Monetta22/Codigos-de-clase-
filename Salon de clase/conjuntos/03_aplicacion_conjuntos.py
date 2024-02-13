import random

# comprension de listas con for
valores = [random.randrange(1, 6) for valor in range(100)]

print(valores)

# identificamos los valores unicos con set
diferentes = set(valores)
print(diferentes)
