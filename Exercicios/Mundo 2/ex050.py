print('Calculador de Números Pares')
print('Insira 6 números que vou somar apenas os pares')

list_numeros = []

while True:
    try:
        for p in range(1, 7):
            num = int(input(f'Insira o {p}° número: '))
            if num % 2 == 0:
                list_numeros.append(num)
        break
    except ValueError:
        print('Insira números inteiros validos!')

soma = sum(list_numeros)

print('A soma dos números {}, é: {}'.format(list_numeros, soma))

#Forma proposta pelo desafio:
'''
count = 0
soma = 0
for p in range(1, 7):
        num = int(input('Insira o {}° número: '))
        if p % 2 == 0:
            count += 1
            soma += 0
    print('Você informou {} números, e a soma deles é: {}'.format(count, soma))
'''