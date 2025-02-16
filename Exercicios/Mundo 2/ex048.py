print('A soma de todos números impares que são multiplos de 3, entre 1 a 500 e:')

s = 0
contador = 0

for i in range(1, 501):
    if i % 2 == 1 and i % 3 == 0:
        contador += 1
        s += i
print('A soma de todos {} valores, é: {}'.format(contador, s))

