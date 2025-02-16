numeros = []
numeros_pares = []
numeros_impares = []

while True:
    try:
        qtd_numeros = int(input('Insira quantos numeros deseja analisa: '))
        for n in range(1, qtd_numeros + 1):
            numeros.append(input(f'Insira o {n}º numero: '))
        break
    except ValueError:
        print('Insira um valor válido!')

print(f'\nOs números inserido foram: {numeros}')

for nu in numeros:
    if nu % 2 == 0:
        numeros_pares.append(nu)
    else:
        numeros_impares.append(nu)

if len(numeros_pares) > 0:
    print(f'Os numeros pares são: {numeros_pares}')
else:
    print('Essa lista não tem números pares!')
if len(numeros_impares) > 0:
    print(f'Os numeros pares são: {numeros_impares}')
else:
    print('Essa lista não tem números impares!')
