tupla = ()
contador_nome = total_compra = 0
contador_preço = total = 1

while True:
    try:
        quantidade_produtos = int(input('Insira a quantidade de produtos: '))
        break
    except ValueError:
        print('Insira um valor válido!')

for c in range(1, quantidade_produtos + 1):
    nome = (str(input(f'Insira o nome do produto {c}: ')),)
    tupla += nome
    while True:
        try:
            preço = (float(input(f'Insira o valor do produto {c}: R$')),)
            break
        except ValueError:
            print('Insira um valor válido!')
    tupla += preço

print('-'* 40)
print('{:^40}'.format(' LISTAGEM DE PRODUTOS '))
print('-'* 40)

for lista in range(0, quantidade_produtos):
    print(f'{tupla[contador_nome]:{'.'}<31}R${tupla[contador_preço]:>7.2f}')
    contador_nome += 2
    contador_preço += 2

for preço_total in range(0, quantidade_produtos):
    total_compra += tupla[total]
    total += 2

print('-'* 40)

print(f'\nPreço Total da compra foi: R${total_compra}')
print('-'* 40)

while True:
    while True:
        try:
            pagamento = float(input('Insira o valor do pagamento: '))
            break
        except ValueError:
            print('Insira um valo válido!')
    if pagamento >= total_compra:
        break
    print('O valor precias ser maior que o total da compra!')

print('-'* 40)

print(f'Valor do troco: R${pagamento - total_compra:.2f}')

print('-'* 40)
