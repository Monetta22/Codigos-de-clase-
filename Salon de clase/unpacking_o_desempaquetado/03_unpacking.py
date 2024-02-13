# programa 1
# la lista tiene 3 elementos que son 3 tuplas
paciente = [(10, "Juan", 170), (20, "Fulano", 120), (30, "Mengano", 200)]

print(len(paciente))

for clave, nombre, estatura in paciente:
    print(f"Socio {clave} de nombre {nombre} con estatura de {estatura} cm.")


# programa 2
encabezado = "Clave\tNombre\tEstatura"
print(encabezado)
print("*" * (len(encabezado) + 10))


for clave, nombre, estatura in paciente:
    print(f"{clave:^5} {nombre:<8} {estatura:^8}")
# aprender acerca de reportes tabulares
