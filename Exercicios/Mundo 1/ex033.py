#maneira proposta pelo exercicio:
print('Qual é o maior e o menor número')
a = float(input('Primeiro Valor: '))
b = float(input('Segundo Valor: '))
c = float(input('Terceiro Valor: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('Entre os valores {} \nO maior é: {} \nE o menor: {}'.format([a, b, c], maior, menor))

#Maneira que eu achei:
print('Qual número é maior, e qual é menor')
num = str(input('Insira tres números pra saber qual o maior e qual menor: ')).split()
print('Entre os numeros: {} \nO maior é: {} \nE o menor: {}'.format(num, max(num), min(num)))
