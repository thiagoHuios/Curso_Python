pessoa = dict()
pessoas = list()
mulheres = list()
pessoas_acima_média = list()
soma_idade = 0

while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Insira o nome: '))
    while True:
        pessoa['Sexo'] = str(input('Insira o sexo [M/F]: ')).strip().upper()[0]
        if pessoa['Sexo'] in 'MmFf':
            break
    while True:
        try:
            pessoa['Idade'] = int(input('Insira a idade: '))
            soma_idade += pessoa['Idade']
            break
        except ValueError:
            print('Insira um valor válido!')
    pessoas.append(pessoa.copy())
    while True:
        continuar = str(input('Deseja inserar mais pessoas [S/N]: ')).strip().lower()[0]
        if continuar not in 'SsNn':
            print('Insira uma opção valida')
        elif continuar == 'n':
            break
    if continuar == 'n':
        break

qtd_pessoas = len(pessoas)
média = soma_idade / qtd_pessoas

for p in pessoas:
    if p['Sexo'] == 'F':
        mulheres.append(p['Nome'])
    if p['Idade'] > média:
        pessoas_acima_média.append(p)

print('-' * 20)

print(f'O grupo tem {qtd_pessoas}. \nA média de idade é de {média:.1f} anos')
print(f'A lista mulheres cadrastradas foram: ', end='')

for i, m in enumerate(mulheres):
    if i < (len(mulheres) -1) and len(mulheres) != 1:
        print(m, end=', ')
    elif len(mulheres) == 1:
        print(f'{m}.')
    elif i == (len(mulheres) - 1):
        print(f'{m}.')

print('As pessoas com idade acima dá média foram: ')

for pam in pessoas_acima_média:
    print(pam)