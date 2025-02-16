cont_idade = cont_homens = cont_mulheres = 0

while True:
    titulo = 'BANCO DE DADOS - CADRASTRO DE PESSOAS'
    print(str(titulo))
    print('-' * 40)
    while True:
        try:
            idade = int(input('Insira a idade: '))
            break
        except ValueError:
            print('Insira um valor válido!')
    sexo = str(input('Insira o sexo [M/F]: ')).lower().strip()[0]
    while sexo not in ['m', 'f']:
        sexo = str(input('Insira o sexo [M/F]: ')).lower().strip()[0]
    if idade > 18:
        cont_idade += 1
    if sexo == 'm':
        cont_homens += 1
    if sexo == 'f' and idade < 20:
        cont_mulheres += 1
    seq = str(input('Deseja continuar? [S/N]: ')).lower().strip()[0]
    while seq not in ['s', 'n']:
        seq = str(input('Deseja continuar? [S/N]: ')).lower().strip()[0]
    if seq == 'n':
        break
    print('-' * 40)

print('Foram cadastrados:')
if cont_idade == 1:
    print(f'Apenas {cont_idade} pessoa maior de 18 anos.')
else:
    print(f'{cont_idade} pessoas maiores de 18 anos.')
if cont_homens == 1:
    print(f'Apenas {cont_homens} homem.')
else:
    print(f'{cont_homens} homens.')
if cont_mulheres == 1:
    print(f'Apenas {cont_mulheres} mulher abaixo de 20 anos.')
else:
    print(f'{cont_mulheres} mulheres abaixo de 20 anos.')