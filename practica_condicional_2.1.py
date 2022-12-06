print("Asignaturas optativas año 2022")
print("Asignaturas optativas: Matematica - Seguridad - Ingles")
opcion=input("Escribe la asignatura escogida: ")

asignatura=opcion.lower()

if asignatura in ("matematica", "seguridad", "ingles"):

	print("Asignatura elegida" + asignatura)

else:

	print("No es correcta la asignatura elegida - favor de revisar otra vez la lista")