from datetime import date
print('Leitor de Ano Bissexto')
ano = int(input('Insira o ano, para saber se ele é bissexto. Ou insira 0 para saber o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de: {}, É bissexto'.format(ano))
else:
    print('O ano de: {}, NÃO é bissexto'.format(ano))
