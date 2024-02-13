# codifique un programa que solicite a usuario una cantidad indeterminada de nombres de empleados, a cada nombre se le debe de asignar una clave de manera automatica por parte del programa una clave unica. Defina usted la manera en que el usuario le indicara que a concluido la captura. Debera almacenar el conjunto de datos en un diccionario. Depliegue el diccionario resultante al final.


# generar llave de manera automatica

diccionario = dict()

numero_clave = 0


print('\t\t\t\tBIENVENIDO. \nPara salir escribe la palabra "salir"\n')

while True:
    dato = input("Ingrese el nombre del empleado: $")
    if dato.lower() == "salir":
        break
    else:
        if dato:
            diccionario[numero_clave] = dato
            numero_clave += 1

print(diccionario)

# investigar sobre "if ternarios"
