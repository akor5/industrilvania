# Personajes #
class Personaje:
	def __init__(self):
		self.__nombre = ""
		self.__fuerza = 0
		self.__destreza = 0
		self.__inteligencia = 0
		self.__habilidadCC = 0
		self.__salud = 0


class Licantropo(Personaje):
	def __init__(self):
		self.__poder = 0
		self.__narmas = 0
		self.__ndonS = 0
		self.__dones = []
		self.__armas = []

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
	