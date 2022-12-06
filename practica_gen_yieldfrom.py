def devevuelve_cidudades(*ciudades):
	for elemento in ciudades:

		yield from elemento

ciudades_devultas=devevuelve_cidudades("Lima", "Callao", "Sanjuan de lurigancho")

print(next(ciudades_devultas))

print(next(ciudades_devultas))