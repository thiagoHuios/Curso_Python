import random
print('Ordem de apresentação dos trabalhos da sala 9B')
print('Digite o nomes dos alunos para sortear a ordem de apresentação:')
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
deck = [a1, a2, a3, a4]
random.shuffle(deck)
print('A ordem de apresentação será: \n{}'.format(deck))
