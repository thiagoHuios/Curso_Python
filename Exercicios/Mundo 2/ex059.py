num1 = float(input('Insira o primeiro número: '))
num2 = float(input('Insira o segundo número: '))

fim = False

while not fim:
    print('''Escolha qual a operação desejada:
    [1] Soma
    [2] Multiplicação
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa''')

    opção = int(input('Insira a opção desejada: '))
    while opção not in [5, 4, 3, 2, 1]:
        print('Insira um valor válido!')
        break

    if opção == 1:
        print('A soma de {}, e {}, é {}'.format(num1, num2, (num1 + num2)))
    elif opção == 2:
        print('A soma de {}, e {}, é {}'.format(num1, num2, (num1 * num2)))
    elif opção == 3:
        lista = [num1, num2]
        print('O maior número de {} e {}, é {}'.format(num1, num2, max(lista)))
    elif opção == 4:
        num1 = float(input('Insira o primeiro número: '))
        num2 = float(input('Insira o segundo número: '))
    elif opção == 5:
        fim = True
