print('Calculador de Progressão Arritimedica')

primeiro_termo = int(input('Insira o priemiro termo da PA: '))
razão = int(input('Insira a razão da PA: '))
numero_termos = int(input('Insira o número de PA: '))

cont = 0
termo = primeiro_termo
total = 0
mais_termos = numero_termos

while mais_termos != 0:
    total += mais_termos
    while cont <= total:
        if cont == total:
            print('{}.'.format(termo))
        else:
            print('{}'.format(termo), end=', ')
        termo += razão
        cont += 1
    print('Insira a quantidade de termo para continar vendo a PA ou Insira [0] para finalizar.')
    mais_termos = int(input('Sua opção: '))

print('Foi feita uma PA de: {} termos'.format(total))


