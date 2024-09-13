'''
Polimorfismo = É uma palavra grega que significa "Varias formas ou faces"
               Poli = Várias
               Morfismo = Formas

               Duas formas de fazer polimorfismo
               1. Herança = Um objeto pode ser tratado como do mesmo tipo que uma classe pai
               2. "Duck typing" = O objeto deve ter atributos e métodos necessários
'''


'''
Vamos pensar o seguinte, pensa num circulo, um circulo é um circulo, mas também é uma forma. 1 objeto, com duas faces
'''
from abc import ABC, abstractmethod
class Forma:
    
    @abstractmethod
    def area(self):
        pass

class Circulo(Forma):
    def __init__(self, raio):
        self.raio =raio
    def area(self):
        return 3.14 * (self.raio ** 2)

class Quadrado(Forma):
    def __init__(self, base): #Lembrando que a base e a altura é sempre a mesma quando se trata de um quadrado
        self.base = base
    def area(self):
        return self.base * 2
    
class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base * self.altura) / 2

#Um exemplo com pizza, uma pizza tem uma forma, ela é circular, então podemos fazer ela herdar os métodos e atributos de Circulo.    
class Pizza(Circulo):
    def __init__(self, ingrediente, raio):
        super().__init__(raio)
        self.ingrediente = ingrediente