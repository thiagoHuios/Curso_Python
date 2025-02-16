soma_produtos = produtos_caros = preço_mais_caro = produto_mais_barato = 0
nome_produto_caro = nome_produto_barato = ''
cont_números = 1

while True:
    print('{:=^20}'.format(' CAIXA - CADASTRO '))
    print('-' * 40)

    while True:
        try:
            nome_produto = str(input(f'Insira o nome do produto {cont_números}: '))
            preço_produto = int(input(f'Insira o valor do {cont_números} produto R$: '))
            break
        except ValueError:
            print('Insira um valor valido!')

    soma_produtos += preço_produto

    if preço_produto > 1000:
        produtos_caros += 1
    if cont_números == 1:
        preço_mais_caro = preço_produto
        nome_produto_caro = nome_produto
        nome_produto_barato = preço_produto
        produto_mais_barato = preço_produto
    if preço_produto > preço_mais_caro:
        preço_mais_caro = preço_produto
        nome_produto_caro = nome_produto
    if preço_produto < produto_mais_barato:
        produto_mais_barato = preço_produto
        nome_produto_barato = nome_produto

    cont_números += 1

    seq = str(input('Deseja continuar comprando? [S/N]: ')).lower().strip()[0]

    while seq not in ['s', 'n']:
        seq = str(input('Deseja continuar comprando? [S/N]: ')).lower().strip()[0]

    if seq == 'n':
        break
    print('-' * 40)

print(f'\nA soma da compra foi R${soma_produtos:.2f}')
print(f'Quantidade de produtos acima de R$ 1000: {produtos_caros}')
print(f'O produto mais caro foi: {nome_produto_caro}, que custa: R${produto_mais_barato}')
print(f'O produto mais barato foi: {nome_produto_barato}, que custa: R${produto_mais_barato}')
