print("Programa de becas 2022")

distancia_escuela=int(input("Introduce la distancia en km "))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el numero de hermanos "))
print(numero_hermanos)

salario_familiar=int(input("Introduce el salario anual bruto "))
print(salario_familiar)

if distancia_escuela>30 and numero_hermanos>2 and salario_familiar<40000:

	print("tienes acceso a la beca")

else:

	print(" no tienes acceso a la beca")

print("gracias por participar ha finalizado el proceso de evaluacion")