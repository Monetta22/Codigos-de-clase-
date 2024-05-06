import random
from datetime import datetime, timedelta

contador_clave = 1
contador_folio = 0
contador_cita_realizada = 0
registro_paciente = dict()
folio_cita = dict()
cita_realizada = dict()

# contador para saber en que ciclo estamos
numero_ciclo = 1
while True:
    print(f"\n********************Ciclo {numero_ciclo}********************")
    numero_ciclo += 1
    print("Acciones que se pueden realizar")
    print("\n=======MENU PRINCIPAL=======")
    print(
        "1.- Registro de pacientes.",
        "\n2.- Programacion de citas.",
        "\n3.- Realizacion de citas programadas.",
        "\n4.- Consultas y reportes.",
        "\n5.- Salir del sistema.",
    )
    try:
        eleccion_pacientes = int(input("\nSeleccione la opcion deseada: "))
    except Exception:
        print("\n\tEl texto debe ser entero. Intente de nuevo")
        continue
    if eleccion_pacientes == 1:

        # LISTO
        # primer apellido
        # not isaplha si no es texto manda error
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
                break

        # LISTO
        # segundo apellido se puede omtir
        # verificando que no sean numeros
        # funcion alpha no acepta espacios
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

        # LISTO
        # registro del nombre del paciente
        # funcion alpha no acepta espacios
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

        # LISTO
        # IMPLEMENTACION
        # FECHA
        while True:
            fecha_nacimiento = input(
                "\nEscriba la fecha de nacimiento del paciente (mm/dd/aaaa): "
            )
            try:
                if fecha_nacimiento == "":
                    print(
                        "\n\tDebes ingresar la fecha de nacimiento del paciente. Intenta de nuevo."
                    )
                    continue
            except:
                print(
                    "\n\tDebes ingresar la fecha de nacimiento del paciente. Intenta de nuevo."
                )
            try:
                if fecha_nacimiento:
                    fecha_nacimiento = datetime.strptime(
                        fecha_nacimiento, "%m/%d/%Y"
                    ).date()
            except:
                print("\n\tDebes ingresar un formato que sea valido. Intenta de nuevo.")
                continue
            dia_hoy = datetime.now().date()
            if fecha_nacimiento < dia_hoy:
                print("\n\tRegistro existoso.")
                break
            else:
                print("\n\tIntoduce una fecha valida. Intenta de nuevo.")
                continue

        registro_paciente[contador_clave] = [
            primer_apellido,
            segundo_apellido,
            nombre,
            fecha_nacimiento.strftime("%m/%d/%Y"),
        ]
        contador_clave += 1

        print(f"\n{registro_paciente}")
        print("\n\tPaciente registrado con exito.")

    elif eleccion_pacientes == 2:
        if contador_clave == 0:
            print("\n\tDebe haber un paciente registrado")
            continue
        while True:
            try:
                clave_paciente = int(input("\nIntroduzca la clave del paciente: "))
            except:
                print("\n\tLa clave de ser el formato deseado. Intente de nuevo")
                continue
            if clave_paciente in registro_paciente:
                break
            else:
                print("\n\tEl paciente no está registrado. Intente de nuevo.")
                continue
        # fecha de la cita
        while True:
            try:
                fecha_cita_str = input(
                    "\nIntroduzca la fecha de la cita (Valor de fecha en el formato mm/dd/aaaa): "
                )
                fecha_cita = datetime.strptime(fecha_cita_str, "%m/%d/%Y")
                # Condicion
                if fecha_cita <= datetime.now() + timedelta(days=60):
                    break
                else:
                    print(
                        "\n\tLa fecha de la cita no puede ser mayor a 60 días después de hoy. Intente de nuevo."
                    )
                    continue
            except:
                print("\n\tLa fecha debe llevar el formato indicado. Intente de nuevo.")
                continue
        # folio es un contador, la clave la agrego con clave que introdujo usuario al principio
        while True:
            try:
                turno_cita = int(
                    input(
                        "\nIntroduzca el turno del paciente 1.- mañana, 2.- mediodia, 3.- tarde"
                    )
                )
                if turno_cita <= 4:
                    break
                else:
                    print(
                        "\n\tEl turno debe de ser solo los proporcionados. Intente de nuevo"
                    )
                    continue
            except:
                print("\n\tEl valor debe ser numerico, Intente de nuevo")
                continue
        contador_folio = contador_folio + 1
        if clave_paciente in registro_paciente:
            folio_cita[contador_folio] = [
                clave_paciente,
                fecha_cita.strftime("%m/%d/%Y"),
                turno_cita,
            ]
            print("\nLa cita ya está programada")
            print(folio_cita)

    elif eleccion_pacientes == 3:
        # compruebo si el folio existe y si existe a la variable registro_clave le doy el valor de la clave que está registrada en ese folio
        while True:
            try:
                confirmacion_folio_cita = int(
                    input("\nIntroduzca el folio de su cita: ")
                )
                if confirmacion_folio_cita in folio_cita:
                    registro_clave = folio_cita[contador_folio][0]
                    # no me deja usar datetime.today
                    hora_llegada_paciente = hora_actual = datetime.now().time()
                    print(registro_clave)
                    break
                else:
                    print(
                        "\n\tEl folio no coincide. La cita no esta registrada. Intente de nuevo."
                    )
                    continue
            except:
                print("\n\tEl dato debe ser numerico. Intente de nuevo.")
                continue
            # peso del paciente con try porque convierte a float(todavia no funciona del todo)
        while True:
            try:
                peso_paciente = float(input("\nIntroduzca el peso del paciente: "))
                break
            except:
                print("\n\tEl peso debe de tener el formato correcto. Intente de nuevo")
                continue
            # altura paciente que convierte a float (todavia no funciona del todo)
        while True:
            try:
                altura_paciente = float(input("\nIntroduzca la altura del paciente: "))
                break
            except:
                print("\n\tLa altura debe tener el formato correcto. Intente de nuevo")
                continue
        # de alguna manera introducir la clave para que en el reporte tabular se imprima el peso y la altura
        cita_realizada[contador_cita_realizada] = [
            hora_llegada_paciente,
            peso_paciente,
            altura_paciente,
            "\nLa cita se realizó",
        ]
        print(cita_realizada)

    elif eleccion_pacientes == 4:
        if contador_clave == 0:
            print("\n\tDebe de haber un paciente registrado. Intente de nuevo")
            continue
        elif contador_folio == 0:
            print("\n\tDebe de haber un folio de cita. Intente de nuevo")
            continue

        while True:
            try:
                eleccion_consulta_o_reporte = int(
                    input(
                        "\nPara los reportes tenemos dos opciones. 1.- Reporte por citas 2.- Reporte por pacientes. 3.- Si deseas salir"
                    )
                )
                break
            except:
                print("\n\tEl dato debe ser numerico. Intente de nuevo")
                continue
        # Reporte por citas
        if eleccion_consulta_o_reporte == 1:
            print("\nSi")
        # Reporte por pacientes
        elif eleccion_consulta_o_reporte == 2:
            while True:
                print("\n1. Lista de los pacientes registrados")
                print("2. Búsqueda de paciente por clave")
                print("3. Búsqueda de pacientes por apellidos y nombres")
                try:
                    eleccion_consulta_paciente = int(
                        input("\nAcciones que se pueden realizar en Consultas: ")
                    )
                    break
                except:
                    print("\n\tEl dato deberia de ser numerico. Intente de nuevo.")
                    continue
            # Mostrarse todos los registros de pacientes
            if eleccion_consulta_paciente == 1:
                for clave, datos_paciente in registro_paciente.items():
                    nueva_variable = registro_paciente[clave]
                    print(f"\nClave {clave}")
                    print(f"Primer Apellido {nueva_variable[0]}")
                    print(f"Segundo Apellido {nueva_variable[1]}")
                    print(f"Nombre {nueva_variable[2]}")
                    print(f"Fecha de nacimiento {nueva_variable[3]}")

                print("\nSe mostraran los registros de pacientes")
                break
            # Búsqueda de paciente por clave
            elif eleccion_consulta_paciente == 2:
                while True:
                    try:
                        clave_busqueda = int(
                            input("\nIntroduzca la clave del paciente a buscar: ")
                        )
                        break
                    except:
                        print(
                            "\n\tLa clave debe ser un numero entero. Intente de nuevo"
                        )
                        continue
                if clave_busqueda in registro_paciente:
                    datos_paciente = registro_paciente[clave_busqueda]
                    print("\nDatos del paciente:")
                    print(f"Clave: {clave_busqueda}")
                    print(f"Primer Apellido: {datos_paciente[0]}")
                    print(f"Segundo Apellido: {datos_paciente[1]}")
                    print(f"Nombre: {datos_paciente[2]}")
                    print(f"Fecha de Nacimiento: {datos_paciente[3]}")
                    break
                else:
                    print(
                        "\n\tNo se encontró un paciente con esa clave. Intente de nuevo"
                    )
                    continue
            # Busqueda paciente por nombres y apellidos
            elif eleccion_consulta_paciente == 3:
                while True:
                    apellidos_nombres = input(
                        "\nIntroduzca los apellidos y nombres del paciente a buscar: "
                    )
                    resultados_busqueda = []
                    for clave, datos in registro_paciente.items():
                        nombre_completo = f"{datos[0]} {datos[1]} {datos[2]}"
                        if apellidos_nombres.lower() in nombre_completo.lower():
                            resultados_busqueda.append(
                                [clave, datos[0], datos[1], datos[2], datos[3]]
                            )

                            print(resultados_busqueda)
                            break
        # Salir
        elif eleccion_consulta_o_reporte == 3:
            continue
        # En caso de que no sea un numero entre los indicados
        else:
            print("\n\tLa opcion debe de ser alguna de las proporcionadas")
            continue

    elif eleccion_pacientes == 5:
        try:
            salir = input("\n¿Seguro que desea salir? Introduzca SI o NO")
        except:
            print("\n\tEl dato que proporciona es incorrecto. Intente de nuevo")
        if salir.upper() == "SI":
            break
        else:
            continue
    else:
        print("\n\tEl dato debe ser un numero del 1 al 5. Intente de nuevo")
        continue
