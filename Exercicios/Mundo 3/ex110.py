from utilitários import moedas

while True:
    try:
        num = int(input("Insira o preço a ser analisado: "))
        opa = int(input("Insira o valor para aumentar: "))
        opd = int(input("Insira o valor para dimnuir: "))
        break
    except ValueError:
        print("Insirá um valor válido!")

moedas.resumo(num, opa, opd)


