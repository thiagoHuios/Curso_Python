print('Conversor de Real para Dollar e Euro')
v=float(input('Qual o valor da sua carteira: R$'))
d = v / 6.19
e = v / 6.41
print('Seu valor de R${:.2f} compra US${:.2f}'.format(v, d))
print('Seu valor de R${:.2f} compra €{:.2f}'.format(v, e))
#Lembre sempre utlizar pontos ao inves de virgulas, pois o python não as reconhece
