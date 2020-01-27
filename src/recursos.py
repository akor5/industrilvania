#Todos los recursos#
class Recurso:
	def __init__(self):
		self.__nombre = ""
		self.__id = "AA0"
		self.__alcance = 0
		self.__poderOfensivo = 0
		self.__poderDefensivo = 0
		self.__astucia = 0
	def modificarAtributos(self,a):
		if a == True:
			self.__nombre = input("Introduzca el nombre: ")
		while True:
			self.__alcance = int(input("Introduzca el alcance del arma (0-> cuerpo a cuerpo 1-> a distancia): "))
			if self._alcance <= 1 and self._alcance >= 0:
				break
		self.__poderOfensivo = int(input("Introduzca el poder ofensivo del arma: "))
		self.__poderDefensivo = int(input("Introduzca el poder defensivo del arma: "))
		self.__astucia = int(input("Introduzca la astucia del arma: "))

	def displayAtributos(self):
		print ("Nombre del recurso: ", self.__nombre)
		print ("identificador: ", self.__id)
		if self.__alcance == 0:
			print ("Alcance: cuerpo a cuerpo")
		else:
			print("Alcance: a distancia")
		print ("Poder defensivo: ", self.__poderDefensivo)
		print ("Poder ofensivo: ", self.__poderOfensivo)
		print ("Astucia: ", self.__astucia)

class Artefacto(Recurso):
	def __init__(self):
		self.__clase = 0
		self.__poder = 0
		self.__tipo = 2
	def modificarAtributos(self,a):
		super().modificarAtributos(self,a)
		while True:
			self.__manejo = int(input("Introduzca el manejo del arma ( 0 = una mano,  1 = dos manos): "))
			if self.__manejo == 0 or self.__manejo == 1:
				break
		self.__clase = int(input("Introduzca la clase del arma (1.Ofensivo 2.Defensivo 3.Astucia): "))
		self.__poder = int(input("Introduzca el poder del arma: "))

class DonSobrenatural(Recurso):
	def __init__(self):
		self.__naturaleza = 0
		self.__tipo = 3
	def display(self):
		super.displayAtributos(self)
		if self.__naturaleza == 1:
			print("Naturaleza: Salvaje")
		else if self.__naturaleza == 2:
			print ("Naturaleza: Mágica")
		else:
			print ("Naturaleza: Demoníaca")
	def modificarAtributos(self, a):
		super().modificarAtributos(self, a)
		while True:
			self.__naturaleza = int(input("Introduzca la naturaleza del Don Sobrenatural (1.Salvaje 2.Mágica 3.Demoníaca): "))
			if self.__naturaleza == 1 or self.__naturaleza == 2 or self.__naturaleza == 3:
				break
class Arma(Recurso):
	def __init__(self):
		self.__manejo: 0 
		self.__tipo: 1
	def modificarAtributos(self,a):
		super().modificarAtributos(self,a)
		self.__manejo = int(input("Introduzca el manejo del arma ( 0 = una mano,  1 = dos manos): "))
	def display (self):
		super().displayAtributos(self)
		if self.__manejo == 0:
			print ("Manejo: Una mano")
		else:
			print("Manejor: Dos manos")




