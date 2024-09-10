#Classe abstrata: Uma classe que não consegue ser instanciada por si mesmo; Precisa de uma subclasse
#            Elas contém métodos abtratos, que são declarados, mas sem implementação
#            Beneficios de uma classe abstrata:
#            1. Previne a instancia de uma classe por si só
#            2. Requer classes filhas para herdar os métodos abstratos

from abc import ABC, abstractmethod 
#O módulo abc fornece a classe ABC, que é usada para criar classes base abstratas.
#Para criar uma classe base abstrata, você herda da classe ABC e usa o decorador @abstractmethod para declarar métodos abstratos.
class Veiculo(ABC): # <<<<<<<<<<< Classe abstrata

    @abstractmethod #Sintaxe necessária para criar um método de uma classe abstrata
    def andar(self): #repare que o método existe, mas não gera nenhum resultado
        pass

    @abstractmethod
    def parar(self):
        pass

class Carro (Veiculo):
    def andar(self):
        print('Você está dirigindo o carro')

    def parar(self):
        print('Você parou o carro')
    
class Moto (Veiculo):
    def andar(self):
        print('Você está pilotando a moto')

    def parar(self):
        print('Você parou a moto')

class Barco (Veiculo):
    def andar(self):
        print('Você está navegando com o barco')

    def parar(self):
        print('Você ancorou o barco')

#OBS... Se você se esquecer de colocar todos os métodos da classe abstrata, você receberá um TYPEERROR
#Isso acontece porque você é obrigado o instanciar todos os métodos da classe abstrata para que um objeto de uma classe filha dela possa ser criado

car = Carro()
moto = Moto()
barco = Barco()
#=====================================
car.andar()
car.parar()
#=====================================
moto.andar()
moto.parar()
#=====================================
barco.andar()
barco.parar()
#Repare que apesar desses veículos herdarem da mesma classe, seus métodos tem resultados diferentes
#Ambos os métodos foram herdados da classe abstrata, mas como os métodos estavam "incompletos", isso te dá o possibilidade de usá-los de diferentes formas
#Resumindo, classes abstratas trazem segurança caso você queira objetos bem padronizados com todos os métodos definidos nela obrigatóriamente
#Isso ajuda a previnir erros e perda de tempo refatorando o código porque alguém esqueceu de botar um método em tal classe padrão
