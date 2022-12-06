
contador=0
miEmail=input("introduce tu direccion de email ")

for i in miEmail:

	if (i=="@" or i=="."):

		contador=contador+1

if contador>1:

	print("el email es correcto")

else:

	print("el email es incorrecto")	

for i in range(5):

	print(f"valor de la variable {i}")

