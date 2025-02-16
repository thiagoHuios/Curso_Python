print('Calculador de Peso')
print('Insira o peso de 5 pessoas para saber quem é o maior e menor:')

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input(f'Insira o {p} peso em Kg: '))
    if p == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso


print('O a maior peso lido foi: {}. \nO menor peso lido foi: {}.'.format(maior, menor))
