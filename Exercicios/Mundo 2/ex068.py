from time import sleep
from random import randint

cont = 0
tipo = ''

while True:
    # ---------------Titulo---------------

    print('-=-' * 20)
    print('PAR OU IMPAR!')
    print('-=-' * 20)

    sleep(0.5)

    # ---------------Pega a opção do usuario---------------

    while True:
        try:
            sel = int(input('Insira com o que você quer jogar: \n[1] PAR \n[2] IMPAR \nSua opção: '))
            while sel not in [1, 2]:
                sel = int(input(('''Insira com o que você quer jogar: \n[1] PAR \n[2] IMPAR \nSua opção: ''')))
            break

        except ValueError:
            print('Insira um valor valido!')

    sleep(0.5)

    # ---------------escolha do valor do usuario---------------

    while True:
        try:
            escolha_player = int(input('Insira um número entre 0 e 5: '))
            while escolha_player not in [0, 1, 2, 3, 4, 5]:
                escolha_player = int(input('Insira um número entre 0 e 5: '))
            break

        except ValueError:
            print('Insira um valor valido!')

    sleep(0.5)

    ##---------------escolha do valor e opção do pc---------------

    escolha_num_pc = randint(0, 5)
    if sel == 1:
        escolha_op_pc = 2
    else:
        escolha_op_pc = 1

    ##---------------varificação de quem ganhou---------------

    if sel == 1:
        teste1 = escolha_num_pc + escolha_player
        if teste1 % 2 == 0:
            ganhador = 'Player'
            tipo = 'PAR'
        else:
            ganhador = 'Pc'
            tipo = 'IMPAR'

    if sel == 2:
        teste1 = escolha_num_pc + escolha_player
        if teste1 % 2 == 0:
            ganhador = 'Pc'
            tipo = 'PAR'
        else:
            ganhador = 'Player'
            tipo = 'IMPAR'

    ##---------------varificação de quem ganhou---------------

    if ganhador == 'Pc':
        print(f'--------Você PERDEU!-------- \nVocê escolheu : {'PAR' if sel == 1 else 'IMPAR'} \nO seu número foi: {escolha_player} \nA escolha da maquina foi: {escolha_num_pc} '
              f'\nA soma das ecolhas é: {escolha_player + escolha_num_pc} {[tipo]}')
        sleep(0.5)
    else:
        print(f'--------Você GANHOU!-------- \nVocê escolheu : {'PAR' if sel == 1 else 'IMPAR'} \nO seu número foi: {escolha_player}  \nA escolha da maquina foi: {escolha_num_pc}'
              f'\nA soma das ecolhas é: {escolha_player + escolha_num_pc} {[tipo]}')
        sleep(0.5)

    #---------------contador de vitorias---------------

    cont +=1

    # ---------------Fim---------------

    if ganhador == 'Player':
        if cont == 1:
            print('''VocÊ consquistou um VITORIA! \nContinue até PERDER para encerrar e vér seu placar!''')
            sleep(0.5)
        else:
            print('''VocÊ consquistou mais uma VITORIA! \nContinue até PERDER para encerrar e ver seu placar!''')
            sleep(0.5)
    elif ganhador == 'Pc':
        print(f'Seu TOTAL de virotias foi: {cont}')
        break

    sleep(1)
