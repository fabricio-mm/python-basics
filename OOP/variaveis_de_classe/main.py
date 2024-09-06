# variavel de classe = Compartilhada entre todas as instancias de uma classe
#               Definida fora do construtor
#               Permite compartilhar dados entre todos os objetos criados a partir daquela classe
#               instancias são declaradas dentro do construtor. Exemplo:
# class Carro:
#    rodas = 4 <----------- variável de classe
#    def __init__(self, modelo, ano): <<<< construtor
#       self.modelo = modelo       <------------ variáveis instanciadas 
#       self.ano = ano

class Animal:
    class_dono = 'Fabricio'
    num_animais = 0 # Vai servir para nos dizer a quantidade de animais que nós já cadastramos
    def __init__(self, nome, grupo, peso, patas):
        self.nome = nome
        self.grupo = grupo
        self.peso = peso
        self.patas = patas
        Animal.num_animais += 1 #Isso está dizendo que sempre que um objeto animal for criado, irá ser somado 1 em num_animais

# obs... Sempre que criamos um novo objeto usamos o construtor, então como Animal.num_animais foi colocado dentro do construtor.
# se criamos 5 contrutores de animais será 1 x 5
# animal = >>>>> Animal() <<<<< este é o construtor.

animal1 = Animal('Pato', 'Ave', '14Kg', 2)
animal2 = Animal('Cachorro', 'Mamifero', '32Kg', 4)
animal3 = Animal('Baleia', 'Mamífero', '9T', 0)
animal4 = Animal('Rato', 'Mamífero', '800Gm', 4)

print(Animal.num_animais) # Será exibido o numero de animais criados
print (animal1.nome)
print (animal1.peso)
print(animal1.class_dono) # Chamando a variável de classe class_dono = 'Fabricio'
print(Animal.class_dono) # Estamos chamando a variável de classe através da classe Animal
# É uma boa prática acessar as variáveis de classe sempre pelo nome da classe, no nosso caso aqui é Animal

# A título de estudo vamos usar a variavel class_dono e num_animais eo mesmo tempo
print(f'Olá, meu nome é {Animal.class_dono} e eu tenho {Animal.num_animais} animais')
print(animal1.nome)
print(animal2.nome)
print(animal3.nome)
print(animal4.nome)