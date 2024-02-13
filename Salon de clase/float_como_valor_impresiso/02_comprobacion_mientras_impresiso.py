# CLASE FLOATS CON IMPRESISOS DE NETURALEZA DE
import math

contador = 0.1

while True:
    print(contador)
    if math.isclose(contador, 1.0):
        break
    contador = contador + 0.1
