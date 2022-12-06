print("Evaluacion de las notas de los alumnos")

nota_alumno=input("Introduce la nota del alumno: ")


def evaluacion(nota):
	valoracion="Aprobado"
	if nota<5:
		valoracion="Desaprobado"
	return valoracion

print(evaluacion(int(nota_alumno)))