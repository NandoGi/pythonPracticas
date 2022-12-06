class Coche():
	
	def __init__(self):

		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4
		self.__enmarcha=False

	def arrancar(self,arrancamos):
		self.__enmarcha=arrancamos

		if(self.__enmarcha):
			chequeo=self.chequeo_interno()

		if(self.__enmarcha and chequeo ):
			return "El coche esta en marcha"

		elif(self.__enmarcha and chequeo==False):
			return "Algo ha salido mal en el chequeo. No podemos arrancar el auto"

		else:
			return "El coche esta detenido"	

	def estado(self):
		print("el coche tiene ", self.__ruedas, " ruedas ", "un largo de ", self.__largoChasis, "y un ancho de ", 
			self.__anchoChasis)


	def chequeo_interno(self):
		print("Realizando chequeo interno")

		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):

			return True

		else:

			return False


miCoche=Coche()
print(miCoche.arrancar(True))

miCoche.estado()

print("---------------A continuacion creamos el segundo objeto----------------")

miCoche2=Coche()
miCoche.ruedas=2
print(miCoche2.arrancar(False)) 


miCoche2.estado()