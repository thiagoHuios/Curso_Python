print('Conversor de Bases Númericas')
num = int(input('Insira um número inteiro para ser convertido: '))
print('Escolha qual opção para ser convertido:')
print('(1) Para converter para BINÁRIO \n(2) Para converter para OCTAL \n(3) Para converter para HEXADECIMAL')
base = str(input('Sua opção:')).strip()

while base not in ['1', '2', '3']:
    print('''Selecione um vallor valido:
    (1) Para converter para BINÁRIO
    (2) Para converter para OCTAL
    (3) Para converter para HEXADECIMAL''')
    base = str(input('Sua opção:')).strip()

if base == '1':
    print('O numero {}, convertido em base binária, é: {}.'.format(num, bin(num)[2:]))
elif base == '2':
    print('O numero {}, convertido em base octal, é: {}.'.format(num, oct(num)[2:]))
elif base == '3':
    print('O número {}, convertido em base hexadecimal, é: {}.'.format(num, hex(num)[2:]))
