print('Calculador de descontos')
p=float(input('Digite o preço do produto: R$'))
d=float(input('Porcentagem que irá descontar:'))
r= p - (p * d / 100)
print('O produto com desconto aplicado é: {:.2f}'.format(r))
#r1=(p*d)/100
#r2=p-r1 (forma mais complexa e e com  mais variaveis, pode ser usado se as variaveis vieram a ser mais utilizadas)
