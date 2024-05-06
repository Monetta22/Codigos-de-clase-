from datetime import datetime

# modificaciones al codigo

# IMPLEMENTACION AL PRIMER APELLIDO
""" # primer apellido
while True:
    primer_apellido = input("\nIntroduzca el primer apellido: ").upper()

    if primer_apellido == "":
        print("\n\tNo puedes omitir este valor. Intenta de nuevo.")
    elif not primer_apellido.isalpha():
        print(
            "\n\tDebes ingresar el nombre en texto y sin espacios vacios. Inteta de nuevo."
        )
    else:
        print("\n\tSe registro satisfactoriamente.")
        break """

# IMPLEMENTACION AL NOMBRE
""" # prueba de registro del nombre sin omitir valor y no acepta valores enteros
while True:
    nombre = input("\nEscribe el nombre: ").upper()

    if nombre == "":
        print("\n\tNo puedes omitir este valor. Intenta de nuevo.")
    elif not nombre.isalpha():
        print(
            "\n\tDebes ingresar el nombre en texto y sin espacios vacios. Inteta de nuevo."
        )
    else:
        print("\n\tSe registro satisfactoriamente.")
        break

 """

# IMPLEMENTACION A EL SEGUNDO APELLIDO
""" # proceso
# segundo apellido se puede omtir
# verificando que no sean numeros
while True:
    segundo_apellido = input("\nIntroduzca el segundo apellido: ").upper()
    if not segundo_apellido == "":
        if not segundo_apellido.isalpha():
            print(
                "\n\tDebes ingresar el nombre en texto y sin espacios vacios. Inteta de nuevo."
            )
        else:
            print("\n\tSe registro satisfactoriamente.")
            break
    else:
        print("\n\tSe registro satisfactoriamente.")
        break
 """

# IMPLEMENTANDO CODIGO
from datetime import datetime

while True:
    fecha_naci = input("\nEscriba la fecha de nacimiento del paciente (mm/dd/aaaa): ")
    try:
        if fecha_naci == "":
            print(
                "\n\tDebes ingresar la fecha de nacimiento del paciente. Intenta de nuevo."
            )
            continue
    except:
        print(
            "\n\tDebes ingresar la fecha de nacimiento del paciente. Intenta de nuevo."
        )
    try:
        if fecha_naci:
            fecha_naci = datetime.strptime(fecha_naci, "%m/%d/%Y").date()
    except:
        print("\n\tDebes ingresar un formato que sea valido. Intenta de nuevo.")
        continue
    dia_hoy = datetime.now().date()
    if fecha_naci < dia_hoy:
        print("\n\tRegistro existoso.")
        break
    else:
        print("\n\tIntoduce una fecha valida. Intenta de nuevo.")
        continue


""" 
while True:
    nombre = (
        input("\nIntroduzca el nombre: ").strip().upper()
    )  # Eliminar espacios en blanco al inicio y al final
    if nombre == "":
        print("\nNo puedes omitir este valor. Intenta de nuevo.")
    # esta validacion elimina los espacios en blanco y comprueba si los valores son alfanumericos. Regresa true
    # si "no" cunple despues de eliminar espacios y comprobar si son alfanumericos.
    # se agrega esta validacion por que isalpha() no acepta espacios en blanco
    elif not nombre.replace(" ", "").isalpha():  # reemplaza espacios en blanco
        print(
            "\nDebes ingresar el nombre en texto sin números ni caracteres especiales. Intenta de nuevo."
        )
    else:
        print("\nSe registró satisfactoriamente")
        break

 """
