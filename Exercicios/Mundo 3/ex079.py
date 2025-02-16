numeros = []
cid = True
while cid:
    while True:
        try:
            numero = int(input('Insira o numero desejado: '))
            break
        except ValueError:
            print('Insira um valor válido!')
    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).lower().strip()[0]
        if continuar not in 'SsNn':
            print('Insira uma opção valida!')
        if continuar == 'n':
            cid = False
            break
        else:
            break
    if numero not in numeros:
        numeros.append(numero)


print('\nA lista inserinda desconsiderando repetições foi:', end=' ')
numeros.sort()
for n in numeros:
    print(n, end=' ')