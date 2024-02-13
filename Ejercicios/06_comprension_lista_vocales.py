# considerando una lista que contenga un conjunto de caracteres de texto resualva mediante comprension de listas que pasen a una segunda lista solamente aquellas letras que sean vocales.

lista_palabras = ["a", "e", "i", "o", "u", "z", "y", "t", "f", "p", "r"]

lista_vocales = [letra for letra in lista_palabras if letra in ("aeiou")]

print(lista_vocales)

# compresnsion de lista defalut
mensaje = "Hola Mundo"
vocales = [letra for letra in mensaje if letra in ("aeiou")]
print(vocales)

# convierte el mensaje a minisculas
mensaje = "HolA Mundo"
vocales = [letra for letra in mensaje.lower() if letra.lower() in ("aeiou")]
print(vocales)

#
mensaje = "Hola Mundo"
vocales = [letra for letra in mensaje if letra in ("aeiou")]
# se convierte en True si vocales contiene uno o mas elementos
if vocales:
    print(vocales)
else:
    print("No se encontraron vocales")

# la otra forma de hacerlo es
# if len(vocales):
#    print(vocales)
# else:
#   print("No se encontraron vocales")
