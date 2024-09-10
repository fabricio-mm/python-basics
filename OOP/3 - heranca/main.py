# Herança = Permite uma classe herdar atributos e métodos de outra classe
        # Ajuda na reusabilidade e extendibilidade
        # class Child (Parent)
 
class Animal:
    num_animais = 0
    def __init__(self, nome):
        self.nome = nome
        self.is_alive = True
        Animal.num_animais += 1
        
    def comer (self):
        print(f'{self.nome} está comendo')
    def dormir(self):
        print (f'{self.nome} está dormindo')
#CLASSES HERDEIRAS - Compartilham de alguns atributos e métodos da classe Pai, porém ainda podem ter métodos especificos de cada uma
class Cachorro(Animal):
    numero = 0
    def latir(self):
        print('WOOF!')

class Gato(Animal):
    def miar(self):
        print('meeeow!')

class Rato(Animal):
    def ratata(self):
        print('RATATA!')

#Repare que criamos 3 classes e colocamos como parametro das classes a classe Animal que aqui vamos chamar de classe Pai
#As classes filhos vão herdar todos os atributos e métodos da classe pai
cachorro = Cachorro('Enkidu')
gato = Gato('Garfield')
rato = Rato('Ratata')

#A classe cachorro usando os métodos e atributos da classe Pai
cachorro.dormir()
cachorro.comer()
print(cachorro.nome)
print(cachorro.is_alive)

#Atributos individuais de cada classe herdeira
cachorro.latir()
gato.miar()
rato.ratata()

# A herança é excelente pq evita que tenhamos que escrever várias linhas de código criando atributos e métodos para classe semelhantes
# Outro fator interessante é que se houver a necessidade de realizar alguma mudança, se mudar algo na classe Pai, as classes herdeiras tbm serão alteradas.