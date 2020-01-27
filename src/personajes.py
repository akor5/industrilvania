# Personajes #
class Personaje:
	def __init__(self):
		self.__nombre = ""
		self.__fuerza = 0
		self.__destreza = 0
		self.__inteligencia = 0
		self.__habilidadCC = 0
		self.__salud = 3
		self.__recursos = []
		#self.__Nrecursos = 0
	def modificarAtributos(self, a):
		if a: #Si no funciona probar con a == True
			self.__nombre = input ("Introduzca el nombre del personaje: ")
		self.__fuerza = input ("Introduzca su fuerza: ")
		self.__destreza = input ("Introduzca su destreza: ")
		self.__inteligencia = input ("Introduzca su inteligencia: ")
		self.__habilidadCC = input ("Introduzca su habilidad cuerpo a cuerpo: ")
	def displayPersonaje(self, a):
		print ("Fuerza: ",self.__fuerza)
		print ("Destreza: ",self.__destreza)
		print ("Inteligencia: ",self.__inteligencia)
		print ("Habilidad cuerpo a cuerpo: ",self.__habilidadCC)
		print ("Salud: ",self.__salud)
	def displayRecursosEquipados(self):
		i = 0
		for item in self.__recursos:
			i++
			print ("Recurso asingado nº ", item,": ")
			self.__recursos[item].display()

class Licantropo(Personaje):
	def __init__(self):
		self.__poder = 0
		self.__narmas = 0
		self.__ndonS = 0
		self.__dones = []
		self.__armas = []
	def display(self):
		super().displayPersonaje(self)
		print ("Poder sobrenatural: ", self.__poder)
		displayRecursosEquipados(self) #Si no funciona probar con super().displayRecursosEquipados(self)
	def modificar(self,a):
		super.modificarAtributos(self,a)
		self.__poder = int(input("Introduzca el poder sobrenatural: "))
class Cazador(Personaje):
	def __init__(self):
		self.__habArmasDis = 0
		self.__nArtefactos = 0
		self.__artefactos = []
		self.__armas = []


class Vampiro(Personaje):
	def __init__(self):
		self.__habArmasDis = 0
		self.__poderVamp = 0
		self.__ghouls = []
		self.__nGhouls = 0
		self.__nArmas = 0
		self.__nDonS = 0
		self.__dones = []
		self.__armas = []

class Ghoul:
	def __init__(self):
		self.__nombre = ""
	