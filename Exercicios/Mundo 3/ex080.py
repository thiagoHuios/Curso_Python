numeros = []

while True:
    try:
        qtd = int(input('Insira quantos numeros quer analisar: '))
        break
    except ValueError:
        print('Insira um valor válido!')

for n in range(1, qtd + 1):
    numero = int(input(f'Insira o {n}º numero: '))
    if n == 1:
        numeros.append(numero)
        print(f'Numero adicionado no inicio da lista!')
    elif numero >= max(numeros):
        numeros.insert(len(numeros), numero)
        print('Numero adicionado no final da lista!')
    elif numero <= min(numeros) and numero != max(numeros):
        numeros.insert(numeros.index(min(numeros)), numero)
        print(f'Numero adicionado no inicio da lista!')
    elif max(numeros) > numero > min(numeros):
        for i, o in enumerate(numeros):
            if numero < o:
                numeros.insert(i, numero)
                print(f'Numero foi adicionado na posição: {i}')
                break

print('-' * 60, f'\nOs valores digitados em ordem foram {numeros}')

#Solução alternativa

lista = []

for c in range(0, 5):
    num = int(input('Insira um número: '))
    if c == 0 or lista[-1] < num:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1

print(lista)


