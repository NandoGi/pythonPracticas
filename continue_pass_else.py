nombre="Aprendiendo a programar muy facil"

contador=0

for i in nombre:

	if i==" ":
		continue

	contador=contador+1

print(contador)

email=input("introduce tu email, porfavor: ")

for i in email:

	if i=="@":
		arroba=True
		break;

else:

	arroba=False

print(arroba)

segundo="todo esfuerzo es bueno, siempre nos lleva algun lugar"

contador=0

for i in segundo:

	if i==" ":
		continue

	contador=contador+1

print(contador)