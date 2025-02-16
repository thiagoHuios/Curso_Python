from datetime import datetime
print('Contador de Maior Idade')
print('Maior idade é considerado 21')

print('Insira O ano de nascimento das 7 pessoas:')

agrup = []
maior = 0
menor = 0

for d in range(1, 8):
    nasc = int(input(f'Insira a data da {d} pessoa: '))
    idade = datetime.today().year - nasc
    agrup.append(idade)
    if idade >= 21:
        maior += 1
    elif idade < 21:
        menor += 1


if maior == 1:
    print('Das datas de nacismento inseridas, apenas uma pessoa, é maiores de idade')
else:
    print('Das datas de nacismento inseridas: {} \n{} pessoas, são maiores de idade \n{} pessoas, são menores de idade'.format(agrup, maior, menor))

