import math

i=1

while i<=10:

	print("ejecucion" + str(i))
	i=i+1

print("terminó la ejecucion")

edad=int(input("introduce la edad porfavor: "))

while edad<18 or edad>45:
	print("has introducido una edad incorrecta, porfavor vuelve a intentarlo cara de pedo")
	edad=int(input("introduce la edad porfavor: "))

print("gracias por colaborar, puedes pasar")
print("edad del aspirante" + str(edad))

print("PROGRAMA DE CALCULO DE RAIZ CUADRADA")
numero=int(input("introduce un numero porfavor: "))

intentos=0

while numero<0:
	print("no se puede hallar la raiz de un numero negativo")

	if intentos==2:
		print("has realizado demasidos intentos. el programa a finalizado")
		break;

	numero=int(input("introduce un numero nuevo porfavor: "))
	if numero<0:
		intentos=intentos+1

if intentos<2:
	solucion=math.sqrt(numero)
	print("la raiz cuadrada de " + str(numero) + " es " + str(solucion))