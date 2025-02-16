while True:
    números = (' Zero ', ' Um ', ' Dois ', ' Três ', ' Quatro ', ' Cinco ', ' Seis ', ' Sete ', ' Oito ', ' Nove ', ' Dez ',
           ' Onze ', ' Doze ', ' Treze ', ' Quatorze ', ' Quinze ', ' Dezesseis ', ' Dezessete ', ' Dezoito ',
           ' Dezenova ', ' Vinte ')

    while True:
        try:
            num_escolido = int(input('Insira um número entre 0 e 20 que quer ver por extenso: '))
            if 20 < num_escolido or num_escolido < 0:
                print('Insira um número válido!')
            else:
                print('\n {:=^45} \n'.format(números[num_escolido]))
                break
        except ValueError:
            print('Insira um valor válido!')





    while True:
        continuar = input('Deseja continuar? [S/N]: ').lower().strip()[0]
        if continuar not in 'SsNn':
            print('Escolha uma opção valida!')
        if continuar == 'n':
            exit()
        else:
            print('-' * 45, '\n')
            break
