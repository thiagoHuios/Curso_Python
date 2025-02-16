import random
print('Quem irá por o Lixo pra fora?')
print('Insira os nomes para serem sorteados:')
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
lista = [n1, n2, n3, n4]
print('O nome sorteado pra por o lixo pra fora foi: {}'.format(random.choice(lista)))
