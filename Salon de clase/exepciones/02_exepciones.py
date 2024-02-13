import sys

lista_con_valores = ["x", 0, 5]

for valor in lista_con_valores:
    try:
        print(f"Valor en turno: {valor}")
        reciproco = 1 / int(valor)
        print(f"El reciproco es: {reciproco}")
    except:
        print(f"El problema que ocurre: {sys.exc_info()[0]}")
        print("Seguimos con el siguiente valor")
