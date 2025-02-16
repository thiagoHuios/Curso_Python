cadrastro = list()

while True:
    nome = str(input('Insira o nome do aluno: '))
    while True:
        try:
            nota1 = (float(input('Insira a primeira nota do aluno: ')))
            nota2 = (float(input('Insira a segunda nota do aluno: ')))
            break
        except ValueError:
            print('Insira um valor válido!')
    média = (nota1 + nota2) / 2
    cadrastro.append([nome, [nota1, nota2], média])
    coninuação = str(input('Desja inserir mais alunos? [S/N]: ')).strip().lower()[0]
    if coninuação in 'Nn':
        print('-' * 64)
        break
    print('-' * 64)

print(f'No. {'Nome':<20} Média \n')

for i, c in enumerate(cadrastro):
    print(f'{i:<2}  {c[0]:<20} {(c[2]):.1f}')
print('-' * 64)

while True:
    opção = str(input('Insira o numero do aluno que deseja ver as notas ou [FECHAR]: ').upper().strip())
    if opção.isdigit():
        opção = int(opção)
        if len(cadrastro) >= opção >= 0:
            print('-' * 64)
            print(f'{cadrastro[opção][0]}, tirou as seguintes notas: {cadrastro[opção][1]}')
            print('-' * 64)
    elif opção == 'FECHAR':
        break