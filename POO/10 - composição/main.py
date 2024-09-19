'''
Agregação = Uma relação com um objeto que contém referencia a o um objeto independente
				"Tem" uma relação

Composição = Ao compor um objeto, o composto detém diretamente seus componentes, os quais não podem existir de forma
independente.
				"Possui" uma relação
'''

class Motor:
	def __init__( self, horse_pw ):
		self.horse_pw = horse_pw

class Roda:
	def __init__(self, aro):
		self.aro = aro

class Carro:
	def __init__( self, marca, model, horse_pw, aro ):
		self.marca = marca
		self.model = model
		self.motor = Motor(horse_pw)
		self.aro = [Roda(aro)for roda in range (4)]

	def display_carro( self ):
		return f"{self.marca} {self.model} {self.motor.horse_pw}hp aro: {self.aro[0].aro}"

carro = Carro("Toyota", "Supra", 450, 18) #
carro2 = Carro("Ford", "GT", 750, 20)
print(carro.display_carro())
print(carro2.display_carro())

'''
Repare que se apagarmos o objeto carro, as rodas e o mortor vão deixar de existir 
isso acontecem justamente por eles serem compornentes de um carro.
'''