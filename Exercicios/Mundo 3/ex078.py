numeros = []

while True:
    try:
        qtd_numeros = int(input('Insira a quantidade de números a serem analisados: '))
        if qtd_numeros == 0:
            exit()
        break
    except ValueError:
        print('Insira um valor válido!')

for n in range(1, (qtd_numeros + 1)):
    while True:
        try:
            numero = int(input(f'Insira o {n}º número: '))
            numeros.append(numero)
            break
        except ValueError:
            print('Insira um valor válido!')

maior = max(numeros)
menor = min(numeros)

print(f'A inserida foi {numeros}')

if numeros.count(maior) > 1:
    print(f'\nO maior número da lista foi {maior} nas posições: ', end='')
    for i, ma in enumerate(numeros):
        if ma == maior:
            print(i, end=' ')
else:
    print(f'\nO maior número da lista foi {maior} nas posiçãos: {numeros.index(maior)}')

if numeros.count(menor) > 1:
    print(f'\nO menor número da lista foi {menor} nas posições: ', end='')
    for i, me in enumerate(numeros):
        if me == menor:
            print(i, end=' ')
else:
    print(f'\nO menor número da lista foi {menor} na posição: {numeros.index(menor)}')