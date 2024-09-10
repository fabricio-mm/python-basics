# herança multipla = herda de mais de uma classe parente
#                       C(A,B)

# herança de multinível = herda de uma classe parente que está herdando de outra
#                       C(B) <- B(A) <- A

class Animal: #Classe Pai, engloba todos os animais
    num_animais = 0
    def __init__(self, nome):
        self.nome = nome
        Animal.num_animais +=1 

    def comer (self):
        print(f"O animal {self.nome} está comendo") 

    def dormir(self):
        print(f"O animal {self.nome} está dormindo")

         
class Presa(Animal):
    def fugir (self):
        print(f'O animal {self.nome} está fugindo')
    

class Predador(Animal):
    def cacar(self):
        print(f'O animal {self.nome} está caçando')

class Coelho(Presa): #Este está herdando somente o método fugir
    pass
    
class Gaviao(Predador): #Este herda apenas o método cacar
    pass

class Peixe(Predador,Presa): #Este herda ambos os métodos
    pass

coelho = Coelho("Buggie")
gaviao = Gaviao("Tony")
peixe = Peixe("Nemo")

print(Animal.num_animais)
coelho.comer()
coelho.fugir()
gaviao.cacar()
peixe.cacar()
peixe.fugir()