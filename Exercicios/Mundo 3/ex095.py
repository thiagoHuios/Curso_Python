jogadores = list()
mais_partidas = 0

print('-' * 40)

while True:
    jogador = dict()
    gols = list()
    total_gols = 0

    jogador['Nome'] = str(input('Insira o nome do jogador: '))
    while True:
        try:
            qtd_partidas = int(input('Insira quantas partidas foram jogadas: '))
            break
        except ValueError:
            print('Insira um valor válido!')

    for g in range(1, qtd_partidas + 1):
        while True:
            try:
                gols.append(int(input(f'Insira quantos gols foram feitos na paritda {g}: ')))
                break
            except ValueError:
                print('Insira um valor válido!')

    jogador['Gols'] = gols[:]
    jogador['Total gols'] = sum(gols)

    jogadores.append(jogador.copy())
    del jogador, gols, total_gols

    while True:
        continuação = str(input('Deseja inserir mais jogadores [S/N]: '))
        if continuação in 'SsNn':
            print('-' * 40)
            break
    if continuação in 'Nn':
        break

print(f'{'Cod.':<5}{'Nome':<20}{'Gols':<15}{'Total'}')

for i, p in enumerate(jogadores):
    gols_list = str(p['Gols'])
    print(f'{i+1:<5}{p['Nome']:<20}{gols_list:15}{p['Total gols']}')

print('-' * 40)

while True:
    dados_jogador = str(input('Insira o codigo do jogador para ver seu dados [Ou insira FECHAR]: ')).lower().strip()
    if dados_jogador.isdigit():
        dados_jogador = int(dados_jogador)
        if dados_jogador >= len(jogadores):
            print('Insira uma opção válida!')
        else:
            print('-' * 40)
            print(f'Levantamendo de daodos do jogador: {jogadores[dados_jogador - 1]['Nome']}')
            for p in range(1, (len(jogadores[dados_jogador -1]['Gols']) + 1)):
                print(f'No jogo {p} fez {jogadores[dados_jogador -1]['Gols'][p - 1]}')

    elif dados_jogador == 'fechar':
        print('-' * 40)
        break

