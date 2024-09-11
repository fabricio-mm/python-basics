from figuras import Figuras, Circulo, Quadrado, Triangulo

circulo = Circulo(cor='Azul', preenchido=True, radius=5) #Voce pode instaciar dessa maneira para melhor legibilidade
quadrado = Quadrado(cor='Verde', preenchido=False, largura=8)
triangulo = Triangulo(cor='Roxo', preenchido=True, largura=8, altura=7)

circulo.descrever()
print()
quadrado.descrever()
print()
triangulo.descrever()

'''
Repare que vai ser usado o método da classe filha e da classe pai ao mesmo tempo
basicamente o que nós fizemos foi extender a funcionalidade do método da classe filha com o da classe pai
'''

'''
 o método super() te dá segurança quando não for criar classes abstratas, ele permite que você pegue atributos da classe pai e use nas classes filhas
 obrigatoriamente quando for instanciá-las caso tenham algum dado em comum.
'''