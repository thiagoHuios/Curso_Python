soma_idades = 0
idade_velho = 0
nome_velho = ''
mulheres_novas = 0

while True:
    try:
        qtd = int(input('Insira quantos pessoas serão analisadas: '))
        break
    except ValueError:
        print('Insira uma quantidade válida!')

for bando_dados in range(1, (qtd + 1)):
    nome = input(f'Insira o nome da {bando_dados}° pessoa: ')
    idade = int(input(f'Insira o idade da {bando_dados}° pessoa: '))
    sexo = input(f'Insira o sexo da {bando_dados}° pessoa: \n[1] Masculino \n[2] Feminino \nSua opção: ')
    soma_idades += idade
    if sexo == '2' and idade < 20:
        mulheres_novas += 1
    if bando_dados == 1 and sexo == '1':
        idade_velho = idade
        nome_velho = nome
    if idade > idade_velho and sexo == '1':
        idade_velho = idade
        nome_velho = nome

média_idade = soma_idades / bando_dados

print('A média das idades apresentadas é: {:.1f}'.format(média_idade))
print('O nome do homem mais veho é: {}'.format(nome_velho))
if mulheres_novas > 0:
    print('Temos {} mulheres abaixo de 20 anos.'.format(mulheres_novas))
