preço_normal = float(input('Insira o valor do produto: R$'))
forma_pagamento = int(input('Insira a forma de pagamento: 1: Dinheiro, 2: Cheque ou 3: Cartão: '))

while forma_pagamento not in [1 , 2 ,3]:
    print('Insira uma forma de pagamento valida!')
    print('''1: Dinheiro \n2: Cheque \n3: Cartão''')
    forma_pagamento = int(input('Escolha a opção: '))

if forma_pagamento == 1:
    desconto = preço_normal * 0.10
    print('O produto no valor de R${:.2f},na forma de dinheiro, recebera do desconto de 10% (R${:.2f}) \nSaindo por R${}.'.format(preço_normal, desconto, (preço_normal - desconto)))
elif forma_pagamento == 2:
    desconto = preço_normal * 0.10
    print('O produto no valor de R${:.2f}, Na forma de cheque, recebera do desconto de 10% (R${:.2f}) \nSaindo por R${:.2f}.'.format(preço_normal, desconto,(preço_normal - desconto)))
elif forma_pagamento == 3:
    parcelas = int((input('Insira o número de parcelas: ')))

    while parcelas == 0:
        print('Tente novamente!')
        parcelas = int((input('Insira o número de parcelas valido! ')))

    if parcelas == 1:
        desconto = (preço_normal * 0.05)
        print('O produto no valor de R${:.2f}, Na forma de cartão a vista, recebera do desconto de 5% (R${:.2f}) \nSaindo por R${:.2f}.'.format( preço_normal, desconto, (preço_normal - desconto)))
    if parcelas == 2:
        print('O produto na forma de cartão em duas parcelas, sairá por R${:.2f} SEM JUROS, sendo cada parcela a: R${:.2f}.'.format(preço_normal, (preço_normal / 2)))
    if parcelas > 2:
        juros = preço_normal * 0.2
        print('O produto no valor de: R$ {:.2f} na forma de cartão acima de duas parcelas tem um juros de 20% (R${:.2f}), e sairá por R${:.2f}.'.format(preço_normal, juros, (preço_normal + juros)))
        print('Com {}x no valor de R${:.2f} cada parcela'.format(parcelas, (preço_normal + juros) / parcelas))