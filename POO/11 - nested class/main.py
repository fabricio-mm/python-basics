'''
Nested class = Uma classe que é definida dentro de outra
					class Fora:
						class Dentro:

Beneficios: Permite pra você logicamente agrupar classes que são minimamente relacionadas
				Encapsula detalhes privados que não são relevantes fora da classe principal
				Mantém o código limpo; reduz a possibilidade de ocorrer comflitos de nome
'''
class Compania:

	class Funcionario:
		def __init__(self, nome, cargo):
			self.nome = nome
			self.cargo = cargo

		def detalhes( self ):
			return f"{self.nome}: {self.cargo}"

	def __init__(self, com_nome): #criando o construtor da Compania
		self.com_nome = com_nome
		self.funcionarios = [] #lista onde vamos armazenar nossos funcionarios.

	def add_funcionario( self, nome, cargo ):
		novato = self.Funcionario(nome, cargo) #self neste caso vai se referenciar à "outer class", a classe que está englobando as outras classes
		self.funcionarios.append(novato)

	def lista_funcionarios( self ):
		return [funcionario.detalhes() for funcionario in self.funcionarios] #pegue os detalhes() para cada funcionario em self.funcionarios

com = Compania("Liga da Justiça 2")
print(f"============================ {com.com_nome} ================================")
com.add_funcionario("Superman", "Protetor")
com.add_funcionario("Batman", "Vigilante")
com.add_funcionario("Iron Man", "Investidor")

for funcionario in com.lista_funcionarios():
	print(funcionario)

com2 = Compania("Vingar Dores")
print(f"============================ {com2.com_nome} ================================")
com2.add_funcionario("Thor", "Protetor")
com2.add_funcionario("Aranha Humana", "Estagiário")
com2.add_funcionario("Coringa", "Psicólogo")

for funcionario in com2.lista_funcionarios():
	print(funcionario)