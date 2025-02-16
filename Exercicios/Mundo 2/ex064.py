num = 0
cont = -1
soma = 0

while num != 999:
    soma += num
    num = int(input('Insira um núemro [Insira 999 para parar!]: '))
    cont += 1
print('A quantidade de números digitados até se digitar 999 foi: {}'.format(cont))
print('E a soma entre eles é: {}'.format(soma))