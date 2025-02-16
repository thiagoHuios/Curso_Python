import datetime

cadrastro = dict()

cadrastro['Nome'] = str(input('Insira o nome: '))
nasc = int(input('Insira o ano de nascimento: '))
ano_atual = datetime.date.today().year
cadrastro['Idade'] = (ano_atual - nasc)
cadrastro['CTPS'] = int(input('Insira o número da CTPS [Ou insira 0 se não tiver]: '))
if cadrastro['CTPS'] != 0:
    cadrastro['Ano Contratação'] = int(input('Insira o ano de contratação: '))
    cadrastro['Salario'] = float(input('Insira o valor do Salário: R$'))
    tempo_aposentar =  ano_atual - cadrastro['Ano Contratação']
    tempo_aposentar_demora = 35 - tempo_aposentar
    cadrastro['Idade Aposentadoria'] = cadrastro['Idade'] + tempo_aposentar_demora
    print('-' * 40)
    for k, v in cadrastro.items():
        print(f'{k} tem o valor de {v}')
else:
    print('-' * 40)
    for k, v in cadrastro.items():
        print(f'{k} tem o valor de {v}')
