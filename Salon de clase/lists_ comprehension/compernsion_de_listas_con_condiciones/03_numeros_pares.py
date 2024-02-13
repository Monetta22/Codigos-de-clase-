lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_pares = [valor for valor in lista if (valor % 2 == 0)]
print(lista_pares)

lista_impares = [valor for valor in lista if (valor % 2 != 0)]
print(lista_impares)
