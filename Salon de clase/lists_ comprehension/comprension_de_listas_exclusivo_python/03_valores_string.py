# SIN conprension de listas
datos = ["a", "b", "c", "d"]
dato_mayusculas = []

for dato in datos:
    dato_mayusculas.append(dato.upper())

print(dato_mayusculas)


# utilizando comprension de listas
datos1 = ["a", "b", "c", "d"]
dato_mayusculas1 = [dato.upper() for dato in datos]
print(dato_mayusculas1)


# comprension de tuplas "NO ES POSIBLE"
datos_tupla = ("a", "b", "c", "d")
# por que poner el tipo de tupla() si al imprimir el tipo de dato es tupla
dato_mayuculas_tupla = (dato.upper() for dato in datos_tupla)
print(dato_mayuculas_tupla)  # error

print(type(datos_tupla))

# comprension de lista
lista = ["a", "b", "c", "d"]
mayuscula = [letra.upper() for letra in lista]
print(f"La lista en mayusculas es: {mayuscula}")

# CORREGIDO
# se tiene que hacer un CAST a tupla
datos_tupla = ("a", "b", "c", "d")

dato_mayuculas_tupla = tuple(dato.upper() for dato in datos_tupla)

print(dato_mayuculas_tupla)

print(type(datos_tupla))
