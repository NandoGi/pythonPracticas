class Auto():
	
	def __init__(self):

		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4
		self.__enmarcha=False

	def arrancar(self,arrancamos):
		self.__enmarcha=arrancamos

		if(self.__enmarcha):
			chequeo=self.__chequeo_interno()

		if(self.__enmarcha and chequeo ):
			return "El Auto esta en marcha"

		elif(self.__enmarcha and chequeo==False):
			return "Algo ha salido mal en el chequeo. No podemos arrancar el auto"

		else:
			return "El Auto esta detenido"	

	def estado(self):
		print("el Auto tiene ", self.__ruedas, " ruedas ", "un largo de ", self.__largoChasis, "y un ancho de ", 
			self.__anchoChasis)


	def __chequeo_interno(self):
		print("Realizando chequeo interno")

		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):

			return True

		else:

			return False


miAuto=Auto()
print(miAuto.arrancar(True))

miAuto.estado()

print("---------------A continuacion creamos el segundo objeto----------------")

miAuto2=Auto()
print(miAuto.arrancar(False)) 


miAuto2.estado()
