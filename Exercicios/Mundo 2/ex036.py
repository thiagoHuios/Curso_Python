print('Validação de Emprestimo')
casa = float(input('Insira o valor da casa: R$'))
salário = float(input('Insira o valor do Salário: R$:'))
anos = int(input('Isnira em quantos anos para pagar a casa: '))

prestanção_mensal = casa / (anos * 12)

if prestanção_mensal <= (salário * 0.30):
    print('Parabéns seu emprestimo foi aprovado, o valor das parcelas mensais  de casa de R${}, será de: R${}, por {} messes'.format(prestanção_mensal, casa, (anos * 12)))
else:
    print('Infelizmente o valor da prestação mensal de: R${:.2f} de uma casa de R${:.2f}, é superior a 30% ({:.2f}) de seu salário. Seu emprestimo foi negado!'.format(prestanção_mensal, casa, (salário * 0.30)))