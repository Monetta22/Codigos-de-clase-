lista = [2, "perro", 4, "gato", 6, "Buo", 8, "elefante", 10]
print(lista)

lista_numeros = [valor for valor in lista if isinstance(valor, int)]
print(lista_numeros)

lista_palabras = [valor for valor in lista if isinstance(valor, str)]
print(lista_palabras)
