matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma3 = 0

for li in range(1, 4):
    for co in range(1, 4):
        while True:
            try:
                matrix[li - 1][co - 1] = int(input(f'Insira o valor da posição: [{li}, {co}]: '))
                break
            except ValueError:
                print('Insira um valor válido!')

print('-' * 40)
print(f'A matrix inserida foi: \n')

for li in range(0, 3):
    for co in range(0, 3):
        print(f'[{matrix[li][co]:^5}]', end=' ')
        if matrix[li][co] % 2 == 0:
            soma += matrix[li][co]
    soma3 += matrix[li][2]
    print('')

print('-' * 40)

print(f'A soma de todos os valores pares foi: {soma}')
print(f'A soma dos valores da terceira coluna foi: {soma3}')
print(f'O maior valor da segunda linha foi: {max(matrix[1])}')

