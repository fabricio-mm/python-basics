# O arquivo, carro.py é onde está nossa classe e vamos impotá-lo pra cá como um módulo

from carro import Carro #importamos nossa classe Carro, agora basta criar um novo objeto.
carro1 = Carro('Mustang', 2024, 'Azul', False)  #print (carro1) = <__main__.Carro object at 0x000001D1D77FA5D0> (endereço de memória)
carro2 = Carro('Corvette', 2023, 'Vermelho', True)
carro3 = Carro('Civic', 2020, 'Preto', True)
carro4 = Carro('Uno', 2001, 'Amarelo', False)
print(carro3.modelo) #Civic
print(carro3.ano) #2020
print(carro3.cor) #Preto
print(carro3.a_venda) #True

#Você pode ir alterando entre carro1, 2 e 3 para conseguir diferentes resultados no seu console
#Lembrando que sempre que for printar um atributo de um objeto a sintaxe é: print(objeto.atributo)

#Vamos acessar os métodos que criamos anteriormente
carro3.dirigir() #Você esta dirigindo o carro
carro3.parar() #Você parou o carro
carro3.descrever()
#Você pode testar o acesso a esses métodos com qualquer um dos objetos criados

#Para finalizar a explicação, Objetos são um conjunto de atributos e métodos
#Atributos são caracteristicas de um objeto
#Métodos é tudo aquilo que o objeto pode fazer 

#FIM

