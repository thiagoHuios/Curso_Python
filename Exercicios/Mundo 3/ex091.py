from operator import itemgetter
from random import randint
from time import sleep

jogada = dict()
jogadas = list()
ordem = [0]
cont = 0

for r in range(1, 5):
    jogada[f'Jogador {r}'] = randint(1, 6)
    jogadas.append(jogada.copy())
    del jogada[f'Jogador {r}']

print('Valores Sorteados: \n')

for r in jogadas:
    for k, v in r.items():
        print(f'{k} tirou: {v}')
        ordem.append(v)


print('-' * 20)
print('Ranking dos Jogadores \n')

ordem.sort(reverse=True)

while True:
    for ra in jogadas:
        for k, v in ra.items():
            if v == ordem[cont]:
                print(f'{cont + 1}º Lugar: {k} com {v}')
                cont +=1
    if cont == 4:
        break

#=========================================================

from random import randint
from time import sleep

jogada1 = {'Jogador1': randint(1, 6),
          'Jogador2': randint(1, 6),
          'Jogaodor3':randint(1, 6),
          'Jogador4': randint(1, 6)}

print('\nValores Sorteados: \n')

for k, v in jogada1.items():
    print(f'{k} tirou: {v}')
    sleep(0.5)
print('-' * 20)
print('Ranking dos Jogadores \n')

ranking = sorted(jogada1.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')



