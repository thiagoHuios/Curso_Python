aluno = dict()

aluno['Nome'] = str(input('Insira o nome do aluno: '))
aluno['Média'] = float(input(f'Insira á media do {aluno['Nome']}: '))

if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')