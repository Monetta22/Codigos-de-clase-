dato = input("Dame tu edad actual, introduce unicamente enteros: ")

if dato.isdigit():  # .isdigit() "comprueba si tiene digitos"
    edad = int(dato)
    print(f"El doble de tu edad es: {edad * 2}")
else:
    print("Intodujiste tipo de dato string")
