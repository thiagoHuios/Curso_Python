print('Analisador de número')
num = float(input('Digite um número para saber se é par ou impar: '))
if int(num) % 2 == 0:
    print('Esse número é {}par{}'.format('\033[32m', '\033[30m'))
else:
    print('Esse número é {}impar{}'.format('\033[31m', '\033[30m'))

