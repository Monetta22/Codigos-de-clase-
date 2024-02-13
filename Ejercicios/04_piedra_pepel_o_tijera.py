import random

print('Bienvenido a este juego "PIEDRA, PAPEL O TIJERA"')
print("=====MENU DE OPCIONES====\n1.Piedra \n2.Papel \n3.Tijera")

# inicializacion de variables
seleccion_usuario = int(input("Selecciona una opcion: "))
opcion_usuario = 0
opcion_menu = True

# leyendo opcion de usuario y pasarla a la variable "opcion_elegida"
if seleccion_usuario == 1:
    opcion_usuario = "Piedra"

elif seleccion_usuario == 2:
    opcion_usuario = "Papel"

elif seleccion_usuario == 3:
    opcion_usuario = "Tijera"

else:
    print("Opcion invalida")
    opcion_menu = False
    opcion_usuario = "INVALID_ERROR"

print(f'El usuario eligio: "{opcion_usuario}"')

# eligiendo en automatico el rol de la computadora
tupla_opciones_pc = ["Piedra", "Papel", "Tijera"]

seleccion_pc = random.choice(tupla_opciones_pc)

print(f'La computadora eligio: "{seleccion_pc}"')


while opcion_menu == True:
    if opcion_usuario == seleccion_pc:
        print(
            f'EMPATE. Por que el usuario escogio "{opcion_usuario}" y la cumputadora escogio "{seleccion_pc}"'
        )
    elif opcion_usuario == "Piedra" and seleccion_pc == "Tijera":
        print(
            f'GANO USUARIO. Por que el usuario escogio "{opcion_usuario}" y la cumputadora escogio "{seleccion_pc}"'
        )
    elif opcion_usuario == "Tijera" and seleccion_pc == "Papel":
        print(
            f'GANO USUARIO. Por que el usuario escogio "{opcion_usuario}" y la cumputadora escogio "{seleccion_pc}"'
        )
    elif opcion_usuario == "Papel" and seleccion_pc == "Piedra":
        print(
            f'GANO USUARIO. Por que el usuario escogio "{opcion_usuario}" y la cumputadora escogio "{seleccion_pc}"'
        )
    else:
        print(
            f'PERDISTE. Por que el usuario escogio "{opcion_usuario}" y la cumputadora escogio "{seleccion_pc}"'
        )
    break
