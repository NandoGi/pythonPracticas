nombreUsuario=input("Introduce tu nombre de Usuario: ")

print("El nombre es: ", nombreUsuario.upper())

edad=input("Introduce la edad: ")

while(edad.isdigit()==False):

	print("porfavor introduce un valor numerico")

	edad=input("introduce la edad: ")

if(int(edad)<18):

	print("no puede pasar")

else:

	print("puede pasar")



