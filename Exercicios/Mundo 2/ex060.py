from math import factorial

print('Leitor de números fatoriais')

num = int(input('Insira o número a ser fatorado: '))

fat = num
ver = num

while num != 1:
    num -= 1
    fat = fat * num

print('O corespodende a {}! é: \n{}'.format(ver, fat))

#---------------------------------------------------------------

print('Fazendo com a repetição For:')

num1 = ver
num2 = ver

for fate in range((num1 - 1), 0, -1):
    num2 = num2 * fate

print(num2)

#---------------------------------------------------------------

print('{}! é corespondente: {}'.format(ver, factorial(ver)))