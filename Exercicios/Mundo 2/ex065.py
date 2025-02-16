soma = cont = maior = menor = 0
pgt = ''

while pgt not in ['n']:
    num = int(input('Insira um número: '))
    pgt = str(input('Você quer continuar? [S/N]')).lower().strip()
    while pgt not in ['s','n']:
        pgt = str(input('Você quer continuar? [S/N]')).lower().strip()
    cont += 1
    soma +=num
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor =  num

média = soma/cont

print('=-=' * 20)

print('''A soma é {}
Você digitou {} números
A média é: {}
O maior valor é: {}
E o menor valor é: {}'''.format(soma, cont, média, maior, menor))