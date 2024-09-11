# super() = função usada em uma classe filha para chamar métodos de uma classe pai (superclasse).
#       Permite você extender as funcionalidade de uma herença de métodos

class Figuras:
    def __init__(self, cor, preenchido): #Reparem que esse construtor tem dois atributos
        self.cor = cor
        self.preenchido = preenchido
    
    def descrever(self):
        print(f'Essa forma é {self.cor} e {'preenchida' if self.preenchido else 'não preenchida'}')
 

class Circulo(Figuras): #Criando a classe circulo eu quis por nela também o atributo cor e preenchido
    def __init__(self, cor, preenchido, radius):
        super().__init__(cor, preenchido) # Eu consigo por essa sintaxe, passando o construtor da minha classe Figuras por meio do método super()
                                          # Não sendo necessário declarar as variáveis com o self todas de novo em cada classe
        self.radius = radius

    def descrever(self):
        print(f'Isso é um circulo com area de {3.14 * self.radius * self.radius}cm^2')
        super().descrever() #Isso serve para puxar também o método da classe pai ou superclasse, esse termo também pode ser utilizado quando se refere a classe Pai


class Quadrado(Figuras):
    def __init__(self, cor, preenchido, largura):
        super().__init__(cor, preenchido)
        self.largura = largura

    def descrever(self):
        print(f'Isso é um Quadrado com area de {self.largura * self.largura}cm^2')
        super().descrever()


class Triangulo(Figuras):
    def __init__(self, cor, preenchido, altura, largura):
        super().__init__(cor, preenchido)
        self.altura = altura
        self.largura = largura

    def descrever(self):
        print(f'Isso é um triangulo com area de {self.largura * self.altura / 2}cm^2')
        super().descrever()