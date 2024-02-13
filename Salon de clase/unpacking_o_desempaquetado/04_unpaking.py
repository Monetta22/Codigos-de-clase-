# unpacking rompiendo la regla de para cada identificador tiene que haber el mismo numero de valores.

# cuando se utiliza el * todos los demas datos se guardan en una lista y solo se puede usar soamelnte un * del unpacking

datos = (2, 8, 10, 19)

# a, *b = datos
# a, *b, c = datos
*a, b, c = datos

print(a)
print(b)
print(c)
