salario_presidente=int(input("introduce salario presidente "))
print("salario presidente: " + str(salario_presidente))

salario_director=int(input("introduce salario director "))
print("salario director: " + str(salario_director))

salario_jefe_area=int(input("introduce salario Jefe area "))
print("salario jefe area: " + str(salario_jefe_area))

salario_adminitrativo=int(input("introduce salario administrativo "))
print("salario administrativo: " + str(salario_adminitrativo))

if salario_adminitrativo<salario_jefe_area<salario_director<salario_presidente:
	print("todo funciona correctamente")
else:
	print("algo anda mal")
