print('=' * 40)
print('CAIXA ELETRONICO')
print('=' * 40)

nota_cinq = nota_vint = nota_dez = nota_um = geral = 0

while True:
    try:
        valor_saque = int(input('Insira o valor do saque desejado: '))
        break
    except ValueError:
        print('Insira um valor valido!')

total = valor_saque
cel = 50
total_cel = 0

print('=' * 40)

while True:
    if total >= cel:
        total -= cel
        total_cel += 1
    else:
        if total_cel > 0:
            print(f'A quantidade de cedulas de R${cel} é de: {total_cel}')
        elif cel == 50:
            cel = 20
            total_cel = 0
        elif cel == 20:
            cel = 10
            total_cel = 0
        elif cel == 10:
            cel = 5
            total_cel = 0
        elif cel == 5:
            cel = 1
        total_cel = 0
        if total == 0:
            break

print('=' * 40)

print('Acabou')
