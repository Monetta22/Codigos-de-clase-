# codifique un programa que le solicite al usuario valores numericos enteros, el programa debera mantener el registro de todos aquellos valores proporcionados por el usuario al final de la captura de dichos valores informe mediante un listado aquellos que fueron mayores o iguales a 100 pero menores o iguales a 150. Considere que no hay una contidad fija de valores a proporcionar por el usuario.print

# Bienvendia
print(
    "Te doy la bienvenida a este programa te dare un informe de valores mayores o iguales a 100 pero menores o iguales a 150"
)
print('Para indicar que quieres salir escribe la palabra: "salir"')

numeros = []

while True:
    dato = input("Dame numeros enteros: ~$")
    if dato.lower() == "salir":
        break
    else:
        numeros.append(int(dato))
        numeros = [dato for dato in numeros if dato >= 100 and dato <= 150]

if numeros:
    print(numeros)
else:
    print("No se introdujeron datos")


# x >= 10 and x <= 20
# 10 <= x <=20
# es lo mismo para asignar un rango de valores
