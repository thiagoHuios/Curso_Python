# Função do IMC
def imc(peso, altura):
    imc_result = peso / pow(altura, 2)
    if imc_result < 18.5:
        imc_result_text = 'Abaixo do Peso'
    elif 25 > imc_result >= 18.5:
        imc_result_text = 'Peso Normal'
    elif 29.9 > imc_result >= 25:
        imc_result_text = 'Excesso de Peso'
    elif 40 > imc_result >= 29.9:
        imc_result_text = 'Obsidade'
    elif imc_result > 40:
        imc_result_text = 'Obsidade Morbida'

    return [imc_result, imc_result_text]

print(f'{'Cadrastro de IMC':-^40}\n')

nome_peso = []
dados = []
pesados = []
leves = []
maior = menor = 0

while True:
    nome_peso.append(str(input('Insira um nome: ')))
    nome_peso.append((float(input('Insira o peso: '))))
    nome_peso.append((float(input('Insira a altura: '))))

    if len(dados) == 0:
        maior = nome_peso[1]
        menor = nome_peso[1]
    elif nome_peso[1] >= maior:
        meior = nome_peso[1]
    elif nome_peso[1] <= menor:
        menor = nome_peso[1]

    dados.append(nome_peso[:])
    nome_peso.clear()

    continuar = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    if continuar in 'Nn':
        print('-' * 40)
        break
    print('-'*40)

for test_peso in dados:
    if test_peso[1] == menor:
        leves.append(test_peso[0])
    elif test_peso[1] == maior:
        pesados.append(test_peso[0])

print(f'\nForam cadrastradas {len(dados)} pessoas. Sendo elas: \n')
for p in dados:
    print(f'{p[0]} com o peso de {p[1]}Kg e a altura de: {p[2]}m.')
    imc_variavel = imc(p[1], p[2])
    print(f'Tendo seu imc de: {imc_variavel[0]:.2f}, {imc_variavel[1]} \n')
print('-'*40)
print(f'O maior pesso foi: {maior}Kg, das pessoas: {pesados}')
print(f'O menor peso foi: {menor}Kg, das pessoas: {leves}')
print('-'*40)
