print('Comparador de Números')
print('Insira dois números, para comparar qual é maior')
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

if num1 > num2:
    print('O primeiro número ({}), é maior'.format(num1))
elif num2 > num1:
    print('O segundo número ({}), é maior'.format(num2))
else:
    print('Não existe valor maior, os dois são iguais')