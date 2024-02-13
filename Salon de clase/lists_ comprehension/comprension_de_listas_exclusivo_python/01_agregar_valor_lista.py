lista = [2, 4, 6, 8, 10]
print(lista)

lista_resultado1 = []
for valor in lista:
    lista_resultado1.append(valor)
print(lista_resultado1)

lista_resultado2 = [valor * 2 for valor in lista]
print(lista_resultado2)
