jogador = dict()
gols = list()
total_gols = 0

print('-' * 40)

jogador['Nome'] = str(input('Insira o nome do jogador: '))
qtd_partidas = int(input('Insira quantas partidas foram jogadas: '))

for g in range(1, qtd_partidas + 1):
    gols.append(int(input(f'Insira quantos gols foram feitos na paritda {g}: ')))

jogador['Gols'] = gols[:]
jogador['Total gols'] = sum(gols)

print('-' * 40)

for k, v in jogador.items():
    print(f'{k} tem o valor de: {v}')

print('-' * 40)

print(f'O jogador {jogador['Nome']} jogou {qtd_partidas} partidas.')

for p in range(0, qtd_partidas):
    print(f'Na partida {p + 1}, fez: {jogador['Gols'][p]} gols')

print(f'Tendo um total de {sum(gols)}')

print('-' * 40)
