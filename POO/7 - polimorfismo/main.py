from formas import *
"""
Agora vamos supor que tenhamos que criar uma lista de formas, o que elas tem em comum?
                             *** TODAS SÂO FORMAS ***
"""

formas = [Circulo(4), Quadrado(8), Triangulo(4,8), Pizza("Calabresa", 15)] #Aqui estamos criando um objeto de cada classe passando os parametros necessarios para cada um

for forma in formas: #Para cada forma em formas faça........
    print(f'{forma.area()}cm²')
    '''
    50.24cm�
    16cm�
    16.0cm�
    706.5cm�
    '''

'''
Em suma, podemos dizer que o polimorfismo pode ser usado quando estamos trabalhando com objetos que se encaixam em mais de uma classe
'''
