'''
duck typing é uma outra maniera de fazer polimorfismo ao invés de herança
			o objeto deve ter um numero minimo de atributos/métodos
			"se isso parece um pato, faz quack como um pato, isso deve ser um pato"
'''

class Animal:
	alive = True

class Cachorro(Animal):
	def speak( self ):
		print("WOOF!")

class Gato(Animal):
	def speak( self ):
		print("MEOW!")

class Carro:
	alive = True

	def speak( self ):
		print("HONK!")

animals = [Cachorro(), Gato(), Carro()]

for animal in animals:
	animal.speak()
	print(animal.alive)

'''
	 reparem que carro, apesar de não ser um animal, ele tem o método speak e tem o atributo alive como um animal,
	 isso faz com que ele seja executado no for. Isso é duck typing.
'''