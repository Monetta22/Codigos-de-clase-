import datetime

# Determinado en YYYY/MM/DD
fecha_usuario = "2005/11/01"

fecha_usuario_convertida = datetime.datetime.strptime(fecha_usuario, "%Y/%m/%d").date()

fecha_actual = datetime.date.today()

edad_años = fecha_actual.year - fecha_usuario_convertida.year

if fecha_actual < datetime.date(
    fecha_actual.year, fecha_usuario_convertida.month, fecha_usuario_convertida.day
):
    edad_años -= 1

print(f"La edad del usuario es: {edad_años} años")
