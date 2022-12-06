class Vehiculos():

	def __init__(self, marca, modelo):

		self.marca=marca
		self.modelo=modelo
		self.enmarcha=True
		self.acelera=True
		self.frena=False

	def arrancar(self):

		self.enmarcha=True

	def acelerar(self):

		self.acelera=True

	def frenar(self):

		self.frena=True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
			self.enmarcha, "\nAcelerando: ", self.acelera, "\nfrenando: ", self.frena)



class Furgoneta(Vehiculos):

	def carga(self, cargar):
		self.cargado=cargar
		if(self.cargado):
			return "la furgoneta esta cargada"
		else:
			return "la furgoneta no esta cargada"

print("MOTO")
class Moto(Vehiculos):
	hcaballito=""
	def caballito(self):
		self.hcaballito="Voy haciendo el caballito"


	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
	self.enmarcha, "\nAcelerando: ", self.acelera, "\nfrenando: ", self.frena, "\n", self.hcaballito) 

class VElectricos(Vehiculos):

	def __init__(self, marca, modelo):

		super().__init__(marca, modelo)

		self.autonomia=100

	def cargarEnergia(self):

		self.cargando=True


miMoto=Moto("Honda", "CBR")

miMoto.caballito()

miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Toro")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))

print("BICICLETA")
class BicicletaElectrica(VElectricos, Vehiculos):
	hcaballito=""
	Vgiro360=360
	def caballito(self):
		self.hcaballito="Voy haciendo el caballito"

	def Vgiro360(self, giro):
		self.giro=360
		if(self.giro):
			return "Se esta realizando giro de: 360 grados" 
		else:
			return "No se ha podido completar realizar el giro"


	def estado(self): 
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
	self.enmarcha, "\nAcelerando: ", self.acelera, "\nfrenando: ", self.frena, "\n", self.hcaballito) 

miBici=BicicletaElectrica("Biker", "360°")

miBici.caballito()

miBici.estado()

print(miBici.Vgiro360(True))






