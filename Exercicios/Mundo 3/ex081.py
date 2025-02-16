numeros = []

while True:
    try:
        numero = int(input('Insira um número: '))
        numeros.append(numero)
        continuar = str(input('Deseja continuar [S/N]: ')).lower().strip()[0]
        if continuar not in 'SsNn':
            print('Escolha uma opção valida!')
        elif continuar == 'n':
            break
    except ValueError:
        print('Insira um valor válido!')

print(f'\nForam inseridos {len(numeros)} sendo eles: \n{numeros}')
numeros.sort(reverse=True)
print(f'A lista em ordem decrescente é: \n{numeros}')
if 5 in numeros:
    if numeros.count(5) > 1:
        print('O numero cinco foi inserido é esta presente nas posições:' , end=' ')
        for i, cinc in enumerate(numeros):
            if cinc == 5:
                print(i, end=' ')
    else:
        print(f'O numero cinco foi inserido na posição: {numeros.index(5)}')
else:
    print('Não foi inserido nenhum número 5 na lista!')
