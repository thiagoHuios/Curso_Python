matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for li in range(1, 4):
    for co in range(1, 4):
        matrix[li - 1][co - 1] = int(input(f'Insira o valor da posição: [{li}, {co}]: '))

print('-' * 40)
for li in range(0, 3):
    for co in range(0, 3):
        print(f'[{matrix[li][co]:^5}]', end=' ')
    print('')