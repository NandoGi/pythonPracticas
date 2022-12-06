print("verificacion de notas")

nota_alumno=int(input("introduce tu nota, please" ))

if nota_alumno<5:
	print("desaprobado-reforzamiento intensivo")
elif nota_alumno<10:
	print("desaprobado-reforzamiento")
elif nota_alumno<13:
	print("aprobado-reforzamiento")
elif nota_alumno<17:
	print("aprobado-sigue asi")
elif nota_alumno>20:
	print("nota incorrecta - sirvase a verificar la nota")
else:
	print("aprobado-muy buen trabajo")

print("finalizado-hasta luego")