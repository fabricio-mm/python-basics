# objeto = um conjunto de atributos (variaveis) e methods (funções)
#               EX.  telefone, copo, livro
#               Você vai precisar de uma classe para criar alguns objetos
# class (classe) = (planta) usada para criar o layout de uma estrutura para um objeto
# Vamos criar um carro:

class Carro:  #Para criar o objeto carro precisamos chamar o método construtor
    def __init__(self, modelo, ano, cor,  a_venda):  #(construtor) esse é o método que cria objetos "init" = 'initialize' o parâmetro self vem por padrão
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.a_venda = a_venda  #self é uma referência a própria instancia, ele permite que você consiga trabalhar com os atributos do objeto

#Vamos falar de métodos:
    def dirigir(self):
        print(f"Você está dirigindo o carro {self.modelo} {self.cor}")  #sempre que esse método for utilizado, a mensagem será printada na tela

    def parar(self):
        print(f"Você parou o carro {self.modelo} {self.cor}") #o mesmo acontece com essa
    
    def descrever(self):
        print(f"{self.modelo} {self.cor} {self.ano}")
#Classe por si só ocupam muito espaço, então deixaremos esse arquivo apenas para a classe Carro e continuamos no aquivo main.py
