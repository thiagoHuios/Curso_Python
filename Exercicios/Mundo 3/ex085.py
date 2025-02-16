numeros = [[], []]
for n in range(1, 8):
    while True:
        try:
            numero = int(input(f'Insira o {n}º: '))
            break
        except ValueError:
            print('Insira um valor válido!')
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

numeros[0].sort()
numeros[1].sort()
print('-' * 40)
print(f'Os numeros pares inseridos foram: {numeros[0]}. \nOs numeros impares inseridos foram: {numeros[1]}')
print('-' * 40)
