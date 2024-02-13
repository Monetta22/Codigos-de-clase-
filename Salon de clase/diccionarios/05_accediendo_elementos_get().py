# En caso de que no exista la clave solicitada, no se generará un error y se retornará el valor default proporcionado.

diccionario = {1: "Value 1", 2: "Value 2", 3: "Value 3"}

print(diccionario.get(3, "No existe"))
