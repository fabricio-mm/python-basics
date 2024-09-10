# super() = função usada em uma classe filha para chamar métodos de uma classe pai (superclasse).
#       Permite você extender as funcionalidade de uma herença de métodos

class Figuras:
    def __init__(self, cor, preenchido):
        self.cor = cor
        self.preenchido = preenchido
#Reparem que essa classe tem dois atributos 

class Circulo(Figuras): #Criando a classe circulo eu quis por nela também o atributo cor e preenchido
    def __init__(self, cor, preenchido, radius):
        super().__init__(cor, preenchido) # Eu consigo por essa sintaxe, passando o construtor da minha classe Figuras por meio do método super()
        self.radius = radius

class Quadrado(Figuras):
    def __init__(self, cor, preenchido, largura):
        super().__init__(cor, preenchido)
        self.largura = largura

class Triangulo(Figuras):
    def __init__(self, cor, preenchido, altura, largura):
        super().__init__(cor, preenchido)
        self.altura = altura
        self.largura = largura

circulo = Circulo(cor='Azul', preenchido=True, radius=5) #Voce pode instaciar dessa maneira para melhor legibilidade
quadrado = Quadrado(cor='Verde', preenchido=False, largura=8)
triangulo = Triangulo(cor='Roxo', preenchido=True, largura=8, altura=7)

print(triangulo.cor)
print(triangulo.preenchido)
print(f' Largura: {triangulo.largura}cm \n Altura: {triangulo.altura}cm')


'''
 o método super te dá segurança quando não for criar classes abstratas, ele permite que você pegue atributos da classe pai e use nas classes filhas
 obrigatoriamente quando for instanciá-las caso tenham algum dado em comum.
'''